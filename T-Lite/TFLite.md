# TFLite 란?

**Tensorflow Lite는 mobile,embedding,iot device에서 모델을 사용할 수 있도록 Tensorflow 모델을 변환해주는 tool 이다**

### 이러한 TFLite의 장점이란? 

1. 서버까지의 왕복이 없어 지연시간이 줄어들고

2. 데이터가 기기를 벗어나지않아 개인정보보호에 탁월하며 

3. 인터넷연결이 필요하지 않습니다 

4. 네트워크 연결에 전력이 필요없어 전력 소비를 낮출수있습니다

이러한 장점을 가지고 있는 TFLite는 아래의 방법으로 사용할 수 있습니다 
```
  PC에서 모델을 학습시킴->학습한 모델을 텐서플로 라이트버전으로 변환->안드로이드 프로젝트 생성->
  assets폴더를 만듦->모델파일을 붙여 넣는다->텐서플로 라이트 모듈을 사용할수 있도록 gradle 파일에 내용추가->
  gradle 파일 수정(모델파일이 압축되지 않게한다)->동기화 진행->tflite 모델 파일로딩->
  run함수호출->결과를 가져옴->안드로이드 화면을 구성하고 코드를 추가해서 결과표시
```

## Tensorflow Lite convert
Keras model을 TFLite model을 변경하는 tool인 Tensorflow Lite convert로 예시를 들어보도록 하겠습니다

**converter=tf.lite.TFLiteConverter.from_keras_model(‘your keras model’)**

위의 함수가 TFLite로 만드는 준비 compile과정이라고 생각하시면 됩니다
그래서 compile setting을 converter변수에 할당합니다

compile이 진행 되었다면 실제로 convert는 다음과 같은 함수로 진행됩니다

**tflite_model=converter.convert()**

compile정보를 담고 있는 converter object에서 convert()함수를 호출 하여
tflite_model변수에 tflite model을 할당하게 됩니다

TFLiteConverter의 입출력 관계는 다음과 같습니다 

![image](https://user-images.githubusercontent.com/80239748/125279231-ab8c8780-e34e-11eb-8a76-ae0e702d0e8b.png)

이 사진의 경우 Keras modell을 입력을 받고 TFLiteConverter를 통과해 tflite확장자를 가진 Flatbuffer형식의 파일을 얻게 됩니다 
Serialized인 Flatbuffer형식이므로 언어에 dependency(의존성) 영향을 받지 않는 모델이 되는 것 입니다 

이는 **다양한 device,mobile에 배치할 수 있음을 암시하는 것입니다**

그럼 이제 train해놓은 keras model을 이용해서 예제 코드를 실행해보겠습니다 (예제 모델:pruned resnet18 on cifar10 )

<pre><code>
def keras2TFlite(model_path):
    #load a pre-trained model
    keras_model =tf.keras.models.load_model(model_path) #model_path is 'cifar10_resnet18_pruned.h5'

    #convert to tflite model
    converter = tf.lite.TFLiteConverter.from_keras_model(keras_model)
    tflite_model = converter.convert()

    #save tflite model
    ext_idx=model_path.rfind('.')
    save_path=model_path[:ext_idx]+'.tflite'
    with open(save_path, "wb") as f:
        f.write(tflite_model)
</code></pre>

TFLite model로 변환했는데 model size가 줄었들었습니다 
역시 TFLite model이 더 최적화되어 있는 듯합니다 그리고 keras model와 tflite model을 netron을 이용해서 visualization한 모습을 비교해보겠습니다

![image](https://user-images.githubusercontent.com/80239748/125281339-10e17800-e351-11eb-9820-5773200a9913.png)

## Operator compatibility

**Tensorflow 에서는 지원하지만 Tensorflow Lite에서는 지원하지 않는 operator가 있습니다**

type측면으로 보면 대부분의 TFLite의 operator들은 float32,uint8,int8을 대상으로 한다고 합니다 그래서 float16또는 strting위한 많은 operator들은 아직이라고 합니다 
