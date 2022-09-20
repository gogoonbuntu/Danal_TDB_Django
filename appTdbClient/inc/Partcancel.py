from django.http import HttpResponse
from . import functions

#################################
#
# �ŷ��� ���� ID �� TID�� ���� �κ� ��ҵ˴ϴ�.
# 
# CAMT : ����� �ݾ�
# RAMT : ��� �� ���� �ݾ�
# CAMT + RAMT ����� �� �ݾװ� ����ġ �� ���� �߻� (893 �����ڵ�)
#
# �Ź� �κ���� �� ���ο� TID �� �����˴ϴ�.
# ���ο� TID �� �ٽ� �κ���Ҹ� �õ��ؾ� �մϴ�.
# 
# �κ���� �ּұݾ��� 1�� �Դϴ�.
# 
# �κ���� ������ �ܾ��� 0���� �ÿ� �κ���Ұ� �ƴ� ��ü��� ������ ����ؾ� �մϴ�
#
#################################


def partcancel(request):
    TransData = dict()
    
    TransData['ID'] = functions.ID
    TransData['PWD'] = functions.PWD
    TransData['COMMAND'] = "PARTCANCEL"
    TransData['OUTPUTOPTION'] = "3"
    TransData['IP'] = "trans.teledit.com"
    TransData['PORT'] = "13005"
    
    TransData['TID'] = "YYMMDDHHmmssXXXXX2" # 18�ڸ� �ŷ���ȣ
    TransData['CAMT'] = "100"
    TransData['RAMT'] = "900"
    
    
    Res = functions.CallTeledit(TransData, False)
    print("RES=> ", Res)
    
    if (Res['Result'] is '0'):
        return HttpResponse('Success\n'+functions.Map2Str(Res))
    else:
        return HttpResponse('Error\n'+functions.Map2Str(Res))
