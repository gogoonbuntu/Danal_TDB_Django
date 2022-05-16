from django.http import HttpResponse

from . import functions

def cpcgi(request):
    BillErr = False
    TransData = dict()
    ServerInfo=""
    
    if(request.method == 'POST'):
        ServerInfo = request.POST["ServerInfo"]
        
    nConfirmOption = 1
    TransData["Command"] = "NCONFIRM"
    TransData["OUTPUTOPTION"] = "DEFAULT"
    TransData["ServerInfo"] = ServerInfo
    TransData["IFVERSION"] = "V1.1.2"
    TransData["ConfirmOption"] = str(nConfirmOption)

    if (nConfirmOption == 1):
        TransData['CPID'] = functions.ID
        TransData['AMOUNT'] = str(functions.AMOUNT)

    Res = functions.CallTeledit(TransData, False)

    if(Res['Result'] is "0"):
        TransR = dict()

        nBillOption = 0
        TransR["Command"] = "NBILL"
        TransR["OUTPUTOPTION"] = "DEFAULT"
        TransR["ServerInfo"] = ServerInfo
        TransR["IFVERSION"] = "V1.1.2"
        TransR["BillOption"] = str(nBillOption)

        Res2 = functions.CallTeledit(TransR,False)

        if( Res2["Result"] != "0" ):	
            BillErr = True

        if (Res['Result']=='0' and Res2['Result']=='0'):
            ##################################
            # 결제 성공에 대한 작업
            ##################################
            return HttpResponse('Success!\n'+functions.Map2Str(TransR)+functions.Map2Str(Res2))
        else:
            ##################################
            # 결제 실패에 대한 작업
            ##################################
            return HttpResponse('Error!!!\n'+functions.Map2Str(TransR)+functions.Map2Str(Res2))
        
    else: 
        ##################################
        # CONFIRM 단계 실패
        ##################################
        return HttpResponse(Map2Str(Res))
        