import os
import ctypes
from getpass import getuser
import sys



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False




if is_admin():
    with open("builder.txt","r") as builder_read:
        builder_list=builder_read.readlines()
    builder_read.close()
    
    os.system(builder_list[0].strip())
    os.system(builder_list[1].strip())
    os.remove("builder.txt")
    input("finish\nyou can remove me ;)")








while True:
    ext=input("select file extension:")
    conferm=input("select file extension:")
    if ext==conferm:
        sure=input("are you sure y/n:").lower()
        if sure=="y":break



primitive_path=r'C:\\Users\\'+str(getuser())
where_path=""
python_path=r"C:\\Users\\"+str(getuser())+"\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"


for dirpath, dirnames, filenames in os.walk(primitive_path):
    for filename in filenames:
        if filename == "rapid-shell.py":
            where_path = os.path.join(dirpath, filename)
            print(filename)


print(where_path)
print(python_path)

if os.path.exists(where_path) and os.path.exists(python_path):
    if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)==42:
        pass
    with open("builder.txt","w+") as builder:
        builder.write("assoc ."+ext+"="+ext+"\n"+"ftype "+ext+"="+python_path+" "+where_path+' "%1" %*')
    
else:
    print("unknown error")
    
