# 安装指导

1. Docker安装
    * [Centos7安装Docker](http://www.runoob.com/docker/centos-docker-install.html)


2. 下拉镜像
    1. 根据[项目](https://github.com/SeleniumHQ/docker-selenium)选择镜像
        ```
        selenium/base: 包含 Java 运行组件及 Selenium jar 文件的基础镜像
        selenium/hub: 运行 Selenium Grid Hub 的镜像
        selenium/node-base: 包含虚拟桌面环境及 VNC 支持的 Selenium Grid Node 基础镜像
        selenium/node-chrome: 包含 Chrome 的 Selenium node 镜像。需要连接 Selenium Grid Hub 使用。
        selenium/node-firefox: 包含 firefox 的 Selenium node 镜像。需要连接 Selenium Grid Hub 使用。
        selenium/standalone-chrome: 包含 Chrome 的 Selenium standalone 镜像（不需要连接 Selenium Grid Hub）
        selenium/standalone-firefox: 包含 Firefox 的 Selenium standalone 镜像（不需要连接 Selenium Grid Hub）
        selenium/standalone-chrome-debug: 包含 Chrome 和 VNC Server 的 Selenium standalone 镜像
        selenium/standalone-firefox-debug: 包含 Firefox 和 VNC Server 的 Selenium standalone 镜像
        selenium/node-chrome-debug: 包含 Chrome 和 VNC Server 的 Selenium Grid Node 镜像，需要连接 Selenium Grid Hub 使用
        selenium/node-firefox-debug: 包含 Firefox 和 VNC Server 的 Selenium Grid Node 镜像，需要连接 Selenium Grid Hub 使用
        ```
    2. 下拉镜像
        ```bash
        docker pull selenium/hub
        docker pull selenium/node-chrome-debug
        docker pull selenium/node-firefox-debug
        ```
3. 单机部署(4444为Hub默认端口,5900为Node的VNC Server端口)
    ```bash
    docker run -d -p 4444:4444 --name selenium-hub selenium/hub
    docker run -d -p 5900:5900 --link selenium-hub:hub -v /dev/shm:/dev/shm --name chrome selenium/hub
    docker run -d -p 5901:5900 --link selenium-hub:hub -v /dev/shm:/dev/shm --name firefox selenium/hub
    ```

4. 查看容器是否启动
    ```bash
    docker ps
    ```

5. 查看配置界面

    地址格式:https://[部署节点IP]:[hub的4444端口映射出去的端口,这里也为4444]/grid/console

# 使用指导
* 调用

    rf通过关键字(Open Browser)的参数remote_url去调用,调用地址:https://[部署节点IP]:[hub的4444端口映射出去的端口,这里也为4444]/wd/hub

    例如
    ```
    Open Browser    https://www.baidu.com    chrome    remote_url=http://1092.168.1.1:4444/wd/hub
    ```
* 使用VNC查看
    1. [地址](https://www.realvnc.com/download/viewer)下载VNC
    2. 使用vnc登录查看
        * Vnc Server:[部署节点IP]:[node的5900端口映射出去的端口]
        * 密码:默认为secret
* 查看日志
   ```
   docker logs -f [容器名]或者[容器id]
   ```

* 清理命令(重新部署时使用)
    ```bash
    docker kill $(docker ps -a -q)
    docker rm $(docker ps -a )
    ```

# 注意事项
* 本机和Docker网络互通,需要保证IP能内部转发:
    1. 打开ipv4能内部转发开关
        ```
        在/etc/sysctl.conf添加:net.ipv4.ip_forward=1
        注意：centos7还需要在/usr/lib/sysctl.d/50-default.conf里加入:net.ipv4.ip_forward=1
        ```
    2. 生效
        ```
        sysctl -p /etc/sysctl.conf
        ```
* 如果想使用容器使用主机的/etc/resolv.cnf
    * 一般容器在启动时被主机的/etc/resolv.cnf覆盖,所以部署容器的时候就需要配置好
    * 停止容器,修改主机/etc/resolv.cnf，然后再启动

* 如果想使用容器使用主机的/etc/hosts
    * 部署的时候用主机文件覆盖进去
        ```
        docker run -v /etc/hosts:/etc/hosts
        ```
    * 部署的时候传递host映射关系进去
    ```
        docker run --add-host host:ip
    ```