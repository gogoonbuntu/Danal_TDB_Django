# 다날 휴대폰결제 Django Python 연동모듈 (22.05.16)

Django version 2.2.4

Python version 3.7.4

### Django 기본 프로젝트 디렉터리
tdbTestPython

### Django startapp 을 통해 생성된 디렉터리
appTdbClient


## 기본 순서 : Ready - CPCGI ( Confirm - Bill )
Ready : 가맹점 인증, 세션정보 생성

CPCGI : 구매자 신분 확인, 거래건 정보 확인, 거래 발생

## 연동시 변경해야할 사항:

appTdbClient / inc / functions.py
 - ID, PWD 가맹점 고유 아이디 비번
 - AMOUNT 상품 금액

appTdbClient / inc / Ready.py
 - ByPassValue 중 CPCGI, BackURL, Success, BillCancel 등 가맹점 서버 URL 설정
 - CPName 가맹점 이름

appTdbClient / inc / CPCGI.py
 - 성공 / 실패시 렌더링할 페이지 혹은 실행할 기능

appTdbClient / inc / Billcancel.py
 - 취소 거래건의 TID


문의는 CPID, TID, 거래일시 등과 함꼐 tech@danal.co.kr 로 문의주시면 빠르게 처리해드리겠습니다.
