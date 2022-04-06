# Sqeezenet(모델 압축)
> 딥러닝의 발달로 분류 정확도가 매우 좋아졌습니다. 하지만 반면급부로 모델의 복잡도 또한 그만금 증가하게 되었습니다. 이에 따라 모델의 파라미터 수와 크기를 줄이면서 정확도를 최대한 유지하고자 하는 연구들도 발전하게 되었습니다.  
> 논문 저자들은 이렇게 알렉스넷(AlexNet)과 비슷한 성능을 내면서도 파라미터는 50배나 줄고 모델 사이즈는 0.5MB밖에 안되는 Squeezenet이라는 네크워크 구조를 제시합니다.

### Intorduction and Motivation
> 동일한 성능을 가지는 모델이 파라미터 수가 더 적다면 다음과 같은 장점을 가질 수 있습니다.
- More efficient distributed training
  - 병렬학습 때 굉장히 큰 효율이 납니다.
- Less overhead when exporting new models to clients
  - 자율주행과 같이 실시간으로 서버와 소통해야 하는 시스템의 경우, 매우 좋습니다. 데이터 전송 자체가 크지 않기 때문에 서버 과부하도 적게 걸리고 더욱 더 업데이트를 자주 할 수 있게 됩니다.
- Feasible FPGA and embedded deployment
  - FPGA(일종의 반도체 소자)는 보통 10MB 이하의 휘발성 메모리를 가지고 있습니다. 작은 모델은 직접적으로 FPGA에 모델을 심을 수 있으며, 이는 다른 기관을 통해 inference할 경우 생기는 병목현상(bottleneck)이 없어집니다. 또한 ASIC(Application-Specific Integrated Circuits)에 직접적으로 CNN을 배치할 수 있게됩니다.

### Architectural design strategies
1. Replace 3x3 filters with 1x1 filters
- 모든 3x3 convolution filter를 1x1 필터로 교체합니다. 이는 1x1 필터가 3x3 필터에 비해 9배나 더 적은 파라미터를 가지고 있기 때문입니다.
2. Decrease the number of input channels to 3x3 filters
- 만약 모델의 레이어 하나가 전부 3x3 필터로 구성되어 있다면, 파라미터의 총 수는 (input channel) x (number of filters) x (3x3)개와 같습니다. 따라서 3x3 필터 자체의 수를 줄이고 이에 더해 3x3으로 들어가는 input channel의 수도 줄여야합니다. 논문에서는 squeeze layer를 사용하여 input channel -> 3x3 filter로의 수를 줄여 버립니다.
3. Downsample late in the network so that convolution layer have large activation
- Downsampling part를 네트워크 후반부에 집중시키는 방법도 사용합니다. 보통 downsample은 max(or average) pooling 또는 필터 자체의 stride를 높이는 방식으로 이미지의 spatial resolution을 줄이게 됩니다. 이렇게 줄여서 한번에 필터가 볼 수 있는 영역을 좁히면서 해당 이미지의 정보를 압축시키는 것입니다. (이에 대한 좀 더 자세한 설명은 CapsNet-1 포스트 pooling 파트를 참고하시면 좋을 것 같습니다.) 논문의 저자들은 모든 조건이 동등하다는 가정하에서 큰 activation map을 가지고 있을 수록 성능이 더 높다는 영감을 얻었습니다. 따라서 스퀴즈넷에서는 네크워크 후반부에 downsample을 넣는 방법을 취합니다.
  
> 일단 1번과 2번은 CNN 전체 파라미터 수를 줄이면서 정확도를 최대한 보존하는 것에 초점을 맞췄습니다. 3번의 경우는 파라미터 수가 제한된 상황에서 정확도를 최대화 시키는 방식입니다.   
> 이렇게 3가지 전략을 적용시킨 것을 fire module이라고 합니다.

### 관련 싸이트
- https://mole-starseeker.tistory.com/18
- https://jayhey.github.io/deep%20learning/2018/05/26/SqueezeNet/
- https://github.com/motlabs/mot-dev/tree/master/lab8_squeezenet
- https://github.com/jhcha08/Implementation_DeepLearningPaper/blob/master/CNN.%20SqueezeNet.ipynb