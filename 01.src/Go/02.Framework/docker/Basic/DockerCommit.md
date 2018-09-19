# 手动修改容器镜像

　　当我们运行一个容器的时候（如果不使用卷的话），我们做的任何文件修改都会被记录于容器存储层里。而 Docker 提供了一个 docker commit 命令，可以将容器的存储层保存下来成为镜像。换句话说，就是在原有镜像的基础上，再叠加上容器的存储层，并构成新的镜像。以后我们运行这个新镜像的时候，就会拥有原有容器最后的文件变化。

1. 先下载centos镜像
    ```bash
    [root@docker ~]# docker pull centos
    ```

2. 启动容器并进行配置
    1. 启动容器
          ```bash
          [root@docker ~]# docker run -it -d --name test-centos1 centos
          d72250ecaa5e3e36226a1edd749f494d9f00eddc4143c81ac3565aa4e551791a
          ```
          ```
            命令注释：-it :　进行交互式操作
            　　　　　-d :　等同于 -d=true,容器将会在后台运行，不然执行一次命令后，退出后，便是exit状态了。
            　　　　　--name : 容器启动后的名字，默认不指定，将会随机产生一个名字。或者使用 -name="containers_name"
            　　　　　centos：使用的镜像名称
          ```

    2. 进入容器，安装ssh server，以及配置开机启动
        ```bash
        [root@docker ~]# docker exec -it test-centos1 /bin/bash
        [root@d72250ecaa5e /]# ifconfig
        bash: ifconfig: command not found
        ```
        注：命令最后参数 /bin/bash： 指进入容器时执行的命令（command）

    3. 我们检查了下容器，暂时安装以下必用的软件吧 net-tools，openssh-server
       ```bash
       [root@d72250ecaa5e /]# yum install openssh-server net-tools -y
       ```
    4. 创建ssh 所需的目录，并在根目录创建sshd 启动脚本
        ```bash
        [root@d72250ecaa5e /]# mkdir -pv /var/run/sshd
        mkdir: created directory '/var/run/sshd'

        [root@d72250ecaa5e /]# cat /auto_sshd.sh
        #!/bin/bash
        /usr/sbin/sshd -D
        [root@d72250ecaa5e /]# chmod +x /auto_sshd.sh
        ```
     5. 修改容器内root 的账户密码
         ```bash
         [root@d72250ecaa5e /]# echo "root:iloveworld" | chpasswd
         ```
    6. 生成ssh 主机dsa 密钥（不然ssh 该容器时，会出现错误。）
        ```bash
        [root@d72250ecaa5e /]# ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
        [root@d72250ecaa5e /]# ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
        ```
     7. 我们加一个history记录的时间功能吧，这样方便后期查看
         ```bash
         echo 'export HISTTIMEFORMAT="%F %T `whoami` "' >> /etc/profile
         ```
         OK，配置基本完毕咯。清理命令历史纪录，之后退出容器。现在可以生成一个新的docker 镜像了。
3. 配置完成后，进行打包成新的镜像
    ```bash
    [root@docker ~]# docker commit test-centos1 centos_sshd:7.0
    sha256:6e3330b30dfff5f029f102874e54cfffffbc37dcf2a4eb7304c817148fbc944d

    [root@docker ~]# docker images
    REPOSITORY          TAG         IMAGE ID      CREATED       SIZE
    centos_sshd         7.0         6e3330b30dff    8 seconds ago    310.1 MB
    docker.io/ubuntu       latest       e4415b714b62    12 days ago     128.1 MB
    ```
    命令注释：commit： 提交一个具有新配置的容器成为镜像，后面跟容器的name 或者容器Id ，最后是生成新镜像的名字
    更新：这条命令更方便以后启动，如下：
    ```bash
    [root@docker ~]# docker commit --change='CMD ["/auto_sshd.sh"]' -c "EXPOSE 22" test-centos1 centos_sshd:7.0
    sha256:7bb4efd82c4ff1f241cbc57ee45aab1b05d214b1e9fcd51196696c67d480e70b
    ```
    命令注释： --change : 将后期使用此镜像运行容器时的命令参数、开放的容器端口提前设置好。
4. 验证
    1. 查看镜像，并启动新的容器
        ```bash
        [root@docker ~]# docker images
        REPOSITORY          TAG         IMAGE ID      CREATED       SIZE
        centos_sshd         7.0         7bb4efd82c4f    4 minutes ago    310.1 MB
        docker.io/ubuntu       latest       e4415b714b62    12 days ago     128.1 MB

        [root@docker ~]# docker run -d -it --name centos_7.0-1 centos_sshd:7.0
        ec17e553d5c4c60865afeb99df8dfd1f4e7d4ba6e1b0d5516f9127f09d1d6356
        [root@docker ~]# docker ps -a
        CONTAINER ID    IMAGE           COMMAND         CREATED       STATUS      PORTS     NAMES
        ec17e553d5c4    centos_sshd:7.0      "/auto_sshd.sh"     6 seconds ago    Up 5 seconds   22/tc
        ```
    2. 进行ssh测试，先查看一下该容器的ip，之后ssh。ok
        ```bash
        [root@docker ~]# docker exec centos_7.0-1 hostname -i
        172.17.0.4

        [root@docker ~]# ssh root@172.17.0.4
        The authenticity of host '172.17.0.4 (172.17.0.4)' can't be established.
        RSA key fingerprint is 87:88:07:12:ac:0a:90:28:10:e1:9e:eb:1f:d6:c9:9d.
        Are you sure you want to continue connecting (yes/no)? yes
        Warning: Permanently added '172.17.0.4' (RSA) to the list of known hosts.
        root@172.17.0.4's password:
        Last login: Tue Nov 29 16:00:49 2016 from gateway

        [root@ec17e553d5c4 ~]# w
         16:34:17 up 63 days, 7:49, 1 user, load average: 0.00, 0.02, 0.05
        USER   TTY   FROM       LOGIN@  IDLE  JCPU  PCPU WHAT
        root   pts/0  gateway     16:34  1.00s 0.00s 0.00s w
        [root@ec17e553d5c4 ~]# ping gateway
        PING gateway (172.17.0.1) 56(84) bytes of data.
        64 bytes from gateway (172.17.0.1): icmp_seq=1 ttl=64 time=0.048 ms
        ```