from django.http import HttpResponse
from . import functions

#################################
#
# 거래건 고유 ID 인 TID를 통해 취소됩니다.
#
#################################


def billcancel(request):
    TransData = dict()
    
    TransData['ID'] = functions.ID
    TransData['PWD'] = functions.PWD
    TransData['Command'] = "BILL_CANCEL"
    TransData['OUTPUTOPTION'] = "3"
    
    TransData['TID'] = "YYMMDDHHmmssXXXXX2" # 18자리 거래번호
    
    Res = functions.CallTeledit(TransData, False)
    print("RES=> ", Res)
    
    if (Res['Result'] is '0'):
        return HttpResponse('Success\n'+functions.Map2Str(Res))
    else:
        return HttpResponse('Error\n'+functions.Map2Str(Res))