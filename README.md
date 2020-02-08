## 设置静态ip

### ifconfig

获取本地网络名称，netmask

### netstat -r 查看 gateway

### sudo vim /etc/network/interfaces

添加如下：
auto eno2(本地网络名称)
iface eno2 inet static
address xxx.xxx.xxx.xxx (想要设置的ip)
gateway xxx.xxx.xxx.xxx (默认网关)
netmask xxx.xxx.xxx.xxx (掩码)
dns-nameserver 119.29.29.29

### 重启网络

sudo /etc/init.d/networking restart

### 配置frp

- frpc.ini 

```markdown
[common]
server_addr = 47.94.xx.xx
server_port = 7000
[ssh2]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6001
```
- frps.ini 

```markdown
[common]
bind_port = 7000
```

nohup ./frps -c frps.ini &

nohup ./frpc -c frpc.ini &

### apt 换源

### git

sudo apt install git

ssh-keygen -t rsa -C "xxx.com"

id_rsa.pub 粘贴进github

ssh -T git@github.com

配置Git配置文件

git config --global user.name "your name"

git config --global user.email "your email"

### docker

对照步骤:

https://bluesmilery.github.io/blogs/252e6902/

https://docs.docker.com/install/linux/docker-ce/ubuntu/

- 删除之前旧版本的docker

- 安装docker-ce

问题链接：

https://stackoverflow.com/questions/48056566/could-not-resolve-host-download-docker-com-while-installing-docker-ce

2. 添加权限

未完成

- 修改docker hub为国内镜像

- 转移数据目录

- Docker Compose

https://github.com/docker/compose/releases





