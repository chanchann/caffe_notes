## Protobuffer 

```cpp
caffe::SolverParameter solver_param;
FileInputSteam* input = new FileInputStream(fd);
bool success = google::protobuf::TextFormat::Parse(input, &solver_param); 
```

## Boost

Caffe主要利用了Boost中的智能指针，自带引用计数功能，可避免共享指针时造成的内存泄漏或多次释放。

## GFLAGS

命令行参数解析作用

使用方法在tools/caffe.cpp

## GLOG

记录应用程序日志的使用库

tools/caffe.cpp

## BLAS

数学中的矩阵，向量计算

两个常用函数，include/caffe/util/math_functions.hpp

```cpp
template <typename Dtype>
void caffe_cpu_gemm(const CBLAS_TRANSPOSE TransA,
    const CBLAS_TRANSPOSE TransB, const int M, const int N, const int K,
    const Dtype alpha, const Dtype* A, const Dtype* B, const Dtype beta,
    Dtype* C);

// C = alpha * op(A) * op(B) + beta * C
```

```cpp
// CBLAS_TRANSPOSE是个枚举类型
// /usr/include
typedef enum {CblasNoTrans=111, CblasTrans=112, CblasConjTrans=113} CBLAS_TRANSPOSE;
```

M,N,K   -->  (M * K) X (K * N) --> M * N

```CPP
// 矩阵向量运算
// y = alpha * op(A) * x + beta * y
template <typename Dtype>
void caffe_cpu_gemv(const CBLAS_TRANSPOSE TransA, const int M, const int N,
    const Dtype alpha, const Dtype* A, const Dtype* x, const Dtype beta,
    Dtype* y);
```

## HDF5

高效存储和分发科学数据的新型数据格式

/src/caffe/util/hdf5.cpp

/include/caffe/util/hdf5.hpp

## opencv

## LMDB && LEVELDB

LMDB : 内存映射型数据库管理器，提供数据管理

key-value

LEVELDB caffe早期使用，考虑兼容

/include/caffe/util/db_lmdb.hpp

/include/caffe/util/db_leveldb.hpp

/src/caffe/uitl/db_lmdb.cpp

/src/caffe/uitl/db_leveldb.cpp

## Snappy 

用来压缩和解压缩的库

## 运行mnist识别

### 下载数据

cd data/mnist

./get_mnist.sh

### 转换格式

下载的二进制文件只有转化为LEVELDB or LMDB 才能被Caffe识别

./examples/mnist/create_mnist.sh
l.
生成

/caffe/examples/mnist/mnist_train_lmdb

/caffe/examples/mnist/mnist_test_lmdb

每个目录都有data.mdb and lock.mdb

### LeNet-5 模型

/examples/mnist/lenet_train_test.prototxt

### 训练超参数

example/mnist/train_lenet.sh

调用编译好的build/tools/caffe.bin 

--solver=examples/mnist/lenet_solver_rmsprop.prototxt

指定了训练超参数文件

学会看log

### 用训练好的模型预测

./build/tools/caffe test -model examples/mnist/lenet_train_test.prototxt -weights examples/mnist/lenet_iter_10000.caffemodel -iterations 100

./build/tools/caffe   : commands

flags:

train 

test 

device_query

time

Flags from tools/caffe.cpp

### 源码阅读

关注三个子目录: include/ , src/, tools/

先阅读src/caffe/proto/caffe.proto

1. 了解基本数据结构内存对象和磁盘文件的一一映射关系

2. 看头文件

3. 针对性看cpp和cu文件，一般根据新的需求派生新的类

4. 工具

### 激活函数

src/caffe/proto/caffe.proto

```cpp
message ReLUParameter {
    // leaky relu 参数
  optional float negative_slope = 1 [default = 0];
  enum Engine {   // 计算引擎选择
    DEFAULT = 0;  
    CAFFE = 1;   // caffe实现
    CUDNN = 2;   // CUDNN实现
  }
  optional Engine engine = 2 [default = DEFAULT];
}

message SigmoidParameter {
  enum Engine {
    DEFAULT = 0;
    CAFFE = 1;
    CUDNN = 2;
  }
  optional Engine engine = 1 [default = DEFAULT];
}

message TanHParameter {
  enum Engine {
    DEFAULT = 0;
    CAFFE = 1;
    CUDNN = 2;
  }
  optional Engine engine = 1 [default = DEFAULT];
}
```

include/caffe/layers/neuron_layer.hpp 

非线性层的鼻祖NeuronLayer，派生于Layer类, 特点是输出blob(y)和输入blob(x)尺寸相同


### 复习虚函数 && 纯虚函数

https://www.zhihu.com/question/23971699

virtual void funtion1()=0; 纯虚函数一定没有定义 ， 错

多数情况下不给定义，但其实我们可以给纯虚函数提供定义。不过函数体必须定义在类的外部，也就是说，我们不能在类的内部为一个=0的函数提供函数体  p541 cpp primer 5th

## c++ explicit

https://www.cnblogs.com/this-543273659/archive/2011/08/02/2124596.html

## c++ public/protected/private

保护成员变量或函数与私有成员十分相似，但有一点不同，保护成员在派生类（即子类）中是可访问的。

## rely layer 

include/caffe/layers/relu_layer.hpp 

同理学习sigmoid, tanh

## relu实现

/src/caffe/layers/relu_layer.cpp

```cpp
//反向传播关键点
for (int i = 0; i < count; ++i) {
    //根据链式法则，后一层的误差乘以导函数得到前一层的误差
    bottom_diff[i] = top_diff[i] * ((bottom_data[i] > 0)
        + negative_slope * (bottom_data[i] <= 0));
```

同理学习sigmoid/tanh

```cpp
//sigmoid 
for (int i = 0; i < count; ++i) {
    const Dtype sigmoid_x = top_data[i];
    bottom_diff[i] = top_diff[i] * sigmoid_x * (1. - sigmoid_x);
}
```

```cpp
for (int i = 0; i < count; ++i) {
    tanhx = top_data[i];
    bottom_diff[i] = top_diff[i] * (1 - tanhx * tanhx);
}
```

### 查定位宏命令

grep -nHR "STUB_GPU"

-n 显示行号

-H 显示文件名

-R 递归查找子目录

### 梳理layer

https://blog.csdn.net/langb2014/article/details/50988275

## caffe的数据结构

### Caffe数据结构

### Blob

四维数组用于存储和交换数据(num, channels, height, width)

用于存储数据或权值(data) , 权值增益（diff)

```cpp
//using namespace caffe;
Blob<float> a;
cout << "Size:" << a.shape_string() << endl;
a.Reshape(1, 2, 3, 4);
cout << "Size:" << a.shape_string() << endl;
```

创建Blob后，可通过 mutable_cpu[gpu]_data[diff]修改内部值

```cpp
float* p  = a.mutable_cpu_data();
for(int i = 0; i< a.count(), i++){
    p[i] = i;
}
for(int u = 0; u < a.num(), u++){
    for(int v = 0; v < a.channels(); v++){
        for(int w = 0; w < a.height(); w++){
            for(int x = 0; x < a.width(); x++){
                cout << a.data_at(u, v, w, x) << endl;
            }
        }
    }
}

```

Blob能够自动同步CPU/GPU数据

支持计算L1,L2范数

```cpp
cout << "L1: " << a.asum_data() << endl;
cout << "L2: " << a.sumsq_data() << endl;
```

```cpp
float* p = a.mutable_cpu_data();
float* q = a.mutable_cpu_diff();
for(int i = 0; i < a.count(); i++){
    p[i] = i;
    q[i] = a.count() - 1 - i;
}
a.Update();  //执行Update操作，将diff和data融合
             //这也是CNN权值更新步骤的最终实施者
             // Update实现了data = data - diff，在权值更新时深入研究
```

```cpp
//将Blob内部值保存到磁盘，或者从磁盘载入内存，
//可以分别通过ToProto(), FromProto()
//#include<caffe/util/io.hpp>
BlobProto bp; // 构造BlobProto对象
a.toProto(&bp, true); //将a序列化，连同diff(默认不带)
WriteProtoToBinaryFile(bp, "a.blob"); //写入磁盘文件"a.blob"
BlobProto bp2;  //构造一个新的BlobProto对象
ReadProtoFromBinaryFileOrDie("a.blob", &bp2); //读取磁盘文件
Blob<float> b;  // 新建一个Blob对象
b.FromProto(bp2, true); //从序列化对象bp2中克隆b(连通形状)

/*
BlobProto对象实现了磁盘，内存间数据通信，对于保存，载入训练好的模型weight
*/
```

### 数据结构描述

src/caffe/proto/caffe.proto  5:29

思考：为什么不直接声明BlobShape, BlobProto为结构体，而要用ProtoBuffer这种格式

1. 结构体的序列化和反序列化需要额外的编程操作，难以做到接口标准化

2. 结构体包含变长数据(一般用指向某个内存地址的指针),需要更加细致的工作保证数据完整

### Blob

/include/caffe/blob.hpp,封装了SyncedMemory类，作为基本计算单元服务Layer,Net,Solver

/src/caffe/blob.cpp

### shared_ptr 

### SyncedMemory

/include/caffe/syncedmem.hpp

### 条件编译

https://blog.csdn.net/fanyun_01/article/details/84584063

### INSTANTIATE_CLASS ???

https://www.cnblogs.com/neopenx/p/5187586.html


## Layer

### 数据结构描述

caffe.proto

message LayerParameter{

}

/include/caffe/layer.hpp

/src/caffe/layer.cpp


## Net

Net是一张图纸，对应的描述文件为*.prototxt

选择自带CaffeNet模型 models/bvlc_reference_caffenet/deploy.prototxt

```cpp
//net_demo.cpp
#include <vector>
#include <iostream>
#include <caffe/net.hpp>
using namespace std;
using namespace caffe;

int main(){
  std::string proto("deploy.prototxt");
  Net<float> nn(proto, caffe::TEST);
  vector<string> bn = nn.blob_names();  //获取Net中所有Blob对象名
  for(int i = 0; i < bn.size(); i++){
    cout << "Blob #" << i << ":" << bn[i] << endl;
  }
  return 0;
}
```

### 数据结构描述

还是从caffe.proto看起

message NetParameter

include/caffe/net.hpp

Blob提供了数据容器的机制，而Layer通过不用的策略使用该容器数据，实现多元化的计算处理过程，又提供了深度学习的基本算法。

Thinking:

1. Net初始化如何统计所需的存储空间？

net.cpp的init()里：

memory_used_ += top_vecs_[layer_id][top_id]->count();

2. cpp中如何禁用某个类的拷贝构造函数和赋值运算符重载？

Caffe 代码中定义了宏 DISABLE_COPY_AND_ASSIGN，利用了 C++ 语言特性，即只要将类拷贝构造函数与赋值运算符重载函数声明为私有就能禁用这两个函数。

该宏定义位于 include/caffe/common.hpp 、

```cpp
#define DISABLE_COPY_AND_ASSIGN(classname) \
private:\
  classname(const classname&);\
  classname& operator=(const classname&)
```

## IO模块

### 数据读取层

Caffe数据读取层(DataLayer)是Layer的派生类。除了读取LMDB，LEVELDB之外，也可以直接从原始图像直接读取(ImageDataLayer)

### 数据结构描述

caffe.proto:

message DataParameter

include/caffe/layers/base_data_layer.hpp

src/caffe/layers/base_data_layer.cpp

## 复习cpp多继承

http://c.biancheng.net/view/2277.html

## 数据变换器

caffe数据变换器(DataTransformer)主要提供了对原始输入图像的预处理方法

还是先看数据结构描述

message TransformationParameter

include/caffe/data_transformer.hpp

src/caffe/data_transformer.cpp

Datum用来从LMDB/LEVELDB中读取数据，或将数据写入，和BlobProto有相似功能，只是BlobProto用于模型权值序列化/反序列化，而Datum专为数据或特征图

## Caffe模型

模型又三部分组成:可学习参数，结构参数，训练超参数

可学习参数在内存中使用Blob保存，必要时以二进制ProtoBuffer文件(*.caffemodel)存磁盘

结构参数ProtoBuffer(*.prototxt),

训练超参数ProtoBuffer(*.prototxt)

### 磁盘上的表示

.solverstate and .caffemodel

solver.cpp

string Solver<Dtype>::SnapshotToBinaryProto()

sgd_solver.cpp

void SGDSolver<Dtype>::SnapshotSolverStateToBinaryProto()

### 前向、后向运算

损失函数 caffe.proto找到Softmax消息定义

include/caffe/loss_layers.hpp

### caffe最优化求解过程

message SolverParameter

### launch.json

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        
        {
            "name" : "(gdb) Launch",
            "type" : "cppdbg",
            "request" : "launch",
            "program": "${workspaceFolder}/build/tools/caffe-d",
            "args": ["train", "--solver", "${workspaceFolder}/examples/mnist/lenet_solver.prototxt"],
            "stopAtEntry" : false,
            "cwd" : "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "/usr/bin/gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true,
                }
            ],
        }
    ]
}
```