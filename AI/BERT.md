# BERT : Bidirectional Encoder Representations form Transformer 

b는 기본적으로 wiki나 bookdata와 같은 대용량 unlabeled data로 모델을 미리 학습 시킨 후 → 특정 task를 가지고 있는 
labeled data로 transfer learning을 하는 모델입니다 

bert이전에 이러한 접근 방법을 가지는 모델이 있었는데 
대용량 unlabeld corpus(무표본 말뭉치)를 통한 언어모델을 학습하고  이를 토대로 뒤쪽의 특정 task(과제)를 처리하는 network를 붙이는 방식 
(ELMo,OpenAI GPT)이 있었습니다 

하지만 이전의 모델의 접근 방식은 shallow bidirectional(얕은 양방향의)또는unidirectional(단방향의) 하므로 
language representation(언어표현)이 부족하다고 표현하였습니다 
BERT는 특정 task를 처리하기 위해 새로운 network를 붙일 필요가 없습니다
모델 자체의 fine-tuning(미조정)을 통해 해당 task의 state-of-the-art(최신)를 달성하게 됩니다 

## Introduction
bert는 기본적으로 두가지 pre-training 방법을 가지고 있다 하나는 Masked Language Model(MLM)이고
다른하나는 Next Sentence Prdiction(NSP)이다 

기존의 방법론은 앞의 n개의 단어를 가지고 뒤의 단어를 예측하는 벙법이다 하지만 이는 필연적으로 
unidirectional(단방향)일수밖에 없다 이를 극복하기 위해 ELMo에서 Bi-LSTM으로 양방향성을 가지려고 노력할수밖에 없다

MLM은 input에서 무작위하게 몇개의 token을 mask시킨다음 이를 transformer구조에 넣으면 주변 단어의 context만을 보고
mask된 단어를 예측하는 방법이다 GPT도 Transformer구조를 사용하지만 앞단어들만 보고 뒷단어를 예측하는 transformer decoder구조를 사용

Next Sentence Prediction : 간단하게 두 문장을 pre-training시에 같이 넣어서 두문장이 이어지는 문장인지 아닌지를 맞추는 것이다

## bert
```
BERT의 아키텍처는 Attention is all you need에서 소개된 Transformer를 사용하지만, 
pre-training(사전훈련)과 fine-tuning(미세조정)시의 아키텍처를 조금 다르게 하여 
Transfer Learnin을 용이하게 만드는 것이 핵심이다 
```

## Model Architecture

bert는 transformer중에서도 encoder부분만 사용한다 모델의 크기에 따라 base모델과 large모델을 제공

```
- **BERT_base** : L=12, H=768, A=12, Total Parameters = 110M
- **BERT_large** : L=24, H=1024, A=16, Total Parameters = 340M
- L : transformer block의 layer 수, H : hidden size, A : self-attention heads 수, 
feed-forward/filter size = 4H
```
Open AI GPT 모델의 경우 next token만을 맞추어내는 긱본적인 언어모델방식을 사용하기 위해 transformer decoder를 사용합니다
하지만 bert는 MLM과 NSP를 위해 self-attention을 수행하는 transformer encoder 구조를 사용합니다 

## bert의 Input Representation

![image](https://user-images.githubusercontent.com/80239748/133095830-ef00eb75-6705-4b7c-b03b-500ecd40794c.png)

bert의 input은 3가지의 embedding값의 합으로 이루어져있습니다 

모든 Sentence의 첫번째 token은 언제나 CLS입니다 
이는 CLS token은 transsformer 전체층을 다 거치고 나면 token sequence의 결합된의미를 가지게 되는데 여기서 간단한 classifier를
붙이면 단일 문장 또는 연속된 문장의 classification을 쉽게 할수있게됩니다 만약, classification task가 아니라면 token은 무시가능합니다

Sentence pair은 합쳐져서 single sequence로 입력되게 됩니다 각각의 Sentence는 실제로는 수개의 Sentence로 이루어져 있을수있습니다

그래서 두개의 문장을 구분하기 위해 첫째로는 sep token사용하는것과 둘째로는 segment embedding을 사용하여 앞의 문장에는
sentence A embedding, 뒤의 문장에는 sentence B embedding을 더 해줍니다 
만약 문장이 하나만 들어간다면 sentence A embedding만 해줍니다 

## MLM의 작동원리 

![image](https://user-images.githubusercontent.com/80239748/133097974-63af14e8-47c1-47df-9af7-5dfedda0f2b1.png)

단어중 일부를 MASK token으로 바꾸어 줍니다 바꿔주는 비율은 15%입니다 그리고 plain text를 tokenization하는 방법은 WordPiece를 사용합니다
이를 통하여 LM의 L2R(혹은R2L)를 통하여 문장 전체를 predict하는 방법론과는 달리 MASK token만을 predict하는 pre-training을 수행합니다 

MASK token은 pre-training에만 사용되고 fine-tuning시에는 사용되지 않습니다 해당 token을 맞추어 내는 task를 수행하면서 
bert는 문맥을 파악하는 능력을 길러냅니다

또한 MLM은 보통의 LM보단 converge 하는데에 많은 training step이 필요하지만 emperical하게는 LM보다 훨씬 빠르게 좋은 성능을 냅니다

## Next Sentence prediction

pre-training task 수행하는 이유는 여러 중요한 NLP task중에 QA나 Natural Language Inference(NLI)와 같이 
두 문장 사이의 관계를 이해하는 것이 중요한 것들이기 때문에 이들은 언어 모델에서 capture되지 않습니다

그래서 BERT에서는 corpus에서 두문장을 이어 붙여 이것이 원래의 corpus에서 바로 이어 붙어져 있던 문장인지를 
맞추는 binarized next sentence prediction task(이진화된 다음 문장 예측 작업)를 수행합니다

pre-training이 완료되면 이 과제는 97~98%의 accuracy(정확도)를 달성하게 됩니다 
간단한 task를 부여해도 QA와 NLI에 굉장히 의미있는 성능 향샹을 이룹니다 

## pre-training Procedure

pre-training의 기본적인 절차는 LM에서 수행하는 것과 같습니다 

- input pre-processing

    NSP를 위해 sentence를 뽑아서 embedding A,B를 먹여줍니다 물론 50%는 진짜 NS를 나머지는 RN를 사용 

    이후에 Masking 작업을 해줌
    

## Fine-tuning Procedure

- sequence-level classification tasks(순서 수준 분류 작업)에 대해서는 BERT fine-tuning과정이 매우straightforward(직설적인)

    input sequence에 대해서는 representation(대표)결과를 얻고 싶기 때문에 CLS token의   Transformer output값을 사용합니다 

    CLS token의 벡터는 H 차원을 가집니다 

    여기서 classify하고 싶은 갯수(K)에 따라 classification layer를 붙여줍니다

- span-level, token-level prediction tasks(범위 수준, 토큰 수준 예측 작업)의 경우에는 위의 과정에서 약간 변형시켜 fine-tuning이 진행합니다

- fine-tuning시의 Hyper-Parameter

    몇가지를 제외하고는 pre-training때의 hyper parameter와 대부분 동일합니다.

    다른점은 **batch size, learning rate, trainig epochs 수** 입니다.

    **optimal hyperparameter**는 **task마다 달라지지만**, 다음에 제시하는 것을 사용하면 대부분 잘 학습됩니다.

- fine-tuning시의 **dataset의 크기가 클수록** hyperparameter에 **영향을 덜 받고 잘 training 됨**을 관측할 수 있었다고 합니다.
- **Fine-tuning**은 굉장히 빠르게 학습되며(pre-training에 비해) 이로 인해 최적의 hyperparameter 탐색을 exhaustive search로 찾아내도 무방합니다


## Comparison of BERT and OpenAI GPT

OpenAI GPT와 BERT는 transformer구조를 사용한다는 점에 있어서 공통점을 갖지만 BERT가 훨씬 좋은 성능을 가진다 
이차이는 앞에 설명한 MLM task,NSP task를 수행하는 것과 별개로 또 더 다른점을 갖기에 생깁니다

 **GPT**의 경우 **BookCorpus(800M words)** 만을 pre-training에 사용 **BERT**는 거기에 + **Wikipedia(2500M words)** 사용
 **GPT**는 `[SEP]`과 `[CLS]` token을 fine-tuning시에만 추가하여 학습; **BERT**는 pre-training시에도 학습 **(NSP task가 존재하기 때문에 가능)**
 **GPT** : 32,000 words/batch for 1M steps ; **BERT** : 128,000 words/batch ofr 1M steps
 **GPT**는 모든 fine-tuning을 수행할 때 learning rate : 5e-5를 사용; **BERT**는 **task-specific**하게 조절하여 사용

    위에 나열한 차이점에서 대한 효과는 ablation experiments(절제 실험)이 수행합니다
