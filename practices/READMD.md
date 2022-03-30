# [ResNet(2015)](https://deep-learning-study.tistory.com/534)
- 전체코드 : https://github.com/Seonghoon-Yu/AI_Paper_Review
- 동빈나: https://github.com/ndb796/Deep-Learning-Paper-Review-and-Practice


## [배치 정규화: Batch Normalization](https://eehoeskrap.tistory.com/430)
- 배치 정규화는 단순하게 평균과 분산을 구하는 것이 아니라 감마(Scale), 베타(Shift)를 통한 변환을 통해 비선형 성질을 유지 하면서 학습 될 수 있게 해줌
- 배치 정규화가 신경망 레이어의 중간 중간에 위치하게 되어 학습을 통해 감마, 베타를 구할 수 있음
- Internal Covariate Shift 문제로 인해 신경망이 깊어질 경우 학습이 어려웠던 문제점을 해결
- gradient의 스케일이나 초기 값에 대한 dependency가 줄어들어 large learning rate를 설정할 수 있기 때문에 결과적으로 빠른 학습 가능함. 즉, 기존 방법에서 learning rate를 높게 잡을 경우 gradient가 vanish/explode 하거나 local minima에 빠지는 경향이 있었는데, 이는 scale 때문이었으며, 배치 정규화를 사용할 경우 propagation시 파라미터의 scale에 영향을 받지 않게 되기 때문에 learning rate를 높게 설정할 수 있는 것임
- regularization 효과가 있기 때문에 dropout등의 기법을 사용하지 않아도 됨
- 학습시 Deterministic하지 않은 결과 생성
- Learning Rate Decay를 더 느리게 설정 가능
- 입력의 범위가 고정되기 때문에 saturating한 함수를 활성화 함수로써도 saturation문제가 일어나지 않음. 여기서 saturation 문제란 가중치의 업데이트가 없어지는 현상임

## transfer-learning
transfer learning

### 참고 문서
- https://tutorials.pytorch.kr/beginner/transfer_learning_tutorial.html
- https://jeinalog.tistory.com/13
  > https://towardsdatascience.com/transfer-learning-from-pre-trained-models-f2393f124751
- https://sims-solve.tistory.com/18


### Transfer learning usage with different input size
https://discuss.pytorch.org/t/transfer-learning-usage-with-different-input-size/20744/3