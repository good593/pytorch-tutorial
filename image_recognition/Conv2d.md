# [Pytorch Conv2d 다루기](https://gaussian37.github.io/dl-pytorch-conv2d/)
```python
torch.nn.Conv2d(
    in_channels, 
    out_channels, 
    kernel_size, 
    stride=1, 
    padding=0, 
    dilation=1, 
    groups=1, 
    bias=True, 
    padding_mode='zeros'
)
```
> input & output는 (N, C, H, W)입니다.
> - N: batch size
> - C: 이미지 채널 수
> - H, W: height, width

### Output Size = (W - F + 2P) / S +1
> - W: input_volume_size
> - F: kernel_size
> - P: padding_size
> - S: strides
```python
nn.Conv2d(3, 32, 3, padding=1)
```
32*32 Imaage의 width인 32가 W의 input_volume_size가 됩니다.
> output_size = (32 - 3 + 2*1) / 1+1 = 32  
  
즉, output_filer_size는 32*32 Image가 되겠고, depth는 32가 됩니다.

