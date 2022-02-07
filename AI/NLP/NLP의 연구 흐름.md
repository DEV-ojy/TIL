# 자연어 처리 (NLP)의 연구 흐름 정리

## 서론 

https://ratsgo.github.io/natural%20language%20processing/2017/08/16/deepNLP/

이 블로그를 보고 흐름을 정리하신 

https://kingtae.tistory.com/entry/%EC%9E%90%EC%97%B0%EC%96%B4-%EC%B2%98%EB%A6%ACNLP%EC%9D%98-%EC%97%B0%EA%B5%AC-%ED%9D%90%EB%A6%84-%EC%A0%95%EB%A6%AC 

이 블로그를 기반으로 작성해 나가겠습니다 

### 1.Embedding 

**NLP 연구에서 핵심이 되는 부분** 이라고 말해도 될 정도로 중요하고 블로그에서도 많이 강조를 한 부분이기도 합니다 

임베딩이란 단어나 혹은 문장이 가지고 있는 상관관계를 벡터의 형태로 그 상관관계가 보존될 수 있게 변형시키는 것을 말합니다 

이미지 러닝의 경우 머신이 이미지를 인식하는 것을 목적으로 하는데 이미지의 경우 그 보이는 외형에 모든 정보가 담겨있습니다 
하지만 NLP의 경우 자연어 처리를 목적으로 하기 때문에 그 문장이나 단어에 섞여있는 속뜼이나 아니면 단어 사이들의 상관관계를 추축해야 하는 과정이 필수적으로 들어가야 합니다 

그에 대한 예로 이미지를 생성하는 머신 러닝의 경우 encoder-decoder과 주축이 되는 모델을 사용합니다 
하지만 NLP의 경우 단어를 직접적으로 input으로 넣어 encode시키기 전 embedding의 과정을 거쳐서 vetor로 변환 시킨후 그다음에 우리가 알고 대표적으로 알고있는 CNN이나 RNN네트워크등을 사용합니다 

![image](https://user-images.githubusercontent.com/80239748/152793888-aedfef79-b8d4-46df-92ac-6e2ef5413b8c.png)

위의 그림의 경우 `I like this movie very much!` 라는 문장을 직접으로 넣는 것이 아니라 d=5인 embedding vector로 변환하는 과정이 포함됩니다 

이때 단어의 수가 7개이므로 matrix의 size는 (7*5)가 됩니다 

https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf 에선 단어의 분산표상을 학습하는 신경 언어모델(neural language model)을 제안했는데 

![image](https://user-images.githubusercontent.com/80239748/152794506-ecb749e5-904d-4fc0-865c-4e73def8bffd.png)
neural language model(2003), 이때 C(i)가 단어의 벡터이다 

그림에서 볼 수 있다 싶이 위의 네트워크는 하나의 단어 벡터를 학습시키기 위해서 그 외의 단ㄴ어에 대한 정보를 모두 사용해서 학습시키므로 비효율적입니다 

그러기에 이후 이를 대처하는 다양한 embedding 방법이 만들어졌는데 단어 임베딩 기법은 바로 continous-bag-of-words(CBOW)와 skip-gram 이다 

고품질의 단어 벡터를 효율적으로 구축하기 위해서 위의 방법들을 제안했습니다 간단하게 설명하자면 중심단어를 기준으로 윈도우를 형성, 그 윈도우 안에 있는 주변 단어들과 중심단어사이의 연관성을 높이는 방향으로 학습을 진행합니다 

이렇게 될 경우 `주변 단어들과의 연관성`을 바탕으로 임베딩이 가능하므로 hot dog와 같은 `숙어를 학습시키는 것이 가능하다는 장점`이 있습니다 

하지만 실제내용이 아닌 주변 단어와의 연관성만을 바탕으로 good과 bad같은 것을 연관성 높게 학습한다는 단점이 있습니다 