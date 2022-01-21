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

