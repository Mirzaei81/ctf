import sys

encryptMessage = sys.stdin.read()
Letters = "abcdefghijklmnopqrstuvwxyz"
def encrypt(s:str,key:int):
    cipher = ""
    for c in s:
        Shifted = ord(c)+key
        delta = Shifted - ord("z")
        if(delta>0):
            Shifted = delta+ord("a")
        cipher+=chr(Shifted)
    
def decript(s:str,key:int):
    message = ""
    for c in s:
        if(c in Letters):
            pass
        Shifted = ord(c)-key
        delta = Shifted - ord("a")
        if(delta<0):
            Shifted = delta+ord("z")
        #print(f"charecter :{c} shifted: {Shifted}")
        message +=chr(Shifted)
    return message

for i in range(ord('z')-ord('a')):
    print(decript(encryptMessage.split('{')[1],i))

