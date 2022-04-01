# CNN의 parameter 개수와 tensor 사이즈 계산하기
- https://seongkyun.github.io/study/2019/01/25/num_of_parameters/

### 1. Convolution layer와 output tensor size
> - $O$: Size(width) of output image
> - $I$: Size(width) of input image
> - $K$: Size(width) of kernels used in the Conv layer
> - $N$: Number of kernels
> - $S$: Stride of the convolution operation
> - $P$: Padding size
  
- $O$(출력 이미지 너비)는 다음과 같이 정의 됨  
> $O = {I - K + 2P \over S} + 1$  
  
- 출력 이미지의 채널 수는 커널의 갯수($N$)와 같음  
  
- Example 
> - 입력 이미지 크기: 227x227x3
> - kernel size(11) x 96개, padding size(0), stride size(4)  
>
> $O = {227 - 11 + 2 * 0 \over 4} + 1 = 55$ 
  
- 따라서, 출력 tensor size는 55x55x96  
  - 각 커널 당 하나의 채널을 나타내므로 3채널(RGB) 이미지에 대해 3배가 곱해져 총 **55x55x96x3**이 됨.  

### 2. MaxPool layer와 output tensor size
> - $O$: Size(width) of output image
> - $I$: Size(width) of input image
> - $S$: Stride of the convolution operation
> - $P_s$: Pooling size
  
- $O$는 다음과 같이 정의 됨
> $O = {I - P_s \over S} +1$
  
- Convolution layer와는 다르게 출력의 채널 수는 입력의 개수와 동일
- Conv layer의 $O$ 수식에서 커널 크기($K$)를 $P_s$로 대체하고 $P = 0$으로 설정하면 동일한 식이 됨  
  
- Example  
> - 입력 이키지 크기: 55x55x96
> - Pooling size(3), stride size(2)
> 
> $O = {55 - 3 \over 2} + 1 = 27$  
  
- 따라서 출력의 크기는 27 x 27 x 96

