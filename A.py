from datetime import date, datetime
fL=str("0")
Ti1=str("11:27")
Ti2=str("11:28")
def remin():
    s=str(datetime.now())
    global fL,Ti1,Ti2
    print(fL==str("0") and s[11:16]==Ti1)
    if(s[11:16]==Ti2):
        fL=str("0");print("waw")
        
    if fL==str("1"):
        return
    
    if(fL==str("0") and s[11:16]==Ti1):
        fL=str("1"),
        
    # print(str(fL)==str("0"))
    if fL==str("0"):
        return 
    
    else: print("awa")

remin()