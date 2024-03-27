cipher = "UFJKXQZQUNB"
key =  "SOLVECRYPTO"
encrypted = ""

for c,i in enumerate(cipher):
    cipher = ord(i)
    k = ord(key[c])
    Ck = cipher -k
    CkMod = Ck%26
    EChar = chr(CkMod+65)
    encrypted+= EChar
    print(f"cipher:{cipher} k : {k},Chipher - key : {Ck} Cipher-key MOD 26 : {CkMod} massageCharacter : {EChar}")

print(encrypted)
