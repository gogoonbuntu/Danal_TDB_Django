from django.http import HttpResponse
from . import functions


def ready(request):
    TransData = dict()
    
    #########################################
    # 아래 데이터는 고정값입니다. 변경하지 마세요 #
    #########################################
    
    TransData['Command'] = 'ITEMSEND2'
    TransData['SERVICE'] = 'TELEDIT'
    TransData['ItemCount'] = '1'
    TransData['OUTPUTOPTION'] = 'DEFAULT'
    
    
    #########################################
    # ID : 다날에서 제공해드린 ID ( function 파일 참조)
    # PWD : 다날에서 제공해드린 PWD ( function 파일 참조)
    # CPName : 가맹점 이름
    #########################################
    
    TransData['ID'] = functions.ID
    TransData['PWD'] = functions.PWD
    CPName = 'CP이름'
    
    # ItemAmt : 결제 금액 (실제 상품금액 처리시엔 Session 또는 DB 를 사용해주세요. 위변조의 위험이 있습니다.)
    # ItemName : 상품명
    # ItemCode : 다날에서 제공해드린 ItemCode
    
    ItemAmt = '301'
    ItemName = '승몽꿩삵횃불싹쐐기!@#'
    ItemCode = '22S0Vs0001'
    ItemInfo = functions.MakeItemInfo( ItemAmt, ItemCode, ItemName )
    TransData["ITEMINFO"] = ItemInfo
    
    # 선택 사항
    # SUBCP : 다날에서 제공해드린 SUBCP
    # USERID : 사용자 USERID
    # ORDERID : CP 주문번호
    # IsPreOtbill : Authkey 수신 유무 (Y/N) 재승인, 월자동결제 등을 위한 Authkey 수신이 필요한 경우 Y
    # IsSubscript : 월 정액 가입 유무 (Y/N) 월 정액 가입을 위한 첫 결제인 경우 Y
    
    TransData['SUBCP'] = ""
    TransData['USERID'] = "USERID"
    TransData['ORDERID'] = "ORDERID"
    TransData['IsPreOtbill'] = "N"
    TransData['IsSubscript'] = "N"
    
    # CPCGI 에 HTTP POST 로 전달되는 데이터
    
    ByPassValue = dict()
    
    ByPassValue["BgColor"] = "00"
    #ByPassValue["TargetURL"] = "http://localhost:8000/CPCGI"
    ByPassValue["TargetURL"] = "https://tdbdjango.run.goorm.io/CPCGI"
    ByPassValue["BackURL"] = "http://localhost:8000/BackURL"
    ByPassValue["IsUseCI"] = "N"
    ByPassValue["CIURL"] = "http://localhost/Danal/Teledit/images/ci.gif"
    
    ByPassValue["Email"] = 'user@cp.co.kr'
    ByPassValue["IsCharSet"] = ""
    
    ByPassValue["ByBuffer"] = "This Value bypass to CPCGI page"
    ByPassValue["ByAnyName"] = 'Any Value '
    
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
                <input type="hidden" name="IsPreOtbill" value="{TransData['IsPreOtbill']}">
                <input type="hidden" name="IsSubscript" value="{TransData['IsSubscript']}">
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