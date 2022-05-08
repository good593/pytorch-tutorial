# [Recommendation with pytorch](https://pytorch.org/tutorials/intermediate/torchrec_tutorial.html)

## 1. Algorithms
- https://tech.kakao.com/2021/10/18/collaborative-filtering/
- https://betterprogramming.pub/building-a-recommendation-engine-with-pytorch-d64be4856fe7
> 신규 아이템의 경우 유저와의 상호작용 데이터가 없기 때문에 CF 모델에서는 추천되기 어렵지만, CB 모델에서는 텍스트 혹은 이미지 유사성 기반의 추천이 가능합니다. 한편, CF 모델은 유저-아이템의 상호작용을 바탕으로 하기 때문에, 꼭 텍스트/이미지 기반 유사성인 높지 않더라도, 실제로 함께 소비하는 경향이 높은 아이템을 발견하여 추천이 가능합니다.   
> 이처럼 CF와 CB 모델은 서로 상호 보완적인 역할을 한다고 볼 수 있습니다.

### 1-1. Content-based filtering; CB
> 유저-아이템의 상호작용 데이터 없이도, 아이템 자체의 이름, 카테고리, 상세 설명, 이미지 등을 활용해 유사성을 판단하고 비슷한 아이템을 추천할 수 있습니다.  

### 1-2. Collaborative filtering; CF
> CF 모델의 핵심 가정은 나와 비슷한 취향을 가진 유저들은 어떠한 아이템에 대해 비슷한 선호도를 가질 것이라는 점입니다.    
> CF 모델은 크게 두 가지 접근 방법으로 나뉩니다. 메모리 기반의 접근 방식과 모델 기반의 접근 방식입니다.  
#### 메모리 기반의 접근 방식
> 가장 전통적인 접근 방식입니다. 유저 간/아이템 간 유사도를 메모리에 저장해두고 있다가, 특정 유저에 대하여 추천이 필요할 때 해당 유저와 유사항 k명의 유저가 소비한 아이템들을 추천하거나, 혹은, 특정 아이템에 대한 Rating 예측이 필요할 때 해당 아이템과 유사한 k개의 아이템의 Rating을 기반으로 추정을 할 수 있습니다.  
  
#### 모델 기반의 접근 방식
- Latent Factor; Matrix Factorization(행렬 분해)
> 모델 기반의 접근 방식 중에서도 Latent Factor 기반의 방식, 특히 아이템 Latent Vector(잠재 벡터)와 유저 Latent Vector 간 Inner Product로 아이템에 대한 유저의 선호를 모델링 하는 [Matrix Factorization](https://towardsdatascience.com/paper-summary-matrix-factorization-techniques-for-recommender-systems-82d1a7ace74) 방식의 접근은, 간단하지만 강력한 추천이 가능합니다.   
> Autoencoder를 추천에 활용하기도 하는데, 이는 Latent Factor 방식의 일반화(Generalization)라고 볼 수 있습니다.   
- Classification/Regression(분류/회귀) 방식
> 콘텐츠 기반 추천 방식과 쉽게 융합이 가능합니다. 피처 x가 주어졌을 때, 라벨 y를 예측하는 구조이기 때문에, 피드백 y를 예측하는 상황에서, x에 콘텐츠 관련 정보를 피처로 만들어서 추가하면, 피드백 데이터뿐만 아니라 콘텐츠 데이터를 활용한 추천이 가능합니다.  

### 1-3. 최신의 융합 모델 방식
- Latent Factor 모델과 Classification/Regression 모델의 특징을 모두 가지고 있는 Factorization Machine 계열의 모델  
- 딥러닝을 활용하여 복잡한 Interaction을 모델링 하는 방향으로 Latent Factor 모델을 확장한 Neural Collaborative Filtering

### [1-4. attentive sequential recommendation](https://lsjsj92.tistory.com/601)

## [2. Evaluation RS](https://velog.io/@redgem92/%EC%B6%94%EC%B2%9C%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C-04.-%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%ED%8F%89%EA%B0%80-%EC%A7%80%ED%91%9C)
- https://yeomko.tistory.com/32
- https://sungkee-book.tistory.com/11
### 2-1. 얼마나 정확하게 정답을 맞추었는지를 평가
- [MAP; Mean Average Precision](https://danthetech.netlify.app/DataScience/evaluation-metrics-for-recommendation-system)    
> $Precision = {True Positive \over Actual Results} = {True Positive \over True Positive + False Positive}$
  
- NDCG(normalized Discounted Cumulative Gain)
> - DCG: 실제 선택한 순서  
> - iDCG: 이상적인 선택 순서    
> $NDCG = {DCG \over iDCG}$ 
  
- Hit Rate
> 전체 사용자 수 대비 적중한 사용자 수를 의미한다(적중률)  
> 1. 사용자가 선호한 아이템 중 1개를 제외한다.  
> 2. 나머지 아이템들로 추천 시스템을 학습한다.  
> 3. 사용자별로 k개의 아이템을 추천하고, 앞서 제외한 아이템이 포함되면 Hit이다.  
> 4. 전체 사용자 수 대비 Hit한 사용자 수 비율을 구하면 Hit Rate가 된다.  
### 2-2. 다양하게 추천을 진행했는지 평가
- Entropy Diversity  
> 모든 사용자들에게 비슷한 종류의 상품을 추천할 경우 해당 상품 추천은 자주 발생하므로 정보량이 낮습니다. 반면 개인에게 맞춤화 된 추천은 발생 횟수가 적으므로 정보량이 높아집니다. 이들의 기대값을 구한 것이 바로 Entropy Diversity입니다.   
> Entropy Diversity만으로 추천 엔진이 더 정확하다고 평가할 수는 없습니다. 어디까지나 추천 결과의 다양성을 측정하는 지표이므로 MAP, NDCG처럼 정확도를 측정할 수 있는 지표와 함께 사용하는 것이 바람직해 보입니다.

## 3. dataset
- https://grouplens.org/datasets/movielens/



