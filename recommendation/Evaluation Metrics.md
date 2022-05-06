# [모델 평가 지표](https://heeya-stupidbutstudying.tistory.com/entry/ML-%EB%AA%A8%EB%8D%B8-%ED%8F%89%EA%B0%80%EC%A7%80%ED%91%9C-%EC%98%A4%EC%B0%A8%ED%96%89%EB%A0%AC-PRC-ROC-AUC)
- metric: 평가지표. 검증셋과 연관. 훈련 과정을 모니터링하는데 사용.   
> 검증셋에서 훈련된 모델의 성능을 평가할 때 어떤 평가지표로 평가할지를 결정해줍니다. 학습곡선을 그릴 때 손실함수와 평가지표를 에포크(epoch)마다 계산한 것을 그려주는데, 손실함수의 추이와 평가지표의 추이를 비교해보면서 모델이 과대적합(overfit) 또는 과소적합(underfit)되고 있는지 여부를 확인할 수 있습니다. 중요한 것은 평가지표로 어떤 것을 사용하더라도 모델 가중치의 업데이트에는 영향을 미치지 않는다는 사실입니다. 

## 1. 오차행렬(confusion matrix)
> 오차행렬은 이진 분류 평가 결과를 나타낼 때 가장 많이 쓰이는 방법 중 하나로, 총 4가지 항목으로 구성된다.  
- TP(True Positive): 양성을 양성이라고 예측
- TN(True Negative): 음성을 음성이라고 예측
- FP(False Positive): 음성을 양성이라고 예측; Type 1 error
- FN(False Negative): 양성을 음성이라고 예측; Type 2 error
### 1-1. 정확도(accuracy)
> 정확도는 오차행렬의 결과를 요약함으로써 얻어질 수 있다.  
$accuracy = {TP + TN \over TP + TN + FP + FN}$  
### 1-2. 정밀도(precision); PPV(양성 예측도)
> 정밀도는 양성으로 예측된 것(TP+FP) 중 얼마나 많은 샘플이 진짜 양성(TP)인지 측정  
$precision = {TP \over TP + FP}$  
### 1-3. 재현율(recall); 민감도, 진짜 양성 비율(TPR)
> 재현율은 전체 양성 샘플(TP + FN) 중에서 얼마나 많은 샘플이 진짜 양성(TP)인지 측정  
$recall = {TP \over TP + FN}$  
### 1-4. F1-score  
> 정밀도 최적화와 재현율 최적화는 동시에 이루어질 수 없다.  
> f1-score는 정밀도와 재현율의 조화 평균이다. 즉, 불균형한 이진 분류 데이터셋에서는 정확도보다 더 나은 지표가 될 수 있다.  
$F = 2 * {precision * recall \over precision + recall}$  

## 2. ROC & AUC
> ROC 곡선은 진짜 양성 비율(TPR)에 대한 거짓 양성 비율(FPR)을 나타낸다. TPR은 재현율의 또 다른 이름이며, FPR은 전체 음성 샘플 중에서 거짓 양성으로 잘못 분류한 비율이다.  
$FPR = {FP \voer FP + TN}$  
- ROC 곡선은 왼쪽 위에 가까울수록 이상적이다. FPR이 낮게 유지되면서 재현율이 높은 분류기가 좋은 것이다.  
- AUC는 ROC 곡선의 아래 면적값이다. 0과 1 사이의 곡선 아래의 면적이므로 항상 0(최악)과 1(최선) 사이의 값을 가진다.  
- FPR과 TPR은 오차행렬에서 각각 다른 행을 이용하여 만들기 때문에 클래스의 불균형이 FPR과 TPR 계산에 영향을 주지 않는다. 그래서 불균형한 데이터 셋에서는 정확도보다 AUC가 휠씬 좋은 지표이다.  


