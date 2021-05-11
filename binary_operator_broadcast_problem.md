camb_pytorch运行结果:

![image-20210421114328223](../../../../Library/Application Support/typora-user-images/image-20210421114328223.png

```shell
>>> import torch_mlu.core.mlu_model as ct
CNML: 7.9.2 1a1e33b
CNRT: 4.10.0 af3d5e7
>>> import torch
>>> cuda_a = torch.randn(3, 2, 1).to(ct.mlu_device())
>>> cuda_b = torch.randn(2, 5).to(ct.mlu_device())
>>> torch.add(cuda_a, cuda_b)
2021-04-21 11:42:31.830927: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.831007: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
2021-04-21 11:42:31.857678: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.857730: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
2021-04-21 11:42:31.871900: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.871951: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
2021-04-21 11:42:31.887486: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.887535: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
2021-04-21 11:42:31.903459: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.903508: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
2021-04-21 11:42:31.918723: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.918757: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
2021-04-21 11:42:31.942358: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.942390: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
2021-04-21 11:42:31.944089: [cnmlError] MLU::dyadic_all dimension mismatch,output shape is wrong, the given shape is:(n=1, c=30,h=1,w=1, d=0, t=0, data in array:{1, 1, 1, 30, } , but the expected shape is:(n=30, c=1,h=1,w=1, d=0, t=0, data in array:{30, 1, 1, 1, }
2021-04-21 11:42:31.946056: [cnmlError] MLU::dyadic_all Op update tensor shape failed
[ERROR][/home/jiangyongjiu1/utils/v1.0.0rc1/cambricon_pytorch/pytorch/src/catch/torch_mlu/csrc/aten/operators/cnml/internal/eq_internal.cpp][line: 35][cnml_eq_internal][thread:140007329646400][process:66132]:
CNML error: CNML_STATUS_INVALIDPARAM
[WARNING][/home/jiangyongjiu1/utils/v1.0.0rc1/cambricon_pytorch/pytorch/src/catch/torch_mlu/csrc/aten/operators/op_methods.cpp][line: 1217][eq][thread:140007329646400][process:66132]: OpMethods::eq Op running on CPU!
2021-04-21 11:42:31.951626: [cnmlError] MLU::unary dimension mismatch,output shape is wrong, the given shape is:(n=1, c=30,h=1,w=1, d=0, t=0, data in array:{1, 1, 1, 30, } , but the expected shape is:(n=30, c=1,h=1,w=1, d=0, t=0, data in array:{30, 1, 1, 1, }
2021-04-21 11:42:31.951728: [cnmlError] MLU::unary Op update tensor shape failed
[ERROR][/home/jiangyongjiu1/utils/v1.0.0rc1/cambricon_pytorch/pytorch/src/catch/torch_mlu/csrc/aten/operators/cnml/internal/abs_internal.cpp][line: 30][cnml_abs_internal][thread:140007329646400][process:66132]:
CNML error: CNML_STATUS_INVALIDPARAM
[WARNING][/home/jiangyongjiu1/utils/v1.0.0rc1/cambricon_pytorch/pytorch/src/catch/torch_mlu/csrc/aten/operators/op_methods.cpp][line: 424][abs][thread:140007329646400][process:66132]: OpMethods::abs Op running on CPU!
2021-04-21 11:42:31.965093: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.965119: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
2021-04-21 11:42:31.975662: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.975700: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
2021-04-21 11:42:31.977112: [cnmlError] MLU::dyadic_all Op should follow these rules: input1_n == input2_n, now, input1_n=30, input2_n=1op_id:15
2021-04-21 11:42:31.977226: [cnmlError] MLU::dyadic_all Op dimension mismatch
[ERROR][/home/jiangyongjiu1/utils/v1.0.0rc1/cambricon_pytorch/pytorch/src/catch/torch_mlu/csrc/aten/operators/cnml/internal/ne_internal.cpp][line: 35][cnml_ne_internal][thread:140007329646400][process:66132]:
CNML error: CNML_STATUS_INVALIDPARAM
[WARNING][/home/jiangyongjiu1/utils/v1.0.0rc1/cambricon_pytorch/pytorch/src/catch/torch_mlu/csrc/aten/operators/op_methods.cpp][line: 459][ne][thread:140007329646400][process:66132]: OpMethods::ne Op running on CPU!
2021-04-21 11:42:31.989077: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
2021-04-21 11:42:31.989116: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
[WARNING][/home/jiangyongjiu1/utils/v1.0.0rc1/cambricon_pytorch/pytorch/src/catch/torch_mlu/csrc/aten/operators/op_methods.cpp][line: 3174][masked_select][thread:140007329646400][process:66132]: OpMethods::masked_select Op running on CPU!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/nvme/yanzijie_cuda10/miniconda3/envs/pytorch/lib/python3.6/site-packages/torch/tensor.py", line 123, in __repr__
    return torch._tensor_str._str(self)
  File "/nvme/yanzijie_cuda10/miniconda3/envs/pytorch/lib/python3.6/site-packages/torch/_tensor_str.py", line 311, in _str
    tensor_str = _tensor_str(self, indent)
  File "/nvme/yanzijie_cuda10/miniconda3/envs/pytorch/lib/python3.6/site-packages/torch/_tensor_str.py", line 209, in _tensor_str
    formatter = _Formatter(get_summarized_data(self) if summarize else self)
  File "/nvme/yanzijie_cuda10/miniconda3/envs/pytorch/lib/python3.6/site-packages/torch/_tensor_str.py", line 87, in __init__
    nonzero_finite_vals = torch.masked_select(tensor_view, torch.isfinite(tensor_view) & tensor_view.ne(0))
RuntimeError: Expected object of scalar type Bool but got scalar type Float for argument #2 'mask' in call to _th_masked_select_bool
>>> ght", "credits" or "license" for more information.
  File "<stdin>", line 1
    ght", "credits" or "license" for more information.
          ^
SyntaxError: invalid syntax
>>> >>> import torch_mlu.core.mlu_model as ct
  File "<stdin>", line 1
    >>> import torch_mlu.core.mlu_model as ct
     ^
SyntaxError: invalid syntax
>>> CNML: 7.9.2 1a1e33b
  File "<stdin>", line 1
    CNML: 7.9.2 1a1e33b
              ^
SyntaxError: invalid syntax
>>> CNRT: 4.10.0 af3d5e7
  File "<stdin>", line 1
    CNRT: 4.10.0 af3d5e7
               ^
SyntaxError: invalid syntax
>>> >>> import torch
  File "<stdin>", line 1
    >>> import torch
     ^
SyntaxError: invalid syntax
>>> >>> cuda_a = torch.randn(3, 2, 1).to(ct.mlu_device())
  File "<stdin>", line 1
    >>> cuda_a = torch.randn(3, 2, 1).to(ct.mlu_device())
     ^
SyntaxError: invalid syntax
>>> >>> cuda_b = torch.randn(2, 5).to(ct.mlu_device())
  File "<stdin>", line 1
    >>> cuda_b = torch.randn(2, 5).to(ct.mlu_device())
     ^
SyntaxError: invalid syntax
>>> >>> torch.add(cuda_a, cuda_b)
  File "<stdin>", line 1
    >>> torch.add(cuda_a, cuda_b)
     ^
SyntaxError: invalid syntax
>>> 2021-04-21 11:42:31.830927: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
  File "<stdin>", line 1
    2021-04-21 11:42:31.830927: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
          ^
SyntaxError: invalid token
>>> 2021-04-21 11:42:31.831007: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
  File "<stdin>", line 1
    2021-04-21 11:42:31.831007: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
          ^
SyntaxError: invalid token
>>> 2021-04-21 11:42:31.857678: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
  File "<stdin>", line 1
    2021-04-21 11:42:31.857678: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
          ^
SyntaxError: invalid token
>>> 2021-04-21 11:42:31.857730: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
  File "<stdin>", line 1
    2021-04-21 11:42:31.857730: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
          ^
SyntaxError: invalid token
>>> 2021-04-21 11:42:31.871900: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
  File "<stdin>", line 1
    2021-04-21 11:42:31.871900: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
          ^
SyntaxError: invalid token
>>> 2021-04-21 11:42:31.871951: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
  File "<stdin>", line 1
    2021-04-21 11:42:31.871951: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
          ^
SyntaxError: invalid token
>>> 2021-04-21 11:42:31.887486: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
  File "<stdin>", line 1
    2021-04-21 11:42:31.887486: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
          ^
SyntaxError: invalid token
>>> 2021-04-21 11:42:31.887535: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
  File "<stdin>", line 1
    2021-04-21 11:42:31.887535: [cnrtWarning] [66132] [Card : 0] The device you run is MLU290, but the platform in kernel is MLU270!
          ^
SyntaxError: invalid token
>>> 2021-04-21 11:42:31.903459: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
  File "<stdin>", line 1
    2021-04-21 11:42:31.903459: [cnrtWarning] [66132] [Card : 0] The device you run is not the same as the platform in kernel!
          ^
SyntaxError: invalid token
```



senseparrots运行结果：

![image-20210421111308110](/Users/xym/Library/Application Support/typora-user-images/image-20210421111308110.png)

cuda_pytorch运行结果：

![image-20210421111039014](/Users/xym/Library/Application Support/typora-user-images/image-20210421111039014.png)

出现同样问题的有：

cuda_a.shape: (3, 2, 1)

cuda_b.shape:(2, 5)