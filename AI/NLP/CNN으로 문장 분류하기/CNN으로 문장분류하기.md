# CNN으로 문장 분류하기 

이번에는 **Convolutional Neural Networks(CNN)**로 문장을 분류하는 방법에 대해 살펴보겠습니다 

https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/

### 자연어 처리에 특화된 네트워크 구조?

자연언어는 단어나 표현의 등장 순서가 중요한 `sequential data`입니다 아래의 예문을 보면 
> {무거운/\*가벼운/\*큰}침묵
> 침묵이 {\*무겁다}
 
> **Only** I hit him in the eye yesterday. (No one else did)
> I **only** hit him in the eye yesterday. (did not slap him)

`무거운 침묵`은 고정된 형식으로 `정적이 흐르는 상태가 매우 심하다`는 뜻의 연어(collocation)으로 쓰입니다 하지만 순서를 바꿔서 `침묵이 무겁다`는 표현은 문장 자체가 성립되지 않은 비문이라고 할 수 있습니다 

영어의 경우위 예시처럼 단어 등장 순서가 의미 차이를 만드는 경우가 많습니다 이렇듯 단어나 표현의 순서는 그 의미 차이를 드러내거나 문장 성립 여부를 결정하는 등 중요한 정보를 함축하고 있습니다 

**Recurrent Neural Networks(RNN)**이나 이번 포스팅의 주제인 CNN은 등장 순서가 중요한 sequential data를 처리하는 데 강점을 지닌 아키텍처입니다 RNN의 경우 아래와 같이 입력값을 순차적으로 처리합니다 입력값을 `단어`로 바꿔놓고 생각해보면 단어의 등장 순서를 보존하는 형태로 학습이 이뤄지게 됨을 알 수 있습니다

![image](https://user-images.githubusercontent.com/80239748/154504968-88e9ff2c-78bc-4426-b301-2cbf0a1fb446.png)

그렇다면 CNN은 어떨까요? 본래 CNN은 이미지 처리를 하기 위해 만들어진 아키텍처입니다
아래 사진처럼 필터(filter)가 움직이면서 이미지의 지역적인 정보를 추출, 보존하는 형태로 학습이 이뤄지게 됩니다

![OXwLhaf](https://user-images.githubusercontent.com/80239748/154803988-206cc27e-f293-445e-a6e7-2c96fad973e0.gif)

이미지 처리를 위한 CNN필터가 이미지의 지역적인 정보를 추출하는 역할을 한다면,텍스트 CNN의 필터는 텍스트의 지역적인 정보, 즉 단어 등장순서/문맥정보를 보존한다는 것입니다 이를 도식화하면 

![1Flo6TK](https://user-images.githubusercontent.com/80239748/154804291-1aa72aab-fb6b-407e-a1d3-ac7a40ac0f00.gif)

자세히 보면 한 문장당 단어 수는 총 n개입니다 이 단어들 각각은 p차원의 벡터입니다 
붉은색 박스는 필터를 의미합니다 위 움짤의 경우 필터의 크기는 2로써 한번에 단어 2개씩을 보게 됩니다 
이 필터는 문장에 등장한 단어 순서대로 슬라이딩해가면서 문장의 지역적인 정보를 보존하게 됩니다 
필터의 크기가 1이라면 Unigram, 2라면 Bigram, 3이면 Trigram.. 이런 식으로 필터의 크기를 조절함으로써 다양한 N-gram 모델을 만들어낼 수 있습니다
