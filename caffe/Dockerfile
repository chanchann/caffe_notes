FROM bvlc/caffe:gpu

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt-get clean \ 
    && apt-get update \
    && pip install -U pip \
    && pip install -U scipy \
    && pip install -U scikit-learn \
    && pip install -U matplotlib \
    && pip install -U jupyter \
    && pip install -U lmdb \
    && pip install -U python-mnist \

# Set the working directory to /caffe
WORKDIR /caffe



