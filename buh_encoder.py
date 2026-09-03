TRI_TC = {
    "█":"ff0",
    "\n":"ff1",
    "?":"ff2",
    "!":"ff3",
    "0":"ff4",
    "1":"ff5",
    "2":"ff6",
    "3":"ff7",
    "4":"ff8",
    "5":"ff9",
    "6":"ffa",
    "7":"ffb",
    "8":"ffc",
    "9":"ffd",
    "	":"ffe",
    }

BI_TC = {
    "f":"f0",
    "y":"f1",
    "w":"f2",
    "g":"f3",
    "p":"f4",
    "b":"f5",
    "v":"f6",
    "k":"f7",
    "x":"f8",
    "q":"f9",
    "j":"fa",
    "z":"fb",
    ".":"fc",
    ",":"fd",
    "'":"fe",
    "|":"ff",
    }

MONO_TC = {
    " ":"0",
    "e":"1",
    "t":"2",
    "a":"3",
    "o":"4",
    "i":"5",
    "n":"6",
    "s":"7",
    "r":"8",
    "h":"9",
    "d":"a",
    "l":"b",
    "u":"c",
    "c":"d",
    "m":"e",
    }

def encodeToByteString(txt):
    txt = txt.lower()
    
    final = ""
    
    for let in txt:
        if let in MONO_TC:
            final += MONO_TC[let]
        elif let in BI_TC:
            final += BI_TC[let]
        elif let in TRI_TC:
            final += TRI_TC[let]
        else:
            final += TRI_TC["█"]
    
    if len(final) % 2 != 0:
        final += "0"
    
    return final

def decodeFromByteString(txt):
    global MONO_TC, BI_TC, TRI_TC
    R_MONO_TC = {value: key for key, value in MONO_TC.items()}
    R_BI_TC = {value: key for key, value in BI_TC.items()}
    R_TRI_TC = {value: key for key, value in TRI_TC.items()}
    
    final = ""
    
    c = -1
    
    for let in txt:
        c+=1
        
        nextl = ""
        nextl2 = ""
        prevl = ""
        prevl2 = ""
        
        try:
            nextl=txt[c+1]
        except:
            pass
        try:
            nextl2=txt[c+2]
        except:
            pass
        try:
            prevl=txt[c-1]
        except:
            pass
        try:
            prevl2=txt[c-2]
        except:
            pass
        
        if let == "f":
            if nextl != "f" and prevl != "f":
                final += R_BI_TC["f" + nextl]
                continue
            elif nextl == "f":
                final += R_TRI_TC["ff" + nextl2]
                continue
        
        if let != "f" and prevl != "f" and not (prevl == "f" and prevl2 == "f"):
            final += R_MONO_TC[let]
    
    return final.upper()

def convertToBuh(path,output):
    source = open(path,"r",encoding="utf-8").read()
    open(output,"wb").write(bytes.fromhex(encodeToByteString(source)))

def convertFromBuh(path,output):
    source = open(path,"rb").read().hex()
    open(output,"w", encoding="utf-8").write(decodeFromByteString(source))

if __name__ == "__main__":
    convertToBuh("buh test.txt","buh test.buh")
    convertFromBuh("buh test.buh", "buh reverse.txt")
    convertToBuh("buh dummy text.txt","buh dummy text.buh")
    convertToBuh("old script.txt","old script.buh")
    convertFromBuh("old script.buh","old script reverse.txt")
    convertToBuh("buh tiny test.txt","buh tiny test.buh")
