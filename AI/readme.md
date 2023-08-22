# 알약 객체 분류 AI


## 프로젝트 소개
- 국립 재활원 제 4회 해커톤 본선 진출프로젝트
## 사용방법 
- pip install -r requirement.txt
## AI모델 설계
- 모든 알약은 제조사나 성분에 따라 모두 다른형태를 가진다 이런 알약의 특성을 이용해
- 이미지 분류 AI를 만들어 시력감소나 기억력 감퇴로 약제 구별에 어려움을 격는 취약계층에 도움을 제공한다

## AI모델 제작과정
- 전이학습을 이용한 모델입니다
- resNet-18 아키텍쳐를 사용하였습니다
- 로프민 네프신 펜잘을 3종류를 분류할수있는 AI입니다


## 약제 관련정보 

- 로프민 
http://www.health.kr/searchDrug/result_drug.asp?drug_cd=A11A1660A0057


- 네프신 
https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2014121100005

- 펜잘8시간이알서방정 
https://www.health.kr/searchDrug/result_drug.asp?drug_cd=2013103000013

## 데이터셋 출처
- https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=576
경구약제 이미지데이터
