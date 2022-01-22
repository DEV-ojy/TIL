# [NLP] 자연어 처리를 위한 필수 개념 정리: Language model, Representation

**Language Model(언어 모델)**

[정의]
단어 시퀀스에 대한 확률 분포로 시퀀스 내 단어 토큰들에 대한 확률을 할당하는 모델이다 

m개의 단어가 주어질 때, m개의 단어 시퀀스가 나타날 확률은 다음과 같다 

![image](https://user-images.githubusercontent.com/80239748/150287102-6c929e55-c66e-49c7-a885-843990d5195a.png)

예를 들어, 시퀀스 내 단어들이 'Today is monday" 라는 문장을 이루게 되는 확률을 구해보자
"Today"가 선택될 확률은 P("Today")다 그 다음 "is"가 올 확률은 P("Today")*P("is")라고 생각할 수도 있다 하지만 글은 순서가 동일해야 똑같은 의미를 지니는 **시퀀스데이터**다 

따라서 다음과 같이 표현되어야 한다 

![image](https://user-images.githubusercontent.com/80239748/150287454-3e1e9fd3-2d61-4ee8-b6fe-52e5f9ff9019.png)

이러한 확률 분포는 학습 데이터의 성격에 따라 매번 다르게 계산될 것이다 왜냐하면 학습 데이터의 성격이 다르면 사용되는 단어의 분포가 다르기 때문이다 

[사용]
언어 모델은 확률 분초에 따라 시퀀스를 추출하기에 용이하다 따라서 다음과 같은 용도로 많이 사용된다 

* Machine translation(기계 번역) : Source 언어의 text에서 target 언어의 text로 변환
* Speech recognition : 오디오 신호에서 text로 변환
* Summarization : 긴 text에서 짧은 text로 변환
* Dialogue system : 사용자의 입력(그리고 knowledge base)에서 text response로 변환

[한계]
실제로 문장의 확률을 계산하기 위해서는 엄청난 양의 Corpus(말뭉치)가 필요할 것이다 
가령 "He loves"라는 문장 뒤 어떤 단어가 올지 LM의 기본 개념을 통해 확률을 구한다고 하면 확률 P는 다음과 같다 

![image](https://user-images.githubusercontent.com/80239748/150526420-cb837eec-e928-4f1a-8e3a-d90f5313fd44.png)

LM(Language Model)은 corpus중 "He loves her"와 같은 표현이 많을수록 확률을 높게 계산할 것이다
그렇다면 "He loves him"은 어떨까? 분명 실세계에서는 충분히 나올 수 있는 문장이다 그러나 corpus에 이러한 문장이 없다면 확률은 0이 되어 [P(W)=0] "him"을 절대로 예측할 수 없을 것이다 

이러한 문제점을 해결하기 위해 일반화가 반드시 필요하다 일반화가 될 수 있도록 하는 방법 중 **N-gram**을 먼저 살펴보자 

### N-grams

N-grams은 corpus에 존재하지 않는 문장을 count하기 위해 마르코프 가정을 사용한다 

가령 "A good boy" 다음 "is"가 나올 확률을 그냥 "boy"다음 "is"가 나올 확률로 가정하는 것이다
즉, 단어 등장 확률을 구하기 위해 기준 단어의 앞 단어를 전부 포함하는 것이 아닌 앞 단어 중 임의의 N개만 포함하여 세는 것이 N-grams이다 하지만 P(W)=0인 상황을 완전히 피할 수는 없다

따라서 이를 해결하기 위한 기법으로  `smoothing`이 있다 
이 기법은 추후에 나올 Naive Bayes(나이브 베이즈) 알고리즘에서도 주로 쓰인다 수식은 다음과 같다

![image](https://user-images.githubusercontent.com/80239748/150542519-8c5e1420-e440-44fa-93af-1b41ec6df6ac.png)

여기서 alpha가 1이면 Laplace smoothing이다

## Representation

NLP 관련 논문을 읽으면 빠짐 없이 아오는 용어로 실제 텍스트를 LM이 연산할 수 있도록 만든 형태라고 보면 된다 Representation은 크게 카운트 기반으로 나타내는 것과 그렇지 않은 것으로 나눌 수 있다 

### One-hot Encoding

데이터를 처리하기 위해서 벡터 형태로 변환해야 하고 각 데이터가 독립적이어야 할 때 사용한다 

예로 특정 사람의 이미지를 보고 성별을 구별해야 한다고 합시다 
남자를 1로 여자를 0으로 카테고리화 하면 두 카테고리 사이에는 남성이라는 값이 여성보다 크다고 관계가 만들어집니다 

이렇게 되면 학습이 잘안 되기 때문에 독립적인 관계를 만들어야 합니다 

[방법]
단순하게 말하면 카테고리 수를 열의 개수로 하는 **sparse matrix(희소행령)**를 생성하면 된다
물론 약간의 전처리 과정이 필요하다 예로 "I am a boy"라는 문장을 인코딩해보다 

|단계|결과|
|-------|------|
|1. Tokenization(토큰화)|[ "I", "am", "a", "boy" ]|
|2. 각 단어에 고유 인덱스 부여 (사전 생성)|[ "I": 1, "am": 2, "a": 3, "boy": 4 ]|
|3.one-hot encoding|[ [ 1, 0, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 0, 1 ] ]|

위와 같이 4x4의 sparse 행렬을 얻을 수 있다

[한계]
엄청나게 많은 종류의 단어를 one-hot 벡터로 만든다고 하면 엄청난 크기의 행렬이 필요할 것이다 
또한 sparse 행렬이므로 많은 메모리가 낭비된다 그렇기 때문에 다차원 공간에 단어의 의미를 벡터화하는 여러 기법들이 존재한다 