FROM bvlc/caffe:gpu
RUN pip install -U pip \
    && pip install -U scipy \
    && pip install -U scikit-learn \
    && pip install -U matplotlib \
    && pip install -U jupyter \
    && pip install -U lmdb \
    && pip install -U python-mnist \
    && sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list && rm -Rf /var/lib/apt/lists/* && apt-get update

# Set the working directory to /caffe
WORKDIR /caffe



