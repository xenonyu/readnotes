# BenchMark 测试记录
|model | epoch 1 | epoch 2 | epoch 4 | epoch 8 |
|:-:|:-:|:-:|:-:|:-:|
resnet50     | Avg time: 0.043<br> Acc@1: 16.18 <br> Acc@5: 36.40 | Avg time: 0.040<br> Acc@1: 25.28 <br> Acc@5: 50.04 | Avg time: 0.046<br> Acc@1: 37.28 <br> Acc@5: 63.72 | Avg time: 0.050<br> Acc@1: 40.45 <br> Acc@5: 68.20 |
resnet101    | Avg time: 0.062<br> Acc@1: 11.36 <br> Acc@5: 28.45 | Avg time: 0.066<br> Acc@1: 28.70 <br> Acc@5: 54.50 | Avg time: 0.066<br> Acc@1: 39.50 <br> Acc@5: 66.18 | Avg time: 0.068<br> Acc@1: 41.53 <br> Acc@5: 68.80 |
inceptionV2  | Avg time: 0.072<br> Acc@1: 19.82 <br> Acc@5: 42.90 | Avg time: 0.082<br> Acc@1: 28.83 <br> Acc@5: 54.35 | Avg time: 0.078<br> Acc@1: 37.82 <br> Acc@5: 63.58 | Avg time: 0.033<br> Acc@1: 36.76 <br> Acc@5: 64.07 |
inceptionV3  | Avg time: 0.055<br> Acc@1: 19.51 <br> Acc@5: 42.10 | Avg time: 0.164<br> Acc@1: 32.20 <br> Acc@5: 59.02 | Avg time: 0.064<br> Acc@1: 37.92 <br> Acc@5: 64.61 | Avg time: 0.130<br> Acc@1: 41.34 <br> Acc@5: 67.88 |

## 过程记录 (注意需要source pat_latest,以及不同epoch需要修改configs/example/下配置文件的max_epoch)
### 测试Resnet 50：
#### 命令：
```shell
sh runner/example/train.sh pat_dev 8 resnet50.benchmark
sh runner/example/train.sh pat_dailybuild 3 resnet50.benchmark
```
#### 出现Warn:

![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/BenchMarkIMG/warn.png)
#### epoch 1
#### epoch 2
#### epoch 4

### 测试Resnet 101:
#### 命令
```shell
sh runner/example/train.sh pat_dailybuild 3 resnet101.benchmark
sh runner/example/train.sh pat_dev 8 resnet101.benchmark
```

### 测试Inception V2

#### 命令
```shell
sh runner/example/train.sh pat_dailybuild 3 inception_v2.benchmark
sh runner/example/train.sh pat_dev 8 inception_v2.benchmark
```

### 测试Inception V3

#### 命令
```shell
sh runner/example/train.sh pat_dailybuild 3 inception_v3.benchmark
sh runner/example/train.sh pat_dev 8 inception_v3.benchmark
```
