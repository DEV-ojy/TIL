# TensorFlow Lite

TensorFlow Lite는 TensorFlow 모델을 휴대폰, embedded 나 IOT 기기에서 구동하기 위해서 ML 툴입니다 
Mobile과 IOT 기기를 위해서 TensorFlow를 경량화 시킨 버전이라고 생각하면 됩니다 
Mobile과 IOT 기기를 위한 만큰 빠른 응답 속도와 작은 바이너리 사이즈가 특징이다

## 1. Edge ML(Machine learning at the edge)

엣지 컴퓨팅(Edge Computing)은 서로 다른 위치에서 가끔씩 클라우드에 연결하거나 클라우드에 전혀 연결하지 않고 컴퓨팅 리소스 및 의사 결정 기능을 활용하는 기술을 말합니다 

보통 ML을 상상하면 클라우드에 존재하는 GPU와 TPU가 무수히 연결된 서버를 생각하게 됩니다 
지 ML(Edge ML)은 이런 클라우드가 아닌 각 단말 단에서 활용되는 ML 기술을 표현할 때 사용됩니다 특히, Edge ML에서의 단말은 통상 Mobile과 IOT등의 작은 컴퓨팅 파워를 가진 디바이스들을 말합니다 

이런 Edge 단에서 수행되는 ML은 아래와 같은 장점을 가집니다 

1. 짧은 응답속도(latency) : ML inference 수행 시, 클라우드 서버에 접근이 없이 단말에서 수행하므로 응답속도가 빠릅니다

2. 개인 정보 보호 : 클라우드 서버에 개인 정보를 전달하지 않아서 privacy 노출 위험이 없습니다

3. 네트워크 불필요 : 클라우드 서버에 접근이 불필요하기 때문에 네트워크 망에 연결될 필요 없습니다

4. 낮은 소비 전력 : 네트워크 연결을 위한 전력 소모가 없으며, 작은 사이즈의 모델 구동으로 컴퓨팅 전력 소모 적습니다

이러한 특징을 갖는 `Edge ML`을 위한 **툴이 TensorFlow Lite**이다