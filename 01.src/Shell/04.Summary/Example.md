# 样例

1. 查找当前目录下占用为0字节的文件并删除
>find ./ -type f -size 0 -exec rm -rf {} ; #此命令不要用于对根目录0字节文件的操作

2. 将系统进程按内存占用大小排列显示出来
>ps -e -o "%C : %p : %z : %a"|sort -k5 -nr

3. 将系统进程按CPU占用大小排列显示
>ps -e -o "%C : %p : %z : %a"|sort -nr

4. 匹配某文件中某一行并进行内容替换
>sed -i '/Root/s/no/yes' /etc/ssh/sshd_config #先匹配到Root，再将此行no替换为yes

5. 显示所有运行级别为3并开机启动的服务
>ls /etc/rc3.d/S* |cut -c 15- #rc3.d中S开头即为运行级别3的服务，并用cut截取第15个字符后面的内容

6. 取得eth0网卡的IP地址
>方法1：ifconfig | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}'方法2：ifconfig eth0 |grep "inet addr:" |awk '{print $2}'|cut -c 6-

7. TCP抓包工具分析80端口数据流
>tcpdump -c 10000 -i eth0 -n dst port 80

8. 查询昨天的日期
>date --date=yesterday

9. 删除所有空目录
>find /data -type d -empty -exec rm -rf {} ; #最好不要在/目录下执行此命令

10. 删除5天前的文件
>find /data -mtime +5 -type f -exec rm -rf {};

11. 强制踢出终端用户
>pkill -KILL -t pts/1

12. 将来自80端口的请求转发到8080端口
>iptables -A PREROUTING -p tcp -m tcp --dport 80 -j DNAT --to-destination 127.0.0.1:8080

13. linux服务器之间传文件
>scp ~/test.txt root@192.168.0.10:/data/ #将个人主目录下test.txt传到远程主机的/data目录下

14. 对大文件进行分割
>split -l 1000 message.log message #按每个文件1000行来分割split -b 5m message.log message #按每个文件5M来分割