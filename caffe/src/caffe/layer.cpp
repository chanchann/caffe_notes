#include "caffe/layer.hpp"
//啥也没实现，只有虚函数，真正的实现都在派生类中
//具体阅读/src/caffe/layers/*.cpp

namespace caffe {

INSTANTIATE_CLASS(Layer);

}  // namespace caffe
