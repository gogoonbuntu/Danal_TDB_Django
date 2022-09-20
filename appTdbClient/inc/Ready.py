from django.http import HttpResponse
from . import functions

CHARSET = functions.jsonData['IsCharSet']
ID = functions.jsonData['ID']
PWD = functions.jsonData['PWD']
CPName = functions.jsonData['CPName']
ItemName = functions.jsonData['ItemName']
ItemAmt = functions.jsonData['ItemAmt']
ItemCode = functions.jsonData['ItemCode']
ItemInfo = ItemCode[0] +'|'+ str(ItemAmt) +'|1|'+ ItemCode +'|'+ ItemName
serverAddr =functions.jsonData['serverAddr']

def ready(request):
    TransData = dict()
    
    #########################################
    # 아래 데이터는 고정값입니다. 변경하지 마세요 #
    #########################################
    
    TransData['COMMAND'] = 'ITEMSEND2'
    TransData['SERVICE'] = 'TELEDIT'
    TransData['ItemCount'] = '1'
    TransData['OUTPUTOPTION'] = 'DEFAULT'
    
    
    #########################################
    # ID : 다날에서 제공해드린 ID ( function 파일 참조)
    # PWD : 다날에서 제공해드린 PWD ( function 파일 참조)
    # CPName : 가맹점 이름
    # ItemCode : 다날에서 제공해드린 ItemCode
    #########################################
    
    TransData['ID'] = ID
    TransData['PWD'] = PWD
    TransData['CPName'] = CPName
    TransData["ITEMINFO"] = ItemInfo
    
    # 선택 사항
    # SUBCP : 다날에서 제공해드린 SUBCP
    # USERID : 사용자 USERID
    # ORDERID : CP 주문번호
    # IsPreOtbill : Authkey 수신 유무 (Y/N) 재승인, 월자동결제 등을 위한 Authkey 수신이 필요한 경우 Y
    # IsSubscript : 월 정액 가입 유무 (Y/N) 월 정액 가입을 위한 첫 결제인 경우 Y
    
    # TransData['SUBCP'] = functions.jsonData['SUBCP']
    # TransData['USERID'] = functions.jsonData['USERID']
    # TransData['ORDERID'] = functions.jsonData['ORDERID']
    # TransData['IsPreOtbill'] = functions.jsonData['IsPreOtbill']
    # TransData['IsSubscript'] = functions.jsonData['IsSubscript']
    
    # CPCGI 에 HTTP POST 로 전달되는 데이터
    
    ByPassValue = dict()
    
    ByPassValue["BgColor"] = "00"
    #ByPassValue["TargetURL"] = "http://localhost:8000/CPCGI"
    ByPassValue["TargetURL"] = serverAddr + functions.jsonData['TargetURL']
    ByPassValue["BackURL"] = serverAddr + functions.jsonData['BackURL']
    ByPassValue["IsUseCI"] = functions.jsonData['IsUseCI']
    ByPassValue["CIURL"] = functions.jsonData['CIURL']
    
    ByPassValue["Email"] = functions.jsonData['Email']
    ByPassValue["IsCharSet"] = functions.jsonData['IsCharSet']
    
    ByPassValue["ByBuffer"] = functions.jsonData['ByBuffer']
    ByPassValue["ByAnyName"] = functions.jsonData['ByAnyName']
    
    Res = functions.CallTeledit(TransData, True);
    
    if( Res['Result'] == "0"):
        Out = """
        <head>
        <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
        <meta http-equiv="Content-Type" content="text/html; charset=euc-kr" />
        </head>
        <body>
            <form name="Ready" action="https://ui.teledit.com/Danal/Teledit/Web/Start.php" method="post">
                """ + functions.MakeFormInput(Res, ["Result", "ErrMsg"]) + functions.MakeFormInput(ByPassValue) + f"""
                <input type="hidden" name="CPName"      value="{CPName}">
                <input type="hidden" name="ItemName"    value="{ItemName}">
                <input type="hidden" name="ItemAmt"     value="{ItemAmt}">
                <input type="hidden" name="IsPreOtbill" value="N">
                <input type="hidden" name="IsSubscript" value="N">
                <input type="hidden" name="IsCharSet"   value="euc-kr">
            </form>
            <script Language="JavaScript">
                document.Ready.submit();
            </script>
        </body>

        """
        
        #return HttpResponse(Out, content_type='application/json; charset=utf-8')
        return HttpResponse(Out, content_type='text/html; charset=euc-kr')
    else :
        Result = Res['Result']
        ErrMsg = Res['ErrMsg']
        AbleBack = False;
        BackURL = ByPassValue['BackURL']
        IsUseCI = ByPassValue['IsUseCI']
        CIURL = ByPassValue['CIURL']
        BgColor = ByPassValue['BgColor']
        
        
    return HttpResponse(Result+" "+ErrMsg)