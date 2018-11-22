# windows7 安装Docker


## 下载、安装DockerToolbox.exe

1. 下载安装包:Docker针对Win10做了专门的Docker版本，其他旧版Windows操作系统安装的是[DockerToolbox.exe](https://docs.docker.com/toolbox/toolbox_install_windows/)

2. 基本按照默认即可，如果已经安装过Git，可以不勾选相应选项
    1) Docker Quickstart Terminal: 提供Docker的命令行操作
    2) Oracle VM VirtualBox: 打开可以看到有一个虚拟机，里面安装了Core Linux机器，名字为default。
    3) Kitematic (Alpha)：图形化的docker工具

## 启动Docker Quickstart Terminal

打开Docker Quickstart Termina,可能遇到下列问题:

* 下载boot2docker.iso很慢
    手动下载[boot2docker.iso](https://github.com/boot2docker/boot2docker/releases)放到C:\Users\<UserName>\.docker\machine\cache
* 未开启对虚拟化技术的支持(the computer doesn't have vt-x/amd-v enabled)
    到BIOS中手动开启硬件虚拟化技术，在Configuration项下将Intel Virtual Technology改为Enable

## 验证安装

```bash
docker version
docker run hello-world
```

## docker machine基本命令

1. docker客户端配置环境变量
    ```bash
    docker-machine env [OPTIONS] [arg...]
    ```

2. 检查机子信息
    ```bash
    docker-machine inspect
    ```

3. 查看虚拟机列表
    ```bash
    docker-machine ls [OPTIONS] [arg...]
    ```

4. 查看虚拟机状态
    ```bash
    docker-machine status [arg...]  //一个虚拟机名称
    ```

5. 启动虚拟机
    ```bash
    docker-machine start [arg...]  //一个或多个虚拟机名称
    ```

6. 停止虚拟机
    ```bash
    docker-machine stop [arg...]  //一个或多个虚拟机名称
    ```

7. 重启虚拟机
    ```bash
    docker-machine restart [arg...]  //一个或多个虚拟机名称
    ```