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

### 2.CNN

![image](https://user-images.githubusercontent.com/80239748/152990171-fe3fc990-c757-4954-9775-a4f1bcf38d3e.png)

다음처럼 임베딩을 바탕으로 embedding vector matrix를 얻고 이를 인풋으로 CNN 네트워크를 만듭니다 
이때 max-pooling을 주로 사용하는 것을 알수있는데 이렇게 사용하는 것이 결과가 좋았다고 합니다이미지 러닝에서는 주로 avgpooling을 사용하는데 이는 이미지와 자연어의 차이때문에 아닐까싶습니다 자연어에서는 가장 높은 값을 가지는 value가 그 추상성을 대표하는 값이 된다고 합니다 

아마 이미지에서는 모든 값들을 대표할 수 있는 값을 담는것이 그 이미지를 대표하는 대표적인 값이라서 그런것이 아닐까 생각합니다 

### 3.RNN

RNN은 recurrent neutral network의 줄임말로써 연속적으로 들어오는 정보의 나열을 학습하기 위한 네트워크 구조로 주로 사용됩니다 ex.차례대로 들어오는 음성이나 문장 

RNN의 경우 아웃풋의 크기를 지정해줘야 하는 CNN에 비해 output을 연속적으로 출력하는 것이 가능하므로 RNN은 크기가 정해지지 않은 출력을 얻는데 적합합니다 

![image](https://user-images.githubusercontent.com/80239748/153714575-b94572ce-eb3e-4768-9454-2fbe1743338f.png)

time step으로 들어오는 input에 따라 output을 만들고 그전에서 얻은 hidden state를 그다음 RNN layer의 인풋으로 사용해서 그전에 들어온 문장의 숨은 특성을 네트워크가 학습시키게 할 수 있습니다 

기본적인 RNN보다 LSTM이나 GRU를 사앙해서 state의 forget circuit를 구현하게 될 경우 그 성능이 더 높은 것으로 알려져 있습니다 