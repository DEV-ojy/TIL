# PyTorch Lightning이란 무엇인가?

**PyTorch Lightning**는 PyTorch에 대한 High-level 인터페이스를 제공하는 오픈소스 Python라이브러이 이다.

 PyTorch만으로도 충분히 다양한 AI 모델들을 쉽게 생성할 수 있지만 **GPU나 TPU,그리고 16-bit precision, 분산학습 등 더욱 복잡한 조건에서 실험하게 될 경우, 코드가 복잡해진다**

### 따라서 코드의 추상화를 통해, 프레임워크를 넘어 하나의 코드 스타일로 자리 잡기 위해 탄생한 프로젝트가 바로 PyTorch Lightning이다

# 우리가 PyTorch Lightning을 써야하는 이유
라이브러리를 구현해주신 분들이 추천한 Lightning 사용 대상은 다음과 같습니다

* PyTorch를 사용하는 모든 사람

* 딥러닝 연구자들

* 추상화하여 딥러닝 모델을 

* 훈련하고 싶은 사람들

* PyTorch로 딥러닝 모델을 서비스화하는 엔지니어들

먼저 PyTorch Lightning이 매력적인 이유는 코드를 작성하던 기존 PyTorch 사용자들이 더욱 **정돈된 코드 스타일을 갖추게 된다는 점**입니다.
```
# ----------------
# TRAINING LOOP
# ----------------
num_epochs = 1
for epoch in range(num_epochs):

  # TRAINING LOOP
  for train_batch in mnist_train:
    x, y = train_batch

    logits = pytorch_model(x)
    loss = cross_entropy_loss(logits, y)
    print('train loss: ', loss.item())

    loss.backward()

    optimizer.step()
    optimizer.zero_grad()

  # VALIDATION LOOP
  with torch.no_grad():
    val_loss = []
    for val_batch in mnist_val:
      x, y = val_batch
      logits = pytorch_model(x)
      val_loss.append(cross_entropy_loss(logits, y).item())

    val_loss = torch.mean(torch.tensor(val_loss))
    print('val_loss: ', val_loss.item())
```
이러한 코드가 

```
# train
model = LightningMNISTClassifier()
trainer = pl.Trainer()

trainer.fit(model)
```

로 바뀌게 됩니다

여기서 살펴볼 것은 **복잡한 양의 코드 작업이 간단하게 줄었다**라는 것입니다 이 부분이 바로 PyTorch Lightning의 핵심 담겨있습니다

이밖에 PyTorch Lightning 장점은 다음과 같습니다

* 굉장히 유연함
   
    PyTorch Code에 아주 적합한 코드
    Trainer를 다양한 방식으로 Override가능
    Callback System을 통해 추가적인 작업을 할 수 있다 
* 딥러닝 학습시 다뤄야할 부분을 잘 구조화 하였음 
   
    Lightning module
    Trainer
* 다양한 학습 방법
   
    GPU,TPU learning
    16-bit precision
* PyTorch Ecosystem에 속해 있다
   
    엄격한 Testing 과정
    PyTorch 친화적

* 다양한 예제와 풍부한 Documentation
* 많은 contributor들이 존재함 
* 기타등등
