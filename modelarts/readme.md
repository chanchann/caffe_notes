https://github.com/zalandoresearch/fashion-mnist/blob/master/README.zh-CN.md

NODE_OPTIONS=--max-http-header-size=16384 /Applications/Postman.app/Contents/MacOS/Postman

## 

https://github.com/huaweicloud/ModelArts-Lab/tree/master/docs/custom_image/custom_base


https://support.huaweicloud.com/usermanual-swr/swr_01_0011.html

swr.cn-north-4.myhuaweicloud.com/modelarts-job-dev-image/custom-gpu-cuda8-base:1.3

sudo docker tag test1:1.0 swr.cn-north-4.myhuaweicloud.com/modelarts-job-dev-image/custom-gpu-cuda8-base:1.3

sudo docker tag swr.cn-north-4.myhuaweicloud.com/modelarts-job-dev-image/custom-gpu-cuda8-base:1.3 swr.cn-north-4.myhuaweicloud.com/frankyi111/test:v1 

sudo docker tag mdarts:v1 swr.cn-north-4.myhuaweicloud.com/frankyi111/mdarts:v1 

sudo docker push swr.cn-north-4.myhuaweicloud.com/frankyi111/mdarts:v1 

sudo docker push swr.cn-north-4.myhuaweicloud.com/frankyi111/test:v1 

https://github.com/huaweicloud/ModelArts-Lab/blob/master/docs/custom_image/%E8%87%AA%E5%AE%9A%E4%B9%89%E9%95%9C%E5%83%8F%E8%AE%AD%E7%BB%83%E5%8A%9F%E8%83%BD%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97.md

## 

docker build  --no-cache --build-arg HTTP_PROXY=http://127.0.0.1:3128 -t elasticsearch-curator:5.4 .

https://support.huaweicloud.com/engineers-modelarts/modelarts_23_0088.html

https://support.huaweicloud.com/engineers-modelarts/modelarts_23_0088.html#modelarts_23_0088__li11403152725518



bash /home/work/run_train.sh python /home/work/user-job-dir/new/mnist_tf15/fashion_code/mnist_softmax.py --data_url /home/work/user-job-dir/mnist_tf15/fashion_data;


FROM swr.cn-north-1.myhuaweicloud.com/eiwizard/custom-cpu-base:1.2

ENV BUILD_PATH /root/work

RUN  pip --no-cache-dir install tensorflow==1.8.0 -i https://pypi.tuna.tsinghua.edu.cn/simple&& \
     echo success


     bash /home/work/run_train.sh python /home/work/user-job-dir/mnist/mnist_softmax.py --data_url /home/work/user-job-dir/mnist/data



