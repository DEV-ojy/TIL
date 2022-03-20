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


