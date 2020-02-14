#include <algorithm>
#include <vector>

#include "caffe/layers/relu_layer.hpp"

namespace caffe {

template <typename Dtype>
void ReLULayer<Dtype>::Forward_cpu(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  //(只读)获得输入blob的data指针
  const Dtype* bottom_data = bottom[0]->cpu_data();
  //(读写)获得输出blob的data指针
  Dtype* top_data = top[0]->mutable_cpu_data();
  //获得输入blob的个数
  const int count = bottom[0]->count();
  //leaky_relu的参数，从layer_param_获得，默认为0(普通relu)
  Dtype negative_slope = this->layer_param_.relu_param().negative_slope();
  for (int i = 0; i < count; ++i) {
    top_data[i] = std::max(bottom_data[i], Dtype(0))
        + negative_slope * std::min(bottom_data[i], Dtype(0));
  }
}

template <typename Dtype>
void ReLULayer<Dtype>::Backward_cpu(const vector<Blob<Dtype>*>& top,
    const vector<bool>& propagate_down,
    const vector<Blob<Dtype>*>& bottom) {
  //如果需要做反向传播计算
  if (propagate_down[0]) {
    //(只读)获得前一层的data指针  
    const Dtype* bottom_data = bottom[0]->cpu_data();
    //(只读)获得后一层的diff指针
    const Dtype* top_diff = top[0]->cpu_diff();
    //(读写)获得前一层的diff指针
    Dtype* bottom_diff = bottom[0]->mutable_cpu_diff();
    //获得参与计算的元素总数
    const int count = bottom[0]->count();
    Dtype negative_slope = this->layer_param_.relu_param().negative_slope();
    for (int i = 0; i < count; ++i) {
      //根据链式法则，后一层的误差乘以导函数得到前一层的误差
      bottom_diff[i] = top_diff[i] * ((bottom_data[i] > 0)
          + negative_slope * (bottom_data[i] <= 0));
    }
  }
}


#ifdef CPU_ONLY
STUB_GPU(ReLULayer);
#endif

INSTANTIATE_CLASS(ReLULayer);

}  // namespace caffe
