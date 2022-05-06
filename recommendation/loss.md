# [손실 함수](https://velog.io/@danceintherain/%ED%9A%8C%EA%B7%80-%ED%8F%89%EA%B0%80-%EC%A7%80%ED%91%9C)
>  loss는 손실함수를 의미합니다. 모델을 훈련시킬때 이 손실 함수를 최소로 만들어주는 가중치들을 찾는 것을 목표로 삼습니다. 위 예에서는 손실함수로 MSE(mean squared error)를 사용했습니다. 손실함수로 MSE만 사용할 수 있는 것이 아니고, MAE(mean absolute error), hinge, categorical crossentropy, sparse categorical crossentropy, binary crossentropy 등도 사용할 수 있습니다. 자신이 훈련시키는 모델에 적합한 손실함수를 선택해주면 됩니다. 예를 들어, 10개의 클래스를 분류할 수 있는 분류기를 훈련시키는 경우에는 손실함수로 sparse categorical crossentropy를 사용할 수 있습니다.

## 1. RSS - 단순 오차
- 실제 값과 예측 값의 단순 오차 제곱합: Loss와 거의 비슷한 형태
- 값이 작을 수록 모델의 성능이 높음
- 전체 데이터에 대한 실제 값과 예측하는 값의 오차 제곱의 총합
### 특징
- 가장 간단한 평가 방법으로 직관적인 해석이 가능함
- 그러나 오차를 그대로 이용하기 때문에 입력 값의 크기에 의존적임
- 절대적인 값과 비교가 불가능함  
> 비슷한 정도로 잘 예측한 데이터여도 데이터의 Raw 값 자체가 크면 RSS값이 크게 나타남. 어떤 모델이 더 좋은지에 대해 비교하기가 애매하다.

## 2. MSE, MAE - 절대적인 크기에 의존한 지표
### 2-1. MSE (Mean Squared Error) -> L2
- 평균 제곱 오차, RSS에서 데이터 수 만큼 나눈 값
- 작을수록 모델의 성능이 높다고 평가할 수 있음  
> Loss라는 것은 그 모델에서 줄여야하는 값, 형태가 꼭 이러란 법은 없음. 계산을 위한 것이지, 특정한 지표를 말하는 것이 아니다!  
### 2-2. MAE (Mean Absolute Error) -> L1
- 평균 절대값 오차, 실제 값과 예측 값의 오차의 절대값의 평균
- 적을수록 모델의 성능이 높다고 평가할 수 있음
### 특징
- MSE: 이상치 즉, 데이터들 중 크게 떨어진 값에 민감함
- MAE: 변동성이 큰 지표와 낮은 지표를 같이 예측할 시 유용
- 가장 간단한 평가 방법들로 직관적인 해석이 가능함
- 그러나 평균을 그대로 이용하기 때문에 입력 값의 크기에 의존적임
- 절대적인 값과 비교가 불가능함

## 3. R^2 R squre (걸졍 계수)
- 회귀 모델의 설명력을 표현하는 지표
- 1에 가까울수록 높은 성능의 모델이라고 해설할 수 있음
- 절대적인 값으로 비교가능!!
- $1 - {예측값과의 차이 제곱의 합(RSS) \over 평균값과의 차이 제곱의 합(TSS)}$
> 잘 예측할수록 RSS값이 작아지므로 1에 가까워지고, 단순 평균 낸 것과 비슷한 수준의 예측이면 0에 가까워짐.  
> 단순 평균 낸 것보다도 못한 예측이면 RSS가 TSS보다 커져서 결정계수값은 마이너스값이 될 수 있음  
### 특징
- 오차가 없을수록 1에 가까운 값
- 값이 0인 경우, 데이터의 평균 값을 출력하는 직선 모델을 의미
- 음수 값이 나온 경우, 평균 값 예측보다 성능이 좋지 않음


