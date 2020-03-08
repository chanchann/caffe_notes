# install docker-ce

https://docs.docker.com/install/linux/docker-ce/ubuntu/

# 添加权限

sudo groupadd docker

sudo gpasswd -a ${USER} docker

sudo service docker restart

newgrp - docker

# 修改docker hub为国内镜像

##sudo vim /etc/docker/daemon.json
{
    "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
##systemctl restart docker.service

# docker pull

docker run -itd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -p 18888:22 -p 12345:12345 -v /home/ysy/frank:/mydata bvlc/caffe:cpu /bin/bash

docekr exec -it (id) /bin/bash

docker ps 查看id

# 坑

-p 开端口上官网的安全组设置

编译debug模式

rm -rf build

mkdir build && cd build 

修改CmakeList.txt

添加 SET(CMAKE_BUILD_TYPE "Debug")

cmake ..

make -j8

make install 



