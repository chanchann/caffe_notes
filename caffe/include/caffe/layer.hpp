#ifndef CAFFE_LAYER_H_
#define CAFFE_LAYER_H_

#include <algorithm>
#include <string>
#include <vector>

#include "caffe/blob.hpp"
#include "caffe/common.hpp"
#include "caffe/layer_factory.hpp"
#include "caffe/proto/caffe.pb.h"
#include "caffe/util/math_functions.hpp"

/**
 Forward declare boost::thread instead of including boost/thread.hpp
 to avoid a boost/NVCC issues (#1009, #1010) on OSX.
 */
namespace boost { class mutex; }

namespace caffe {

/**
 * @brief An interface for the units of computation which can be composed into a
 *        Net.
 *
 * Layer%s must implement a Forward function, in which they take their input
 * (bottom) Blob%s (if any) and compute their output Blob%s (if any).
 * They may also implement a Backward function, in which they compute the error
 * gradients with respect to their input Blob%s, given the error gradients with
 * their output Blob%s.
 */
template <typename Dtype>
class Layer {
 public:
  /**
   * You should not implement your own constructor. Any set up code should go
   * to SetUp(), where the dimensions of the bottom blobs are provided to the
   * layer.
   */
  // 显式构造函数，从LayerParameter对象加载配置
  explicit Layer(const LayerParameter& param)
    : layer_param_(param) {
      // Set phase and copy blobs (if there are any).
      phase_ = param.phase(); //设置当前阶段(训练/预测)
      if (layer_param_.blobs_size() > 0) {
        //按layer_param_设置本身Blob对象个数
        blobs_.resize(layer_param_.blobs_size());
        //并以此将每个Blob对象尺寸调整为layer_param_中的Blob尺寸一致
        for (int i = 0; i < layer_param_.blobs_size(); ++i) {
          blobs_[i].reset(new Blob<Dtype>());
          blobs_[i]->FromProto(layer_param_.blobs(i));
        }
      }
    }
  virtual ~Layer() {}

  /**
   * @brief Implements common layer setup functionality.
   *
   * @param bottom the preshaped input blobs
   * @param top
   *     the allocated but unshaped output blobs, to be shaped by Reshape
   *
   * Checks that the number of bottom and top blobs is correct.
   * Calls LayerSetUp to do special layer setup for individual layer types,
   * followed by Reshape to set up sizes of top blobs and internal buffers.
   * Sets up the loss weight multiplier blobs for any non-zero loss weights.
   * This method may not be overridden.
   */
  //配置函数，实现常用层配置接口，不可被覆盖
  void SetUp(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
    CheckBlobCounts(bottom, top); // 检查Blob
    LayerSetUp(bottom, top); // 与层类型相关的配置过程
    Reshape(bottom, top);  // 对Top Blob变形
    SetLossWeights(top);  // 设置损失权值因子Blob
  }

  /**
   * @brief Does layer-specific setup: your layer should implement this function
   *        as well as Reshape.
   *
   * @param bottom
   *     the preshaped input blobs, whose data fields store the input data for
   *     this layer
   * @param top
   *     the allocated but unshaped output blobs
   *
   * This method should do one-time layer specific setup. This includes reading
   * and processing relevent parameters from the <code>layer_param_</code>.
   * Setting up the shapes of top blobs and internal buffers should be done in
   * <code>Reshape</code>, which will be called before the forward pass to
   * adjust the top blob sizes.
   */
  //层配置虚函数，做特定类型层相关的配置，由该类型层自己实现
  virtual void LayerSetUp(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {}

  /**
   * @brief Adjust the shapes of top blobs and internal buffers to accommodate
   *        the shapes of the bottom blobs.
   *
   * @param bottom the input blobs, with the requested input shapes
   * @param top the top blobs, which should be reshaped as needed
   *
   * This method should reshape top blobs as needed according to the shapes
   * of the bottom (input) blobs, as well as reshaping any internal buffers
   * and making any other necessary adjustments so that the layer can
   * accommodate the bottom blobs.
   */
  //变形(纯虚)函数，修改Top Blob以及内部Blob缓冲区的形状
  virtual void Reshape(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) = 0;

  /**
   * @brief Given the bottom blobs, compute the top blobs and the loss.
   *
   * @param bottom
   *     the input blobs, whose data fields store the input data for this layer
   * @param top
   *     the preshaped output blobs, whose data fields will store this layers'
   *     outputs
   * \return The total loss from the layer.
   *
   * The Forward wrapper calls the relevant device wrapper function
   * (Forward_cpu or Forward_gpu) to compute the top blob values given the
   * bottom blobs.  If the layer has any non-zero loss_weights, the wrapper
   * then computes and returns the loss.
   *
   * Your layer should implement Forward_cpu and (optionally) Forward_gpu.
   */
  //前向传播函数，给定Bottom Blob，计算Top Blob和loss，返回值为当前层loss
  //该函数会调用相应设备包装函数，如Forward_cpu或Forward_gpu来实现真正的计算过程
  //如果该层有任意非0 loss_weights参数，那么包装函数会计算并返回loss
  //派生类应该实现Forwad_cpu / Forward_gpu(可选)
  inline Dtype Forward(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top);

  /**
   * @brief Given the top blob error gradients, compute the bottom blob error
   *        gradients.
   *
   * @param top
   *     the output blobs, whose diff fields store the gradient of the error
   *     with respect to themselves
   * @param propagate_down
   *     a vector with equal length to bottom, with each index indicating
   *     whether to propagate the error gradients down to the bottom blob at
   *     the corresponding index
   * @param bottom
   *     the input blobs, whose diff fields will store the gradient of the error
   *     with respect to themselves after Backward is run
   *
   * The Backward wrapper calls the relevant device wrapper function
   * (Backward_cpu or Backward_gpu) to compute the bottom blob diffs given the
   * top blob diffs.
   *
   * Your layer should implement Backward_cpu and (optionally) Backward_gpu.
   */
  // 反向传播函数，给定Top Blob误差梯度，计算Bottom Blob误差梯度
  // top 其diff域来自上一层的误差梯度
  // propagate_down,多路开关，与Bottom矢量维度相同，每个值表示是否将误差梯度传递到对应Bottom
  // bottom ,其diff域需要由该函数计算得到。
  // 该函数会调用相应设备包装函数，如Backward_cpu,Backward_gpu来实现真正的计算过程,派生类负责实现
  inline void Backward(const vector<Blob<Dtype>*>& top,
      const vector<bool>& propagate_down,
      const vector<Blob<Dtype>*>& bottom);

  /**
   * @brief Returns the vector of learnable parameter blobs.
   */
  // 返回Layer内部可训练的权值，偏置项Blob向量
  vector<shared_ptr<Blob<Dtype> > >& blobs() {
    return blobs_;
  }

  /**
   * @brief Returns the layer parameter.
   */
  // 返回Layer初始化参数(ProtoBuffer提供)
  const LayerParameter& layer_param() const { return layer_param_; }

  /**
   * @brief Writes the layer parameter to a protocol buffer
   */
  // Layer初始化参数写入ProtoBuffer缓冲区
  virtual void ToProto(LayerParameter* param, bool write_diff = false);

  /**
   * @brief Returns the scalar loss associated with a top blob at a given index.
   */
  // 返回与某个Top Blob相关的表标量loss值
  inline Dtype loss(const int top_index) const {
    return (loss_.size() > top_index) ? loss_[top_index] : Dtype(0);
  }

  /**
   * @brief Sets the loss associated with a top blob at a given index.
   */
  // 设置与某个Top Blob相关的表标量loss值
  inline void set_loss(const int top_index, const Dtype value) {
    if (loss_.size() <= top_index) {
      loss_.resize(top_index + 1, Dtype(0));
    }
    loss_[top_index] = value;
  }

  /**
   * @brief Returns the layer type.
   */
  // 返回层类型字符串，便于识别，由派生类负责实现
  virtual inline const char* type() const { return ""; }

  /**
   * @brief Returns the exact number of bottom blobs required by the layer,
   *        or -1 if no exact number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some exact number of bottom blobs.
   */
  // 返回该Layer需要输入的Blob数目，-1表示不关心，由派生类实现
  virtual inline int ExactNumBottomBlobs() const { return -1; }
  /**
   * @brief Returns the minimum number of bottom blobs required by the layer,
   *        or -1 if no minimum number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some minimum number of bottom blobs.
   */
  virtual inline int MinBottomBlobs() const { return -1; }
  /**
   * @brief Returns the maximum number of bottom blobs required by the layer,
   *        or -1 if no maximum number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some maximum number of bottom blobs.
   */
  virtual inline int MaxBottomBlobs() const { return -1; }
  /**
   * @brief Returns the exact number of top blobs required by the layer,
   *        or -1 if no exact number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some exact number of top blobs.
   */
  // 返回该Layer需要输出的Blob数目，-1表示不关心，由派生类实现
  virtual inline int ExactNumTopBlobs() const { return -1; }
  /**
   * @brief Returns the minimum number of top blobs required by the layer,
   *        or -1 if no minimum number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some minimum number of top blobs.
   */
  virtual inline int MinTopBlobs() const { return -1; }
  /**
   * @brief Returns the maximum number of top blobs required by the layer,
   *        or -1 if no maximum number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some maximum number of top blobs.
   */
  virtual inline int MaxTopBlobs() const { return -1; }
  /**
   * @brief Returns true if the layer requires an equal number of bottom and
   *        top blobs.
   *
   * This method should be overridden to return true if your layer expects an
   * equal number of bottom and top blobs.
   */
  // 返回该Layer是否有相同的输入/输出Blob，由派生类负责实现
  virtual inline bool EqualNumBottomTopBlobs() const { return false; }

  /**
   * @brief Return whether "anonymous" top blobs are created automatically
   *        by the layer.
   *
   * If this method returns true, Net::Init will create enough "anonymous" top
   * blobs to fulfill the requirement specified by ExactNumTopBlobs() or
   * MinTopBlobs().
   */
  //返回是否允许匿名Top Blob，由该层Layer自动创建
  //若为真，在Net::init()函数中创建足够多的匿名Top Blob
  //来满足该Layer ExactNumTopBlobs(),MinTopBlobs()需求
  virtual inline bool AutoTopBlobs() const { return false; }

  /**
   * @brief Return whether to allow force_backward for a given bottom blob
   *        index.
   *
   * If AllowForceBackward(i) == false, we will ignore the force_backward
   * setting and backpropagate to blob i only if it needs gradient information
   * (as is done when force_backward == false).
   */
  //返回某些Bottom Blob是否允许强制反向传播
  //如果AllowForcebackward(i) == false，将会忽略force_backward设定
  virtual inline bool AllowForceBackward(const int bottom_index) const {
    return true;
  }

  /**
   * @brief Specifies whether the layer should compute gradients w.r.t. a
   *        parameter at a particular index given by param_id.
   *
   * You can safely ignore false values and always compute gradients
   * for all parameters, but possibly with wasteful computation.
   */
  //指定该Layer是否计算相对权值或bias的梯度
  //具体相对谁由param_id定
  inline bool param_propagate_down(const int param_id) {
    return (param_propagate_down_.size() > param_id) ?
        param_propagate_down_[param_id] : false;
  }
  /**
   * @brief Sets whether the layer should compute gradients w.r.t. a
   *        parameter at a particular index given by param_id.
   */
  // 设置该Layer是否计算相对权值或bias的梯度
  inline void set_param_propagate_down(const int param_id, const bool value) {
    if (param_propagate_down_.size() <= param_id) {
      param_propagate_down_.resize(param_id + 1, true);
    }
    param_propagate_down_[param_id] = value;
  }


 protected:
  /** The protobuf that stores the layer parameters */
  LayerParameter layer_param_; // 保存layer参数的Protobuffer对象
  /** The phase: TRAIN or TEST */
  Phase phase_;  //Layer当前所处阶段，可选TRAIN或TEST
  /** The vector that stores the learnable parameters as a set of blobs. */
  vector<shared_ptr<Blob<Dtype> > > blobs_;  // layer内部权值或偏置项，以Blob形式组织
  /** Vector indicating whether to compute the diff of each param blob. */
  vector<bool> param_propagate_down_; //标志位，是否计算对应参数的误差梯度

  /** The vector that indicates whether each top blob has a non-zero weight in
   *  the objective function. */
  vector<Dtype> loss_; // 标志位，在目标函数中，是否每个Top Blob都有非零权重

  /** @brief Using the CPU device, compute the layer output. */
  virtual void Forward_cpu(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) = 0;
  /**
   * @brief Using the GPU device, compute the layer output.
   *        Fall back to Forward_cpu() if unavailable.
   */
  virtual void Forward_gpu(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
    // LOG(WARNING) << "Using CPU code as backup.";
    return Forward_cpu(bottom, top);
  }

  /**
   * @brief Using the CPU device, compute the gradients for any parameters and
   *        for the bottom blobs if propagate_down is true.
   */
  virtual void Backward_cpu(const vector<Blob<Dtype>*>& top,
      const vector<bool>& propagate_down,
      const vector<Blob<Dtype>*>& bottom) = 0;
  /**
   * @brief Using the GPU device, compute the gradients for any parameters and
   *        for the bottom blobs if propagate_down is true.
   *        Fall back to Backward_cpu() if unavailable.
   */
  virtual void Backward_gpu(const vector<Blob<Dtype>*>& top,
      const vector<bool>& propagate_down,
      const vector<Blob<Dtype>*>& bottom) {
    // LOG(WARNING) << "Using CPU code as backup.";
    Backward_cpu(top, propagate_down, bottom);
  }

  /**
   * Called by the parent Layer's SetUp to check that the number of bottom
   * and top Blobs provided as input match the expected numbers specified by
   * the {ExactNum,Min,Max}{Bottom,Top}Blobs() functions.
   */
  // 校验输入/输出Blob数目是否满足layer需求
  virtual void CheckBlobCounts(const vector<Blob<Dtype>*>& bottom,
                               const vector<Blob<Dtype>*>& top) {
    if (ExactNumBottomBlobs() >= 0) {
      CHECK_EQ(ExactNumBottomBlobs(), bottom.size())
          << type() << " Layer takes " << ExactNumBottomBlobs()
          << " bottom blob(s) as input.";
    }
    if (MinBottomBlobs() >= 0) {
      CHECK_LE(MinBottomBlobs(), bottom.size())
          << type() << " Layer takes at least " << MinBottomBlobs()
          << " bottom blob(s) as input.";
    }
    if (MaxBottomBlobs() >= 0) {
      CHECK_GE(MaxBottomBlobs(), bottom.size())
          << type() << " Layer takes at most " << MaxBottomBlobs()
          << " bottom blob(s) as input.";
    }
    if (ExactNumTopBlobs() >= 0) {
      CHECK_EQ(ExactNumTopBlobs(), top.size())
          << type() << " Layer produces " << ExactNumTopBlobs()
          << " top blob(s) as output.";
    }
    if (MinTopBlobs() >= 0) {
      CHECK_LE(MinTopBlobs(), top.size())
          << type() << " Layer produces at least " << MinTopBlobs()
          << " top blob(s) as output.";
    }
    if (MaxTopBlobs() >= 0) {
      CHECK_GE(MaxTopBlobs(), top.size())
          << type() << " Layer produces at most " << MaxTopBlobs()
          << " top blob(s) as output.";
    }
    if (EqualNumBottomTopBlobs()) {
      CHECK_EQ(bottom.size(), top.size())
          << type() << " Layer produces one top blob as output for each "
          << "bottom blob input.";
    }
  }

  /**
   * Called by SetUp to initialize the weights associated with any top blobs in
   * the loss function. Store non-zero loss weights in the diff blob.
   */
  //该函数在Layer的SetUp函数中被调用，主要目的是初始化与Top Blob相关的loss权重
  //放到Top Blob的diff域，实际由Forward计算loss
  //loss_weight == 0,表示当前层不参与loss函数计算，大部分Layer属于这一类
  //loss_weight == 1,表示当前层参与loss函数计算，损失层(LossLayer)属于这一类
  inline void SetLossWeights(const vector<Blob<Dtype>*>& top) {
    //从Protobuffer对象中获得layer参数(loss_weight_sizes)
    const int num_loss_weights = layer_param_.loss_weight_size();
    if (num_loss_weights) {
      //loss_weight参数个数应当与Top Blob数目相同，或者不要loss weight参数
      CHECK_EQ(top.size(), num_loss_weights) << "loss_weight must be "
          "unspecified or specified once per top blob.";
      //遍历每个Top Blob
      for (int top_id = 0; top_id < top.size(); ++top_id) {
        //从Protobuffer对象中拿到loss_weight实际值(0 or 1)
        const Dtype loss_weight = layer_param_.loss_weight(top_id);
        //如果为0则跳过
        if (loss_weight == Dtype(0)) { continue; }
        //如果为1则对网络做相关设置
        this->set_loss(top_id, loss_weight); //本地记录loss_weight值
        const int count = top[top_id]->count();
        Dtype* loss_multiplier = top[top_id]->mutable_cpu_diff();
        //将loss_weight值写入Top Blob的diff域，传递到其他需要使用的地方，实现远程同步
        caffe_set(count, loss_weight, loss_multiplier);
      }
    }
  }

 private:
  DISABLE_COPY_AND_ASSIGN(Layer); //禁用拷贝构造函数和赋值运算函数
};  // class Layer

// Forward and backward wrappers. You should implement the cpu and
// gpu specific implementations instead, and should not change these
// functions.
//forward/backward函数包装，不需要修改这两个函数
//派生的时候只需要改写foward[backward]_cpu[gpu]
template <typename Dtype>
inline Dtype Layer<Dtype>::Forward(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  Dtype loss = 0;
  Reshape(bottom, top);
  switch (Caffe::mode()) {
  case Caffe::CPU:
    Forward_cpu(bottom, top);
    for (int top_id = 0; top_id < top.size(); ++top_id) {
      if (!this->loss(top_id)) { continue; }
      const int count = top[top_id]->count(); 
      //若为LossLayer,则已经通过Forward函数计算出全局损失函数，放在Top Blob data域
      const Dtype* data = top[top_id]->cpu_data();
      //若loss_weight不为0，则已经在SetLossWeight函数中将loss权重放在Top Blob diff域
      const Dtype* loss_weights = top[top_id]->cpu_diff();
      //计算加权之后的loss
      loss += caffe_cpu_dot(count, data, loss_weights);
    }
    break;
  case Caffe::GPU:
    Forward_gpu(bottom, top);
#ifndef CPU_ONLY
    for (int top_id = 0; top_id < top.size(); ++top_id) {
      if (!this->loss(top_id)) { continue; }
      const int count = top[top_id]->count();
      const Dtype* data = top[top_id]->gpu_data();
      const Dtype* loss_weights = top[top_id]->gpu_diff();
      Dtype blob_loss = 0;
      caffe_gpu_dot(count, data, loss_weights, &blob_loss);
      loss += blob_loss;
    }
#endif
    break;
  default:
    LOG(FATAL) << "Unknown caffe mode.";
  }
  return loss;
}

template <typename Dtype>
inline void Layer<Dtype>::Backward(const vector<Blob<Dtype>*>& top,
    const vector<bool>& propagate_down,
    const vector<Blob<Dtype>*>& bottom) {
  switch (Caffe::mode()) {
  case Caffe::CPU:
    Backward_cpu(top, propagate_down, bottom);
    break;
  case Caffe::GPU:
    Backward_gpu(top, propagate_down, bottom);
    break;
  default:
    LOG(FATAL) << "Unknown caffe mode.";
  }
}

// Serialize LayerParameter to protocol buffer
//将层配置参数序列化为ProtoBuffer
template <typename Dtype>
void Layer<Dtype>::ToProto(LayerParameter* param, bool write_diff) {
  param->Clear();
  param->CopyFrom(layer_param_);
  param->clear_blobs();
  for (int i = 0; i < blobs_.size(); ++i) {
    blobs_[i]->ToProto(param->add_blobs(), write_diff);
  }
}

}  // namespace caffe

#endif  // CAFFE_LAYER_H_
