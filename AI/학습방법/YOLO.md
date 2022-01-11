#  YOLO(You Only Look Once) Object Detection 모델 

Object detection 분야에서 쓰이는 모델로는, Faster-RCNN, MobileNet, SSD 등 많은 모델이 있지만 그 중 YOLO 모델에 대해 자세히 알아보려고합니다

YOLO는 버전 1,2,3 까지 현재 나와있는 상태이고 앞으로 소개할 YOLO 모델 종류들은 모두 하나의 공통점을 가지고 있습니다 

바로 `입력 이미지 또는 Feature Map을 특정 그리드로 나누고 각 Cell 마다 Object Detection을 수행하는 것`입니다 

Feauture Map의 각 포인트마다 Object Detection을 수행하는 원리와 동일하다 그리드의 각 Cell이 무엇을 의미하는지 잘 모르는 사람도 있을 수 있기에 하단의 그림을 참조하겠습니다

![image](https://user-images.githubusercontent.com/80239748/145363831-8837eb70-0e9b-409c-940e-f457fb0d0ef8.png)


# YOLO - Version 1 

YOLO 버전 1 모델은 컨볼루션을 거친 Feature Map이 아닌 `입력 이미지 자체를 특정 그리드 S x S로 나눕니다` 그리고 `나눈 그리드의 각 Cell마다 Anchor Box를 2개씩 씌우고 이를 기반으로 Ground Truth와 비교를 하면서 Object Detection을 수행`합니다 

![image](https://user-images.githubusercontent.com/80239748/145364619-040b7317-cf88-4d14-bf6b-4cada920dd61.png)

(구글에서 검색한 YOLO 모델의 아키텍처)

![image](https://user-images.githubusercontent.com/80239748/145366679-61638db9-1cd4-4524-80d9-bb2deef40110.png)

(보는 블로그 필자가 직접 만든 아키텍처)

YOLO 버전 1 모델은 **입력 이미지를 7 x 7 그리드로 나누고 나눈 Cell 당 하나의 Object Detection을 수행하고 그 결과를 통합** 해서 최종적인 Object Detection을 수행해주는 것입니다 

위 자료의 빨간색 1 x 1 x 30 벡터를 설명해 놓은 부분을 봐봅시다 

하나의 Anchor Box에 대한 벡터 5개. 이 Box가 2개가 있으므로 총 10개, 그리고 Pascal VOC Dataset 기준으로 클래스 종류가 20개이기 때문에 20개의 벡터, 이들을 합하면 총 30개의 벡터가 되는 것을 볼 수 있습니다

이렇게 하나의 Cell 마다 Object Detection을 수행해주고 나면 수많은 Bounding Box들이 도출될 것이다

이 때 Ground Truth와 최대한 유사한 최적의 Bounding Box들 만을 남기기 위해 NMS 과정을 수행해준다

하지만 YOLO 버전 1모델의 치명적인 단점은 그리드를 나눈 각 Cell 마다  Anchor Box가 2개밖에 없다는 것이다 `Anchor Box가 2개라면 그만큼 ROI(Regions Of Interest, 객체가 있을만한 후보 영역)들이 적을 것이고 이는 결국 Object를 잘 탐지하지 못하게 되는 문제가 발생한다` 라는 점입니다

또한 입력 이미지를 그리드 셀로 나누고 각 Cell 마다 Object Detection을 수행하기 때문에 만약 하나의 그리드 Cell에 여러개 Object가 겹쳐있으면 단순히 하나의 Object로만 탐지하고 넘어간다는 것입니다

이런 점을 보안하고자 나온 것이 YOLO Version 2 입니다

# YOLO - Version 2

1. 입력 이미지가 아닌 Feature Map에서 13 x 13 그리드로 나누고 각 Cell 마다 Object Detection을 수행
2. 각 Cell 당 씌우는 Anchor Box 개수를 5개로 늘리기
3. 동일한 이미지 이지만 크기만 다르게 해서 모델을 학습(Multi-Scaling)
4. 모델에 Batch Normalization 적용
5. 분류 모델을 Fine Tuning
6. Darknet-19 라는 개별의 Feature Extractor 사용

Version2 에서 주목해야 할 특징은 1,2번입니다 나머지 특징들은 읽기만 해도 이해가 될 것 입니다 우선 기본적인 YOLO 버전 2의 아키텍처를 살펴봅시다

![image](https://user-images.githubusercontent.com/80239748/145386461-aab02264-e8d6-4e09-a846-6fe9c50ad537.png)

(YOLO Version 2 모델 아키텍쳐)

버전 1모델과 두드러진 차이점은 `FC Layer가 없어졌다는 점` 이다 그리고 입력 데이터가 아닌 `Feature Map에서 13 x 13 그리드로 나누고 각 Cell 마다 Object Detection을 수행한다는 점`이다

![image](https://user-images.githubusercontent.com/80239748/145386795-8322c255-3dfb-425e-b84e-e772c8174373.png)

(YOLO Version 2의 큰 아키텍처)

위 그림을 보다시피 전개되는 과정은 버전 1 모델과 유사하다 ` Feature Map에 그리드를 나눈다는 점과 각 그리드 Cell 마다 Anchor Box를 2개가 아닌 5개를 씌워준다는 점`이 다르나 그런데 여기서 Anchor Box를 5개 씌워줄 때 서로 다른 크기의 박스들을 씌워준다고 했습니다 

그러면 서로 다른 적절한 크기를 어떻게 설정해줄까요?

`5개의 서로 다른 Anchor Box의 사이즈 기준은 입력되는 이미지 데이터의 Ground Truth의 Bouding Box를 분석해 비슷한 부분끼리 그룹핑되도록 K-means Clustering을 사용`하게 됩니다

![image](https://user-images.githubusercontent.com/80239748/145387339-bb94bff1-ca59-46af-941a-55818440a5bd.png)

(K-means를 활용해 서로 다른 사이즈의 Anchor Box 설정하기)

결과적으로 하나의 그리드 Cell에 대해 125개의 벡터가 존재하게 됩니다 하나의 Anchor Box당 25개의 벡터가 존재하고 Anchor Box가 5개가 있어 25∗5인 125가 됩니다


# YOLO - Version 3 

YOLO 버전 2 모델은 버전1에서 탐지속도와 탐지성능을 대폭 개선했었더라면 버전 3는 버전 2에서 탐지 속도는 약간 느려졌지만 탐지성능을 여기서 더 대폭 개선한 버전이라고 할 수 있습니다 

모델 3의 특징은 다음과 같습니다 

1. SSD의 Multi-Scale Feature Layer와 유사한 기법을 적용
2. Multi-label Classification을 해결하기 위해 클래스 분류 시 Softmax가 아닌 독립적인 여러개의 Sigmoid Layer를 사용
3. 하나의 그리드 Cell 당 3개의 Anchor Box를 씌움
4. 클래스 종류가 80개인 COCO Dataset을 사용
5. Darknet-53 이라는 개별 Feature Extractor를 사용
6. 동일하지만 사이즈만 다른 이미지들을 학습(Multi-Scaling), Data Augmentation 사용
7. Layer 중간에 Feature Map 사이즈 축소를 막기 위한 Up Sampling 사용
8. Resnet과 같이 Gradient Vanishing을 방지하기 위해 Skip Connection을 사용

여러가지 특징 중 1,2번에 대해서 자세히 설명하겠습니다 

## 3-1. SSD의 Multi-Scale Feature Layer 아이디어를 빌려보자!

버전 2모델과 가장 큰 차이점 중 하나는 SSD 모델에서 Multi-Scale Feature Layer와 추후에 Resnet에서 살펴볼 FPN(Feature Pyramid Network)과 유사한 기법을 적용했다는 것입니다 

아직 Resnet은 배우지 않았으니 SSD의 Multi-Scale Feature Layer에 대해 다시 상기해봅시다 
이것은 서로 다른 크기의 Feature Map에 각 포인트마다 Object Detection을 수행해주는 기법이었습니다 

YOLO 버전 3 모델은 이 Multi-Scale Feature Layer를 그리드에 적용해주는 셈입니다 
우선 큰 아키텍처부터 살펴봅시다

![image](https://user-images.githubusercontent.com/80239748/145583315-c5062a07-a92a-4330-99f5-82f6cebbcad0.png)

(모델 3의 큰 아키텍쳐)

위 그림을 보시다 시피 버전 3 모델은  82번째, 94번째, 106번째 Layer의 `Feature Map에서 각각 서로 다른 크기의 그리드로 나누고 각 Cell 마다 Object Detection을 수행` 하게 됩니다ㅣ

단의 자료는 위 그림의 전체 구조보다 각기 다른 Feature Map에 Multi-Scale Feature Layer를 사용하는 부분에 집중해서 자료를 만들었다는 점을 참고해주면 좋겠습니다 

![image](https://user-images.githubusercontent.com/80239748/145583485-8d67a660-551b-4976-a9cc-2018a790db0b.png)

(YOLO Version 3에서의 Multi-Scale Feature Layer)

YOLO 버전 3 모델은 위의 Multi-Scale Feature Layer 기법을 사용해 그리드 사이즈가 작을 때는 Anchor Box 크기가 커지므로 상대적으로 큰 객체를, 그리드 사이즈가 클 때는 Anchor Box 크기가 작아지므로 상대적으로 작은 객체를 잘 탐지하도록 하기 위해 구현되었습니다

## 3-2. 독립적인 여러개의 Sigmoid로 Multi-label Classification 해결

    해당 내용을 이해하기 전에 Multi-label Classification과 Multi-class Classification의 차이점을 이해해야 합니다

* Multi-label Classification : 동시에 여러개의 레이블을 가질 수 있다. 예를 들어 '남자(레이블1), 사람(레이블2)' 를 동시에 가질 수 있습니다 

* Multi-class Classification : 무조건적으로 하나의 레이블만 가질 수 있다. 예를 들어 '남자(레이블1)' 또는 '사람(레이블2)' 둘 중 하나만 가질 수 있습니다

그동안의 Object Detection 모델은 객체의 최종 클래스 분류를 위해 모든 클래스의 확률 값을 더하면 무조건 1이 되는 Softmax Layer를 사용했습니다

즉, Multi-class Classification 문제만을 해결했습니다
하지만 `YOLO 버전 3 모델`은 최종 클래스를 분류할 때 Softmax Layer가 아닌 `각 클래스 마다 Sigmoid(=Logisitc 함수) Layer를 사용해 Multi-label Classification을 해결`할 수 있게했습니다 

예를 하나만 들어보자. '남자'라는 객체가 들어있는 이미지가 YOLO 버전 3 모델로 입력되었습니다
그리고 주어진 클래스 종류는 [사람, 남자, 강아지]라고 해볼때 Softmax Layer를 사용하게 되면 각 클래스에 대한 확률 Score가 대략 [0.3, 0.6, 0.1]가 될 것입니다 

즉, 세 값의 총 합은 1이 된다. 그렇기 때문에 예측 모델은 가장 Score가 높은 0.6인 '남자'로만 예측할 것입니다 

하지만 여기서 `각 클래스 마다 독립적인 Sigmoid Layer를 사용`하게 되면 Score는 [0.8, 0.8, 0.2] 정도가 될 것이고 결국 Score의 값 하나씩 분류 결정 임곗값(여기서 0.5라고 합시다)과 비교해서 크면 1, 작으면 0으로 분류하게 됨에 따라 Multi-label로 예측하게 될것입니다 

다시 말해 입력된 이미지는 '사람' 이면서 '남자' 인 2개의 레이블을 갖도록 예측하게 되는 것입니다 


참고자료: https://techblog-history-younghunjo1.tistory.com/186

##### 2021.12.11