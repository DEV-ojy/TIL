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













