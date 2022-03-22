# ML Metric

머신러닝에서는 학습이 잘 되었는지 확인하기 위한 다양한 Metric이 존재합니다 
이번 포스트에서 대표적인 Metric들을 알아보겠습니다 

Metric은 크게 **분류를 위한 평가지표**와 **회귀를 위한 평가지표** 이 두가지로 나눌 수 있습니다

## Classification(분류) Metric 

### Confusion Matrix(오차 행렬)

먼저 오차 행렬은 *모델이 예측을 하면서 얼마나 헷갈리고 있는지를 보여주는 지표*입니다
주로 이진 분류에서 많이 사용하며 아래의 그림과 같이 나타낼수 있습니다 

![image](https://user-images.githubusercontent.com/80239748/158939837-af925bf1-ebd8-44d5-93ba-6dfb70203b27.png)

* 기준은 Model이 낸 output이 기준이 되므로, Prediction을 기준으로 명명합니다 
* 모델이 Positive로 분류했으며 Positive, 모델이 Negative로 분류했으면 Negative로 명명됩니다
* 이때 정답을 맞춘 Positive라면 True Positive, 틀린 Positive라면 False Positive가 됩니다 
* 위에서 표시된 TP,FP,FN,TN을 바탕으로 다양한 Metric을 구할 수 있습니다 

Accuracy - 정확도
- TP + TN / (TP+FP+TN+FN) 전체중에 `True`의 개수

Precision - 정밀도
- TP / (TP + FP) 모델이 예측한 positive중에서 실제 Positive의 비율(**긍정 데이터 예측 성능에 초점을 맞춘 평가지표**)

Recall - 재현율
- TP / (TP + FN) 실제 Positive중 모델이 예측한 비율(**예측을 긍정으로 한 데이터 중 실제로 긍정인 비율**)

------------------------

`정밀도`와 `재현율`은 **트레이드오프 관계**를 갖습니다 정밀도는 *FP*을 재현율은 *FN*을 낮춤으로써 긍정 예측 성능을 높일 수 있습니다 

이같은 특성 때문에 정밀도가 높아지면 재현율은 낮아지고 재현율이 높아지면 정밀도는 낮아지고
가장 좋은 경우는 두 지표 다 적절히 높은 경우입니다 

----------------------



Fall -Out 
- FP / (FP + TN) 실제로는 Negative인데 모델이 Positive로 오탐한 비율

F1 Score 
**정밀도와 재현율 한 쪽에 치우치지 않고 둘 다 균형을 이루는 것**

- 무조건 Positive로 분류하면 Recall이 1이 되지만 Precision이 폭락하고 무조건 Negative로 분류하면 Precision은 1이 되지만 Recall이 0이 됩니다 
- 이처럼 Precision이나 Recall은 단일 Metric으로 사용하기엔 모델의 일반화 성능을 나타낼 수 없다는 한계점이 존재합니다 그러기에 Precision과 Recall의 조화평균값인 F1 Score를 사용할 수 있습니다 

![image](https://user-images.githubusercontent.com/80239748/159257049-5b091525-971e-4af8-968b-7984e5c2e742.png)

### ROC-AUC

![image](https://user-images.githubusercontent.com/80239748/159465916-500501ec-bba7-46ba-938b-ad58f1304d49.png)

ROC는 **FPR(False Positive Rate)가 변할 때 TPR(True Positive Rate)가 어떻게 변하는지를 나타내는 곡선**을 말합니다 
(여기서 FPR이란 FP / (FP + TN)이고, TPR은 TP / (FN + TP)으로 재현율을 말합니다)

그럼 어떻게 FPR을 움직일까요?
바로 분류 결정 임계값을 변경함으로써 움직일 수 있습니다 FPR이 0이 되려면 임계값을 1로 설정하면 됩니다 

그럼 긍정의 기준이 높으니 모두 부정으로 예측될 것입니다 반대로 1이 되려면 임계값을 0으로 설정하여 모두 긍정으로 예측시키면 됩니다 
이렇게 **임계값을 움직이면서 나오는 FPR과TPR을 각각 x와 y좌표로 두고 그린 곡선이 ROC**입니다

AUC는 ROC곡선의 넓이를 말한다 AUC가 높을수록 즉, AUC가 높을수록 즉, AUC가 왼쪽 위로 휘어질수록 좋은 성능이 나온다고 판단합니다 TPR이 높고 FPR이 낮을수록 예측 오류는 낮아지기 때문에 성능이 잘 나온다고 볼 수 있습니다 

마지막으로 *회귀 작업*에 적용할 수 있는 평가지표를 살펴봅시다

MAE(Mean Absolute Error)는 *예측값과 정답값 사이의 차이의 절대값의 평균*을 말합니다
![image](https://user-images.githubusercontent.com/80239748/159469564-db3c471f-1955-403e-bdc7-a701290d8ca9.png)

MSE(Mean Squared Error)는 *예측값과 정답값 사이의 차이의 제곱의 평균*을 말하며, MAE와 달리 제곱을 했기 때문에 **이상치에 민감**합니다
![image](https://user-images.githubusercontent.com/80239748/159469802-04a67b3d-e299-4b76-af61-7b6f49464ab4.png)

RMSE(Root Mean Squared Error)는 *MSE에 루트를 씌운 값*을 말합니다
![image](https://user-images.githubusercontent.com/80239748/159469959-7ec35015-ff88-443d-8376-0dac12a38059.png)

RMSLE(Root Mean Squared Logarithmic Error)는 RMSE와 비슷하나 *예측값과 정답값에 각각 로그를 씌워 계산*을 합니다
![image](https://user-images.githubusercontent.com/80239748/159470175-ea90cecb-e5ea-4690-ad2f-d923f9414b08.png)

R Squared는 *분산을 기반으로 예측 성능을 평가하는 지표*를 말합니다 정답값의 분산 대비 예측값의 분산 비율을 지표로 하며, 1에 가까울수록 정확도가 높습니다