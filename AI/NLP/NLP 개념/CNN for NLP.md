# NLP를 위한 CNN 

일반적으로 우리가 CNN이라고 생각하면 Computer Vision분야를 대부분 떠올릴것입니다 
실제로도 CNN은 Computer Vision분야에서 많은 발전을 이루었으며 Image Classification, Image Detection, Semantic Segmentation 등 많은 분야에서도 CNN을 활용해서 성능 발전을 보여준 사례가 많습니다 

최근에는 CNN을 NLP문제에 활용하기 위한 많은 시도들을 했습니다 
이 포스트에서 CNN의 설명과 NLP에서 CNN이 어떤 식으로 적용되는지에 대해서 설명하려고 합니다 이를 이용하여 CNN으로 문장을 분류도 함께 해보겠습니다 

## Convolutional Neural Network (합성곱 신경망)

CNN은 window가 sliding하며 Convolution연산이 수행되는 과정이 포함된 네트워크입니다 

