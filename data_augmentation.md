## 이미지 증강 옵션

```py
keras.preprocessing.image.ImageDataGenerator(
    featurewise_center=False, # boolean type
    samplewise_center=False, # boolean type
    featurewise_std_normalization=False, # boolean type
    samplewise_std_normalization=False, # boolean type
    zca_whitening=False, # boolean type
    zca_epsilon=1e-06, 
    rotation_range=0, 
    width_shift_range=0.0,
    height_shift_range=0.0,
    brightness_range=None,
    shear_range=0.0,
    zoom_range=0.0,
    channel_shift_range=0.0,
    fill_mode='nearest',
    cval=0.0,
    horizontal_flip=False,
    vertical_flip=False,
    rescale=None,
    preprocessing_function=None,
    data_format=None,
    validation_split=0.0,
    interpolation_order=1,
    dtype=None
)

```

## 옵션 별 상세 내역

1. featurewise_center
    - 데이터 정규화 옵션으로, **각 이미지 채널(RGB)값의 평균을 산출**하고 각 채널에 일괄적으로 빼줌으로서, **채널 별 평균을 0에 가깝게** 맞춘다.
    - <span style="background-color:#fff5b1;">데이터셋이 비교적 크고, 데이터셋의 전체적인 통계적 특성을 반영하고자 할 때 유용</span>하다

2. samplewise_center
    - 데이터 정규화 옵션으로, **전체 픽셀에 대한 평균을 산출**하고 각 픽셀값에서 빼줌으로서, **이미지 자체의 평균이 0에 가까워지게** 만든다.
    - <span style="background-color:#fff5b1;">데이터셋이 비교적 작고, 각 이미지의 특성을 개별적으로 보정하고자 할 때 유용</span>하다.
    - featurewise, samplewise center의 경우 모두 데이터의 변동(분산)만 학습하게 되어 더 나은 성능을 발휘하게끔 한다.

3. featurewise_std_normalization
    - `featurewise_center` 옵션과 비슷하게, **각 이미지 채널값의 표준편차를 각각 산출**하고 <span style="color: red;"><strong>각 채널에 나눠줌</strong></span>으로서, **채널 별 표준편차를 1에 가깝게** 만든다.
    - 사용하는 시기는 featurewise_center 시기와 똑같다.
    - 사용 시기라고 판단될 때, featurewise_center와 함께 사용하는 것이 좋다.

4. samplewise_std_normalization
    - `samplewise_center` 옵션과 비슷하게, **전체 이미지 채널값의 표준편차를 산출**하고 <span style="color: red;"><strong>모든 픽셀값에 나눠줌</strong></span>으로서, 이미지 자체의 표준편차가 1에 가깝게 만든다.
    - 마찬가지로 사용하는 시기는 samplewise_center와 똑같다.
    - 사용 시기라고 판단될 때, samplewise_center와 함께 사용하는 것이 좋다.

5. zca_whitening
    - **데이터의 공분산을 제거**하여 각 차원 즉, **픽셀 간의 상관관계를 없애고** 데이터를 추가적으로 정규화하는 과정. 
    - <span style="background-color:#fff5b1;">공분산 행렬을 계산하고, 고유값을 분해한 다음 화이트닝 변환을 진행한다.</span>
    - 최종적으로 얻어지는 것은 공분산이 제거된 데이터에 화이트닝 변환이 적용된 행렬이며, 이는 이미지의 각 픽셀 간 상관관계를 제거하여 각 필셀을 독립적으로 학습할 수 있도록 도와준다.

6. zca_epshilon
    - zca_whitening을 진행하는 과정 중 화이트닝 변환을 진행할 때, 작은 고유값에 대한 수치적 안정성을 제공하기 위해 사용한다
    - 기본값으로 설정되어 있는 값으로도 유추할 수 있겠지만, 일반적으로 매우 작은 값을 사용한다.

7. rotation_range
    - **지정하는 값의 각도만큼 회전**시켜, **모델이 다양한 각도에 대해 적응**할 수 있도록 하는 증강 옵션
    - **특정 각도에 의존하지 않게 하기 위해** 사용한다.
    - `rotation_range=30`으로 설정하면 -30도에서 30도까지 <span style="color: red;"><strong>무작위</strong></span>로 회전시킨다.

8. width_shift_range
    - **지정하는 값 만큼 좌우로 이동**시켜, **모델이 다양한 위치에 대해 적응**할 수 있도록 하는 증강 옵션
    - **특정 위치에 의존하기 않게 하기 위해**서 사용한다.
    - `width_shift_range=0.2`로 지정하면 **이미지 너비의 최대 20%까지 좌우로 이동**할 수 있음을 의미하고, `width_shift_range=20`은 **좌우로 20px까지 이동**할 수 있음을 의미한다. 
    - 해당 옵션도 지정하는 값에 대해 무작위로 적용된다.

9. height_shift_range
    - width_shift_range의 수직 버전이다. 설명은 위와 동일하다.

10. brightness_range
    - **지정하는 `[min, max]` 범위 내에서 이미지의 밝기를 조정**하며, **모델이 다양한 조명 조건에 적응**할 수 있도록 하는 증강 옵션
    - `brightness_range=[0.8, 1.2]`로 지정하면 **이미지의 원래 밝기의 80%~120% 사이의 무작위한 값으로 조정**한다.

11. shear_range
    - **지정하는 값 기반 다양한 기울기로 변환**하며, **모델이 왜곡된 형태의 이미지를 학습**할 수 있도록 한다.
    - 이는 **모델이 다양한 형태의 왜곡에도 강건하게 작동**할 수 있도록 도움을 준다.
    - `shear_range=0.2`는 이미지를 최대 20도 각도로 기울인다.

12. zoom_range
    - **지정하는 `[min, max]` 범위 내에서 이미지를 확대 및 축소**하며, **모델이 다양한 크기에 적응**할 수 있도록 한다.
    - 이는 **모델이 특정 크기에 의존하지 않게**끔 도움을 준다.
    - `zoom_range=[0.8, 1.2]`로 지정하면 **이미지의 크기를 80%~120% 비율로 확대**한다.

13. channel_shift_range
    - **지정하는 값의 $\pm$ 범위로 이미지의 색상 채널 값을 무작위로 변환**한다.
    - 이는 **모델이 다양한 색상의 사진에 적응**할 수 있게 한다.
    - `channel_shift_range=50`으로 지정하면 **-50부터 50까지 각 픽셀에 범위 내의 값을 무작위로 더해 변형**시킨다.

14. fill_mode
    - **이미지 변형으로 인해 발생하는 빈 공간을 채우는 방식을 설정**한다.
    - **이미지 변형 시 발생하는 경계의 빈 공간을 처리하는 방법**을 정의하며, **이미지 변형 후의 일관성을 유지**하는 데 도움을 준다
    - 설정값은 총 4개가 존재한다.
        + `constant` : 고정된 값(cval)으로 채운다.
        + `nearest` : 가장 가까운 픽셀 값으로 채운다.
        + `reflect` : 거울에 반전시킨 것 처럼 채운다.
        + `wrap` : 이미지의 반대편 경계 값을 사용하여 채운다.

15. cval
    - <span style="color: red;">fill_mode가 constant로 설정된 경우</span> 채워질 고정 값을 정의하는 옵션
    - 이미지 변형 시 발생하는 빈 공간을 특정 값으로 채워 일관성을 유지한다.
    - `cval=0`으로 지정하면 빈 공간을 검정색으로 채운다.

16. horizontal_flip
    - 이미지를 수평으로 뒤집는 사항에 대한 여부이다. 모델이 특정 방향에 편향되지 않게끔 해준다.
    - 주의사항으로는, 수평으로 뒤집으면 안되는 이미지들에 대해서는 사용 여부에 대해 고려해봐야 한다
        + ex. 표지판 분류 모델 학습 시 좌회전, 우회전이 구분되어야 하는 경우

17. vertical_flip
    - 이미지를 수직으로 뒤집는 사항에 대한 여부이다. 모델이 특정 방향에 편향되지 않게끔 해준다.

18. rescale
    - 이미지를 스케일링한다. 정규화를 통해 모델의 학습을 안정화한다.
    - 일반적으로 픽셀 값을 [0, 1] 사이로 조정하며, `rescale=1./255`로 지정하여 사용한다.

19. preprocessing_function
    - 사용자 정의 전처리 함수를 적용하는 옵션이다.
    - 사용자가 직접 정의한 함수를 기반으로 이미지에 대해 전처리 작업을 수행할 수 있다.

20. data_format
    - 이미지 데이터를 저장하는 형식을 설정하는 옵션이다.
    - 데이터 형식을 설정하여, 이미지 데이터를 올바르게 처리할 수 있게끔 한다.
    - 설정값에는 두 가지가 있다.
        + `channel_first` : 이미지 데이터가 (채널, 높이, 너비) 형식으로 저장된다
        + `channel_last` : 이미지 데이터가 (높이, 너비, 채널) 형식으로 저장된다

21. validation_split
    - 전체 데이터 중 검증 셋으로 분할하는 비율을 의미한다.
    - 훈련 셋이 100장이고, `validation_split=0.2` 로 지정하면 20장을 검증 셋으로 사용한다.

22. dtype
    - 이미지의 데이터 타입을 설정하는 옵션이다.
    - 이미지의 데이터 타입을 설정하여 데이터의 일관성을 유지하고 메모리 사용을 최적화할 수 있다.
    - keras에서는 일반적으로 `float32`를 사용한다.