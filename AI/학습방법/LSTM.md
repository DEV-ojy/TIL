# LSTM (Long Short-Term Memory) - 장단기 메모리

RNN의 특별한 한 종류로, 긴 의존 기간을 필요로 하는 학습을 수행할 능력을 가지고 있는 **LSTM**이다.

모든 RNN은 nenual network 모듈을 반복시키는 체인과 같은 형태를 하고 있다 기본적인 RNN에서 이렇게 반복되는 모듈 굉장히 단순한 구조를 가지고 있다 

![image](https://user-images.githubusercontent.com/80239748/122632781-f3cdd680-d10f-11eb-84dd-033ba9cadb9e.png)

LSTM도 똑같이 체인과 같은 구조를 가지고 있지만, 각 반복 모듈은 다른 구조를 갖고 있다 단순한 neural network layer 한 층 대신에, 4개의 layer가 특별한 방식으로 서로 정보를 주고 받도록 되어 있다.

![image](https://user-images.githubusercontent.com/80239748/122632767-e0bb0680-d10f-11eb-80a4-a99e67066ef8.png)

위 그림에서 각 선은 한 노드의 output을 다른 노드의 input으로 vector 전체를 보내는 흐름을 나타낸다 분홍색 동그라미는 vector합과 같은 pointwise operation을 나타낸다 노란색 박스는 neural network layer이다 합쳐지는 선은 concatenation을 의미한다 

![image](https://user-images.githubusercontent.com/80239748/122632947-db11f080-d110-11eb-8ae5-32f16f593fe0.png)

## LSTM의 핵심 아이디어 
LSTM의 핵심은 cell state이다 모듈 그림에서 수평으로 그어진 윗 선에 해당한다

Cell state는 컨베이어 벨트와 같아서, 작은 linear interaction만을 적용시키면 전체 체인을 계속 구동시킨다.정보가 전혀 바뀌지 않고 그대로 흐르게만 하는 것은 매우 쉽게 할 수 있다 

LSTM은 cell state에 뭔가를 더하거나 없앨 수 있는 능력이 있다 
이 능력은 gate라고 불리는 구조에 의해서 조심스럽게 제어가 된다

Gate는 정보가 전달될 수 있는 추가적인 방법으로, sigmoid layer와 pointwise 곱셈으로 이루어져 있다 

Sigmoid layer은 0과1 사이의 숫자를 내보내는데, 이 값은 각 컴포넌트가 얼마나 정보를 전달해야 하는지에 대한 척도를 나타낸다.
그값이 0이라면 아무것도 넘기지마라, 값이 1이면 모든것을 넘겨라 라는 뜻이 된다.  LSTM은 3개의 gate를 가지고 있고 이 문들은 cell state를 보호하고 제어한다

