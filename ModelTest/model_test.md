# BenchMark 测试记录
|model | epoch 1 | epoch 2 | epoch 4 | epoch 8 |
|:-:|:-:|:-:|:-:|:-:|
resnet50     | Avg time: 2.278<br> Acc@1: 15.23 <br> Acc@5: 31.25 | Avg time: 2.727<br> Acc@1: 31.26 <br> Acc@5: 56.20 | Avg time: 2.322<br> Acc@1: 40.62 <br> Acc@5: 71.88 | Avg time: 0.122<br> Acc@1: 15.23 <br> Acc@5: 31.25 |
resnet101    | Avg time: 2.576<br> Acc@1: 12.50 <br> Acc@5: 15.62 | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 |
inceptionV2  | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 |
inceptionV3  | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 | Avg time: 0.000<br> Acc@1: 0.000 <br> Acc@5: 0.000 |

## 过程记录
### 测试Resnet 50：
#### 命令：
```shell
sh runner/example/train.sh pat_dev 8 resnet50.benchmark
```
#### 出现Warn:

![avatar](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/BenchMarkIMG/warn.png)
#### epoch 1
#### epoch 2
#### epoch 4

### 测试Resnet 101:
#### 命令
```shell
sh runner/example/train.sh pat_dev 8 resnet101.benchmark
```
