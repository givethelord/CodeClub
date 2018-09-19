# Centos

1. 安装依赖包
```bash
yum install lzo-devel
yum install openssl-devel
yum install pam-devel
```

2. 关闭防火墙,设置关机禁止启动firewalld
```bash
service firewalld stop
systemctl disable firewalld
```

3. 添加openssl的MD5支持
```bash
export NSS_HASH_ALG_SUPPORT=+MD5
export OPENSSL_ENABLE_MD5_VERIFY=1
```

4. 解压文件,并安装openvpn
```bash
tar -zxvf openvpn-2.3.0.tar.gz
cd openvpn-2.3.0
./configure
make && make install
```

5. 上传证书和配置到目录(/etc/openvpn)
```
ca.crt
client.crt
client.key
client.ovpn
```

6. 运行openvpn
```bash
nohup openvpn --cd /erc/openvpn --daemon --config /etc/openvpn/client.ovpn
```


