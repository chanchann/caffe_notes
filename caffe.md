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

/src/caffe/uitl/hdf5.cpp

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

