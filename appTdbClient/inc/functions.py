import os
import subprocess
from urllib import parse
import locale

#############################################
#
# TeleditBinPath 에 SClient 실행파일을 꼭 위치시키고, 실행권한을 설정해주세요.
# 기본값은 프로젝트 디렉터리/bin/SClient 입니다.
# 해당 SClient 는 리눅스 64비트 용입니다.
#
#############################################

TeleditBinPath = "appTdbClient/bin/"
ID = "A010002002"
PWD = "bbbbb"
AMOUNT = 301

def CallTeledit(TransData, Debug=False):
    Bin="SClient"
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
    print(ItemInfo)
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