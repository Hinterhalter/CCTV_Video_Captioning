# CCTV_Video_Captioning
Video captioning project using deep learning models. 

## 프로젝트 활동 일지
----------------------------------------------
### 20.1.29
- ECO: Efficient Convolutional Network for Online Video Understanding
- (https://paperswithcode.com/paper/eco-efficient-convolutional-network-for)
- 저자 깃허브 주소 (https://github.com/mzolfaghari/ECO-efficient-video-understanding)
- 논문 1차 리딩 완료, 주요 개념 학습 중
- 깃허브 코드 실행을 해보려고 했으나 오류 발생
#### issue :
- 영상을 모델에 넣기 위해서는 통째로 넣는 것이 아니라 N개의 샘플로 나누어서 학습을 시켜야 함
- 영상을 프레임 단위로 나눌 수 있는 코드가 (https://github.com/yjxiong/temporal-segment-networks#extract-frames-and-optical-flow-images)에 있으나 make과정에서 'E: Unable to locate package libboost1.55-all-dev' 오류 발생
- 프레임 추출 대신 우선 본 코드를 다시 실행해보려고 했으나 pre-train 파일이 없어서 막힘.

----------------------------------------------

Reference
----------------------------------------------
|#|title|source|note|
|:----:|:-----|:-------|:------|
|1|[ECO: Efficient Convolutional Network for Online Video Understanding](#국가건강검진-건강위험평가-개선-참고-페이지)|질병관리본부|health_data 변수 전처리 참고, 심뇌혈관질환 위험도 계산|
|2|국가중점개방데이터 사용자 매뉴얼(ver4.0)|국민건강보험공단 빅데이터운영실|health_data 변수 파악|
