# CNNL 算子开发流程

## 环境篇

1. vscode 环境配置流程参考:https://confluence.sensetime.com/pages/viewpage.action?pageId=216404471
2. 新建环境 

   1. source /nvme/camb.env
   2. conda create -n pytorch --clone base
   3. conda activate pytorch

3. 准备下载代码

   1. git clone git@gitlab.bj.sensetime.com:platform/ParrotsDL/senseparrots.git
   2. git checkout -b camb_concat

4. 编译

   1. 在根目录：sh scripts/ci_cambricon_script.sh mk_cambricon_mpion

   2. 如果编译失败，出现了tmp目录无权限访问，则更改编译脚本ci_cambricon_script.sh

      ```shell
      export NEUWARE_HOME=/usr/local/neuware
      #export TMPDIR=${HOME}/tmp
      source /nvme/camb.env
      ```
      ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/change_sh.png)
      
   3. 编译成功: ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/compile_success.png)
   4. 验证编译成功: senseparrots/python 目录下 python -c "import torch" ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/comple_success_2.png)
   
## 代码阅读篇
1. 以torch.add为例 找到torch.add的调用流程(不同算子调用流程不一样,要熟悉grep -nR 使用方式)
2. step1: senseparrots/python/parrots/__init__.py 中,找到: ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/flow1.png)
3. step2: 在binding/compute/function.hpp定义在binding/compute/function.cpp中实现了add op: ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/flow2.png)
4. step3: binding/compute/operator.hpp 重载了运算符:![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/flow3.png)
5. step4: binding/compute/operator.cpp 调用了addBinaryOp ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/flow4.png)
6. step5: binding/ir.cpp 中定义了调用了addBinaryOp ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/flow5.png)
7. step6: src/compute/src/darray/camb/binary.cpp 中实现了算子,但是性能不佳,我们要重载它,并注释掉这里的代码! ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/flow6.png)
8. 注释掉之后重新编译测试会发现无法调用该算子,可以开始实现了.![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/flow7.png)
## 开发流程
1. 以torch.add为例
2. 查阅pytorch官方文档,阅读torch.add特性 ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/work_torch_add.png)
3. 阅读cambricon 官方文档(找人要cambricon ftp登录方式,这里不方便列出),查阅kernel function 使用方式: ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/work_camb.png)
4. 在目录下添加文件:![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/work_catalog.png)
5. 更改src下:cmake文件 添加依赖:![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/work_change_cmake.png)
6. 根据camb文档编写add.cpp,注意代码所在namespace: ![](https://gitlab.sh.sensetime.com/xieyuming/imghost/raw/master/CodeNote/work_add_cpp.png)
7. 最后重新编译运行,python端测试查看效果, add部分pytest 代码见python/test_compute/test_darray_binary_op.py, 调用方式:
```shell
 pytest -vx test_compute/test_darray_binary_op.py
 ```
