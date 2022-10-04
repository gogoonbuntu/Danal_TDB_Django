from django.http import HttpResponse
from . import functions

#################################
#
# 거래건 고유 ID 인 TID를 통해 부분 취소됩니다.
# 
# CAMT : 취소할 금액
# RAMT : 취소 후 남은 금액
# CAMT + RAMT 결과가 원 금액과 불일치 시 에러 발생 (893 에러코드)
#
# 매번 부분취소 후 새로운 TID 가 생성됩니다.
# 새로운 TID 로 다시 부분취소를 시도해야 합니다.
# 
# 부분취소 최소금액은 1원 입니다.
# 
# 부분취소 마지막 잔액이 0원일 시엔 부분취소가 아닌 전체취소 전문을 사용해야 합니다
#
#################################


def partcancel(request):
    TransData = dict()
    
    TransData['ID'] = functions.jsonData['ID']
    TransData['PWD'] = functions.jsonData['PWD']
    TransData['COMMAND'] = "PARTCANCEL"
    TransData['OUTPUTOPTION'] = "3"
    TransData['IP'] = "trans.teledit.com"
    TransData['PORT'] = "13005"
    
    TransData['TID'] = "YYMMDDHHmmssXXXXX2" # 18자리 거래번호
    TransData['CAMT'] = "100"
    TransData['RAMT'] = "900"
    
    
    Res = functions.CallTeledit(TransData, False)
    print("RES=> ", Res)
    
    if (Res['Result'] is '0'):
        return HttpResponse('Success\n'+functions.Map2Str(Res))
    else:
        return HttpResponse('Error\n'+functions.Map2Str(Res))