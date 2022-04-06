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

### 관련 싸이트
- https://mole-starseeker.tistory.com/18
- https://jayhey.github.io/deep%20learning/2018/05/26/SqueezeNet/
- https://github.com/motlabs/mot-dev/tree/master/lab8_squeezenet
- https://github.com/jhcha08/Implementation_DeepLearningPaper/blob/master/CNN.%20SqueezeNet.ipynb