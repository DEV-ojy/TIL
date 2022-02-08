# Embedding 개념

## 임베딩(Embedding)이란?

자연어 처리에서 임베딩이란, 일반적으로 사람들이 쓰는 언어를 기계가 알아들을 수 있게 수치화하는 것으로 단어나 문장을 `벡터 공간에 끼워 넣는다`라는 의미를 가지고 있습니다  

임베딩을 통해 가능해진 것 
* 단어나 문장 사이의 유사도 계산
코사인 유사도가 가장 높은 단어를 구하는 등의 계산 가능
(+ t-SNE 차원 축소 기법으로 시각화 가능)

* 단어들 사이의 의미/문법적 정보 도출
벡터 간 연산으로 단어 사이 문법적 관계 도출
(평가 방법으로는 단어 유추 평가(word analogy test)가 있음)

* 전이 학습(transfer learning)
다른 딥러닝 모델의 입력값으로 사용 

임베딩의 변천사 

|과거|현재|
|:-----:|:----:|
|LSA(잠재 의미 분석, Latent Semantic Analysis) tf-idf 등의 행렬을 특이값 분해 등을 통해 차원 축소 corpus 통계량을 직접적으로 활용|Neural Network 기반 임베딩 기법|
|단어 수준 임베딩 모델 NPLM, Word2Vec, GloVe, FastText, Swivel단점) 동음이의어 분간하기 어려움|문장 수준 임베딩 모델ELMo, BERT, GPT 단어 sequence 전체의 문맥적 의미 함축|
|End-to-End 모델sequence-to-sequence 모델|Pretrain & Fine Tuning corpus 통해 임베딩을 만들어 의미, 문법적 맥락이 포함되게 한 뒤(pretrain), 모델 업데이트(fine tuning)|

```
Downstream & Upstream Task
Downstream Task
- 일반적인 NLP task
- 품사 판별, 시맨틱 태깅(NER, NED)
Upstream Task
- 임베딩을 pretrain하는 작업
- 임베딩 품질이 좋아야 모델이 좋아짐
```

임베딩의 종류 

* 행렬 분해 기반 방법
행렬을 쪼개는 방식 (GloVe, Swivel)

* 예측 기반 방법
특정 단어 예측 (Word2Vec, FastText, BERT, ELMo, GPT)

* 토픽 기반 방법
문서가 내포하고 있는 주제를 추론하는 방식 (LDA)