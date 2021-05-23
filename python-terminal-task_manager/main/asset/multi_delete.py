import os

import hashlib

def File_calcolatore_sha256(filename) -> str:
    sha256 = hashlib.sha256()
    with open(filename, "rb") as thefile:
        buf = thefile.read()
        sha256.update(buf)
    return str(sha256.hexdigest())

def delete_duplicate():
    sha_256=[]
    elements=[]
    for file in os.listdir():
        hasha=File_calcolatore_sha256(file)
        if hasha in sha_256:elements.append(file)
        else:
            sha_256.append(hasha)
    
    return elements 


def delete_name(file_name,discrimina=False):
    name=[]
    for x in os.listdir():
        filename= os.path.splitext(x)[0]
        if discrimina==True and filename!=file_name:name.append(x)
        elif discrimina==False and filename==file_name:name.append(x)
        else:pass
    return name

def delete_ext(ext="vandalo",discrimina=False):
    name=[]
    for x in os.listdir():
        file_extension = os.path.splitext(x)[1]
        if discrimina==True and file_extension!=ext:name.append(x)
        elif discrimina==False and file_extension==ext:name.append(x)
        else:pass
    return name

def delete_size(size,discrimina):
    name=[]
    for element in os.listdir():
        file_size=round(os.path.getsize(element)/(1024*1024),3)
        if discrimina=="-mag":
            if file_size>size:name.append(element)
            else:pass
        if discrimina=="-min":
            if file_size<size:name.append(element)
            else:pass
        if discrimina=="-umag":
            if file_size>=size:name.append(element)
            else:pass
        if discrimina=="-umin":
            if file_size<=size:name.append(element)
            else:pass
        return name