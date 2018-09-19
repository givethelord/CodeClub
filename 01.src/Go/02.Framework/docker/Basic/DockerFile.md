# Dockerfile
　　从刚才的 docker commit 的学习中，我们可以了解到，镜像的定制实际上就是定制每一层所添加的配置、文件。如果我们可以把每一层修改、安装、构建、操作的命令都写入一个脚本，用这个脚本来构建、定制镜像，那么之前提及的无法重复的问题、镜像构建透明性的问题、体积的问题就都会解决。这个脚本就是 Dockerfile。

　　Dockerfile 是一个文本文件，其内包含了一条条的指令(Instruction)，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建。

1. 系统环境
    ```bash
    #cat /etc/redhat-release
    CentOS Linux release 7.3.1611 (Core)
    ```

2. 编写Dockerfile文件
   ```bash
   ##FROM 指定基础镜像
   FROM centos:7.2.1511
   ##作者标签，联系方式
   LABEL maintainer "wtf@datagrand.com"
   ##环境变量硬编码及时区
   ENV ENVIRONMENT production
   RUN cd / && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
   ##yum 基础工具，记住clean
   RUN yum clean all \
   && yum makecache \
   && yum install -y wget gcc gcc-c++ python-devel bzip2 \
   && yum clean all
   COPY docker-ce-17.09.0.ce-1.el7.centos.x86_64.rpm /usr/local/docker-ce-17.09.0.ce-1.el7.centos.x86_64.rpm
   ADD docker.txt  /tmp/docker.txt
   ##docker 基础工具及版本
   RUN cd /usr/local \
   && yum install -y docker-ce-17.09.0.ce-1.el7.centos.x86_64.rpm
   ##镜像启动命令
   CMD ["systemctl","start","docker"]
   ```
   ```
   文件解释：
   FROM： 必不可少的命令，从某个镜像作为基。如 FROM <image_name> ，或者 FROM <image_name>:<tag>. 如果不加tag，默认为latest。先从本地镜像仓库去搜索基镜像，如过本地没有，在去网上docker registry去寻找。,除了选择现有镜像为基础镜像外，Docker 还存在一个特殊的镜像，名为 scratch。这个镜像是虚拟的概念，并不实际存在，它表示一个空白的镜像。
   MAINTAINER：标明该Dockerfile作者及联系方式，可忽略不写
   RUN：建立新的镜像时，可以执行在系统里的命令，如安装特定的软件以及设置环境变量。
   ENV：设置系统环境变量（注意：写在/etc/profile里的命令在dockerfile这里会不生效，所以为改成ENV的方式）
   EXPOSE：开放容器内的端口，但不和宿主机进行映射。方便在宿主机上进行开发测试。（如需映射到宿主机端口，可在运行容器时使用 -p host_port:container_port）
   CMD：设置执行的命令，经常用于容器启动时指定的某个操作。如执行自定义脚本服务，或者是执行系统命令。CMD 只能存在一条，如在Dockerfile中有多条CMD的话，只有最后一条CMD生效！
   ```

3. 文件目录路径
    ```bash
    #pwd
    /root/dockerfile
    说明：上面是当前文件路径，目录内容如下：
    #ls
    docker-ce-17.09.0.ce-1.el7.centos.x86_64.rpm
    docker.txt
    Dockerfile
    docker_shell.sh
    ##docker-ce-17.09.0.ce-1.el7.centos.x86_64.rpm、Dockerfile、docker_shell.sh，docker.txt在     同一个目录下！
    docker.txt的内容：
    #cat docker.txt
    this is a test
    ```

4. 编写脚本docker_shell.sh
    ```bash
    #cat docker_shell.sh
    TIMENOW=`date +%y.%m.%d.%H%M`
    ##-f 指定文件 ， -t 指定生成镜像名称 ， 冒号后为版本号 ， 例子 ： ##docker_image:17.08.01.1311 "."为当前目录
    docker build -f Dockerfile -t docker_image:${TIMENOW} .
    ```

5. 执行docker_shell.sh
    ```bash
    #sh docker_shell.sh
    ```

6. 查看镜像
    ```bash
    #docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    docker_image        18.01.14.1702       d227774c2960        23 minutes ago      588MB
    ```

7. 镜像压缩与打包
    ```bash
    #docker save d227774c2960 |gzip>docker_file.tgz
    #ls
    docker-ce-17.09.0.ce-1.el7.centos.x86_64.rpm
    docker_file.tgz
    docker.txt
    Dockerfile
    docker_shell.sh
    ```

8. 镜像导入
    ```bash
    ##把docker里原有docker_image镜像删除，导入压缩打包后的镜像
    #docker rmi d227774c2960
    #docker images|grep docker_image
    #docker load < docker_file.tgz
    #docker tag  d227774c296x docker_image:18.01.14.1702
    说明：d227774c296x是docker load < docker_file.tgz 加载镜像生成的ID号！
    ```

9. 启动镜像
    ```bash
    ##镜像名字是wtf_shiyan
    #docker run -itd --name=wtf_shiyan 34b5ef62c921
    #docker exec -it wtf_shiyan /bin/bash
    ```