FROM bvlc/caffe:gpu

COPY . .
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && mv sources.list /etc/apt/ && apt-get update -y  && apt-get clean 
# Set the working directory to /caffe
WORKDIR /caffe



