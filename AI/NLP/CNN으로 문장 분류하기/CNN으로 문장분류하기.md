# CNN으로 문장 분류하기 

이번에는 **Convolutional Neural Networks(CNN)**로 문장을 분류하는 방법에 대해 살펴보겠습니다 

https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/

### 자연어 처리에 특화된 네트웨크 구조?

자연언어는 단어나 표현의 등장 순서가 중요한 `sequential data`입니다 아래의 예문을 보면 
> {무거운/\*가벼운/\*큰}침묵
> 침묵이 {\*무겁다}
 
> **Only** I hit him in the eye yesterday. (No one else did)
> I **only** hit him in the eye yesterday. (did not slap him)

`무거운 침묵`은 고정된 형식으로 ‘정적이 흐르는 상태가 매우 심하다’는 뜻의 연어(collocation)으로 쓰입니다 