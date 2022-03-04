# MLOps와 DevOps 이해하기

DevOps와 MLOps에서 말하는 CI/CD/CT의 개념을 비교하여 MLOps에서 목표하는 바를 이해해보려고 합니다 

### DevOps와 MLOps
MLOps, AIOps, 또는 ML ML Infrastucture 등 다양한 이름으로 불리는 이 개념은 기존 소프트웨어의 개발 및 배포에서 사용하던 DevOps와 함께 언급이 됩니다 

### DevOps: Dev + Ops

**Dev(Development)와 Ops(Operations)**

소프트웨어 개발 및 배포 파이프라인 전반에 걸쳐 개발 조직과 운영조직 간의 협업을 통해 소프트웨어 제품과 서비스를 빠른 시간에 개발 및 배포하는 것을 목표로 합니다 

![image](https://user-images.githubusercontent.com/80239748/153714479-27632b67-ffb7-4252-aa7e-15269c5807a6.png)

### MLOps: ML + Ops

**ML(Machine Learning)과 Ops(Operations)**

ML 모델 서빙 파이프라인 전반에 걸쳐 Scientist와 Engineer의 협업을 통해 모델을 정확하고 안정적으로 서빙하는 것을 목표로 합니다 

![image](https://user-images.githubusercontent.com/80239748/153714512-9849ba3f-b6b7-4565-b189-d5cdb0165a40.png)

### DevOps 와 MLOps에서 CI/CD/CT

DevOps 와 MLOps에서 CI/CD, 그리고 CT의 개념은 조금 다르게 설명이 됩니다 
지향하는 목표는 대체로 유사하지만 그 방법과 특성에서 조금 차이가 있습니다 

#### CI/CD/CT in DevOps 

DevOps에서 일반적으로 말하는 CI/CD와 CT는 다음과 같습니다 

##### [1] CI: Continuous Integration(지속적 통합)

DevOps에서 CI는 소프트웨어의 새로운 변경 사항에 대해 Build 및 Test를 거쳐 Shared Repository에 통합하는 프로세스를 지속적으로 실시하는 것을 의미합니다 

다수의 개발자가 Git,Bitbucket 등 형상관리 툴을 공유하여 사용하면서 다수의 개인이 commit을 시도하는 환경이나 Agile 방법론의 톡성에 따라 기능의 수정 및 추가가 비번하게 시도되는 MSA환경에서는 소스코드의 충동 문제가 빈번하게 발생합니다 

이러한 **문제를 빠르게 해결하고,새로운 업데이트의 검증과 릴리즈 시간을 단축하여 소프트웨어 품질을 향상하는 것을 목표**로 합니다 

##### [2] CD:Continuous Delivery/Deployment(지속적 제공/배포)

DevOps에서 CI가 Build-Test-Integration 과정에서의 지속성을 의미한다면, `CD`는 **Shared Repository에서 병합된 소스 코드를 Production 환경에 릴리스하는 과정**에서의 `지속성`을 의미한다

특히 짧은 주기로 소프트웨어를 개발하고 배포하는 경우, **더 빠른 주기로 출시하면서도 항상 신뢰할 수 있는 수준으로 출시할 수 있도록 보증**하기 위한 전략이다

릴리즈 방식에 있어 Manual하게 배포하는 경우에는 Continuous Delivery라고 하고 
Automatic 하게 배포하는 경우에는 Continuous Deployment라고 한다

![image](https://user-images.githubusercontent.com/80239748/156780198-43c746ca-687d-4ab4-b3da-bc04314ad239.png)

##### [3] CT: Continuous Testing (지속적 테스트)

