import os
import subprocess
from urllib import parse
import locale
import requests
import json

#############################################
#
# SClient가 설치된 다날 WEB GW 를 호출입니다. POST 형태의 문자열로 데이터를 받습니다.
#
#############################################

with open(os.path.join(os.getcwd(), 'appTdbClient', 'inc','conf.json')) as f:
    jsonData = json.load(f)
    
if jsonData['Debug'] : print(jsonData)

ID = jsonData['ID']
PWD = jsonData['PWD']
AMOUNT = jsonData['ItemAmt']



def CallTeledit(TransData, Debug=False):

    #headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    #arg=MakeParam(TransData).encode('euc-kr')
    #Output = requests.post('https://ui.teledit.com/Danal/TGW/request.php', headers=headers, data=arg)
    
    TeleditBinPath = jsonData['TeleditBinPath']
    Bin="/SClient"
    arg=MakeParam(TransData)
    Input = TeleditBinPath+Bin+" \""+arg+"\""
    #Output = os.popen(Input).read()
    Output = subprocess.Popen(["/bin/bash", "-c", Input], stdout=subprocess.PIPE)
    msg_content=""
    for line in Output.stdout:
        l = line.decode(encoding="euc-kr", errors="ignore")
        msg_content += l
        Output.wait()
        
    Output = msg_content
    
    if Debug :
        print("Input is : "+Input)
        print("Output is : "+Output)
    MapOutput = Parsor(Output)
    return MapOutput

def Parsor(TransStr, Sep1="\n", Sep2="="):
    Out = dict()
    In = ""
    
    if ( isinstance(TransStr, list) ):
        for one in TransStr:
            In += one + Sep1
    else :
        In = TransStr
    
    Tok = In.split(Sep1)
    
    for one in Tok:
        Tmp = one.split(Sep2)
        if Tmp[0] is not '':
            name = Tmp[0].strip()
            value = Tmp[1].strip()
            Out[name] = parse.quote(value)
    
    return Out

def MakeFormInput(dic,ext=list(),Prefix=""):
    Out = ""
    for one in dic.items():
        if(one[0] not in ext):
            Out += f"""
                <input type=hidden name="{one[0]}" value="{one[1]}" >
            """
    return Out

def MakeItemInfo(ItemAmt,ItemCode,ItemName):
    ItemInfo = ItemCode[0]+"|"+ItemAmt+"|1|"+ItemCode+"|"+ItemName
    
    return ItemInfo

def MakeParam(dic):
    Out = ""
    for one in dic.items():
        Out += one[0] + "=" + one[1] + ";"
    return Out

def Map2Str(dic):
    Out = ""
    for one in dic.items():
        Out += one[0] + "=" + one[1] +"<BR>"
    return Out