# 다날 휴대폰결제 Django Python 연동모듈 (22.05.16)

Django version 2.2.4
Python version 3.7.4

## Django 기본 프로젝트 디렉터리
tdbTestPython

## Django startapp 을 통해 생성된 디렉터리
appTdbClient


# 기본 순서 : Ready - CPCGI ( Confirm - Bill )
Ready : 가맹점 인증, 세션정보 생성
CPCGI : 구매자 신분 확인, 거래건 정보 확인, 거래 발생

## 연동시 변경해야할 사항:

appTdbClient / inc / conf.json

가맹점 정보에 맞게 설정하시면 됩니다.
더 자세한 커스텀을 원하시면 inc 디렉터리 속 Ready, CPCGI, functions 위주로 봐주세요.

## 부분취소 사용하시려면
부분취소는 사용하시려면 별도의 등록 절차가 필요합니다.
영업 담당자에게 등록요청 부탁드립니다.


문의는 CPID, TID, 거래일시 등과 함꼐 tech@danal.co.kr 로 문의주시면 빠르게 처리해드리겠습니다.
