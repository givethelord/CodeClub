# Linux slocate命令
[返回Linux 命令目录](11.Linux命令大全.md)

Linux slocate命令查找文件或目录。

slocate本身具有一个数据库，里面存放了系统中文件与目录的相关信息。

## 语法
```bash
slocate [-u][--help][--version][-d <目录>][查找的文件]
```

### 参数：

* -d<目录>或--database=<目录> 　指定数据库所在的目录。
* -u 　更新slocate数据库。
* --help 　显示帮助。
* --version 　显示版本信息。

## 实例

* 使用指令"slocate"显示文件名中含有关键字"fdisk"的文件路径信息，输入如下命令：
    ```bash
    $ slocate fdisk #显示文件名中含有fdisk关键字的文件的路径信息 
    ```

* 执行以上命令后，指令执行的输出信息如下：
    ```bash
    $ slocate fdisk #显示文件名中含有fdisk 关键字的文件的路径信息  
    /root/cfdisk        #搜索到的文件路径列表  
    /root/fdisk  
    /root/sfdisk  
    /usr/include/grub/ieee1275/ofdisk.h  
    /usr/share/doc/util-Linux/README.cfdisk  
    /usr/share/doc/util-Linux/README.fdisk.gz  
    /usr/share/doc/util-Linux/examples/sfdisk.examples.gz  
    ```