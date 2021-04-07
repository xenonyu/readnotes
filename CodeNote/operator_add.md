# CNNL 算子开发流程

## 环境篇

1. 新建环境 

   1. source /nvme/camb.env
   2. conda create -n pytorch --clone base
   3. conda activate pytorch

2. 准备下载代码

   1. git clone git@gitlab.bj.sensetime.com:platform/ParrotsDL/senseparrots.git
   2. git checkout -b camb_concat

3. 编译

   1. 在根目录：sh scripts/ci_cambricon_script.sh mk_cambricon_mpion

   2. 如果编译失败，出现了tmp目录无权限访问，则更改编译脚本ci_cambricon_script.sh

      ```shell
      export NEUWARE_HOME=/usr/local/neuware
      #export TMPDIR=${HOME}/tmp
      source /nvme/camb.env
      ```
      
   3. 编译成功: ![]()
   
      
   
4. 

