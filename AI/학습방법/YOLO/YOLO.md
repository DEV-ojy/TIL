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
