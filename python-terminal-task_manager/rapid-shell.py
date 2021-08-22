nice_conta_file=0
test_echo_command_sha256=False

#'\033[32m'
import os
os.system("")
try:
    from rich.console import Console 
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss rich lib run first installer.py")
    exit()

import os
help_path=r''+os.getcwd()+"\\"+"help.txt"
echo_off=os.getcwd()
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1
import subprocess
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1

try:
    from rich.table import Table
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss rich lib run first installer.py")
    exit()

try:
    from rich.prompt import Confirm
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss rich lib run first installer.py")
    exit()

from random import randint
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1

from datetime import datetime
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1
import platform
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1

try:
    import main.asset.secure.file_sha256
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
    import main.asset.secure.cripta
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
    import main.asset.Down.DonwloadLib as DonwloadLib
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
    import main.asset.multi_delete as multi_delete
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
    import main.asset.wifi as wifi
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
    import main.asset.correttore as Correttore
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1

except Exception as e:
    print(str(e))
    input('\033[31m'+"you miss some file please run installer.py with this code 1789")
    exit()
import sys
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1
import time
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1
import shutil
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1
import re
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1
try:
    from tqdm import tqdm
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss tqm lib run first installer.py")
    exit()
try:
    import pyAesCrypt 
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss pyAesCrypt lib run first installer.py")
    exit()

try:
    import requests
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss request lib run first installer.py")
    exit()


from getpass import getpass,getuser
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1
import random ,string
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1
import urllib.request, json
print(f"[+] success {nice_conta_file}")
nice_conta_file+=1
try:
    import psutil
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss request lib run first installer.py")
    exit()

import zipfile
    
os.system('cls' if os.name=='nt' else 'clear')



try:
    with urllib.request.urlopen("https://nicholas-the-null.github.io/py_manager_website/stats.json") as url:data = json.loads(url.read().decode())
except:
    data=None


import ctypes

counter_error_passer=0



usb_active=False

delete_log_file=os.getcwd()


console = Console()
history=[]
primitive_path=r'C:\\Users\\'+str(getuser())
plugin_path=r''+os.getcwd()+"\\plugin"
error_log_path=r''+os.getcwd()+"\\loghshshshshshshshshhshsh.txt"
if os.path.exists(error_log_path) is False:
    with open(error_log_path,"w+") as file:
        pass

def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference

def error_log(command,error):
    global counter_error_passer
    counter_error_passer+=1
    ora=datetime.now()
    ora=ora.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    with open(error_log_path,"a") as logs:
        logs.write("error at "+ora+" in command " + command + " with this message " + error +"\n")
    if counter_error_passer%100==0:
        print("error if you want report please send log.txt file text to https://github.com/Nicholas-the-Null/py-manager/issues")
def GetShortPathName(path):
    if os.getcwd in [r"C:\\Users","C:",primitive_path]:
        path=path
    else:
        path=path[len(primitive_path)-1:]
        return path

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def SetProtection():
	ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
	ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

def UnsetProtection():
	ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0


table = Table(title="info")
table.add_column("time",style="magenta")
table.add_column("os",style="green",no_wrap=True)
table.add_column("version",style="purple",no_wrap=True)
table.add_column("sha256",style="green",no_wrap=True)


if data is None:
    table.add_column("update",style="green",no_wrap=True)
    update="error no internet"
    version="1.1.22.3.4"


elif data.get("sha256")!=main.asset.secure.file_sha256.File_calcolatore_sha256(sys.argv[0]):
    table.add_column("update",style="red",no_wrap=True)
    update="True"
else:
    table.add_column("update",style="green",no_wrap=True)
    update="False"

if data is not None:version=data.get("version")
table.add_row(str(datetime.now()),str(platform.uname().system),version, #versione giusta
main.asset.secure.file_sha256.File_calcolatore_sha256(sys.argv[0]),update)

console.print(table)





console.print("""[green] 
  _____       __  __                                   
 |  __ \     |  \/  |                                  
 | |__) |   _| \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 |  ___/ | | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |   | |_| | |  | | (_| | | | | (_| | (_| |  __/ |   
 |_|    \__, |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
         __/ |                          __/ |          
        |___/                          |___/           
""" +"[/]")

print("")

protect=False

multiple_command=[]
multi_command_parse=[]
multi_command_string=""
multi_command_parse_string=""

finito=False
conta=0

file=sys.argv[1]

with open(file,'r') as file_read:
    list_command=file_read.readlines()



while True:
    try:
        if echo_off!="":
            echo_off=os.getcwd()
        
        if is_admin():
            sys_type="#"
        else:
            sys_type="$"
            
        if len(multi_command_string)!=0:
            multiple_command=multi_command_string.split()
            command=multiple_command
            multi_command_string=""



        else:
            if conta>len(list_command):
                break
            if conta==len(list_command):
                break
            command=list_command[conta].strip().split()
            conta+=1
        if "|" in command:
            found=False
            for commands in command:
                if commands=="|" and found==False:
                    found=True
                    multi_command_parse=multi_command_parse_string.split()
                else:
                    if len(multi_command_parse)==0:
                        multi_command_parse_string+=commands+" "
                    else:
                        multi_command_string+=commands+" "
            command=multi_command_parse
            multi_command_parse_string=""
            multi_command_parse=[]
#pwd | ls -l | echo ciao | scf ? ? $** import os | pwd

        
        if len(command)==0:
            command=["echo",""]
        if command[0]=="secret":
            command.pop(0)
        else:
            history.append(" ".join(command))

        if usb_active==True:
            dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
            uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
            x = diff(uncheckeddrives, drives)
            x = diff(drives, uncheckeddrives)
            drives = uncheckeddrives
            if usb not in drives:
                usb_active=False
                os.chdir(original_usb)
                command=["echo",f"error usb removed return to {original_usb}"]
            
        if len(command)==0:
            command=["echo","no command in input"]

        if command[0].lower() in ["hs","hy","history"]:#history of command
            if len(command)==3:
                commando=command[1]
                file=command[2]
                try:
                    if os.path.exists(file) is False:
                        x=open(file,"w+")
                        x.close()
                except Exception as e:
                    error_log("history",str(e))
                if commando==">":commando="w"
                elif commando==">>":commando="a"
                else:commando=None
                if commando !=None:
                    try:
                        with open(file,commando) as f:
                            for numero,nome in enumerate(history):
                                f.write(str(numero+1)+ " " +str(nome)+"\n")
                    except Exception as e:
                        print("error file not valid "+ str(e))
                        error_log("history",str(e))

                else:
                    print("error invalid operator")
            else:
                table = Table(title="history")
                table.add_column("numero",style="magenta")
                table.add_column("command",style="green",no_wrap=True)
                for numero,nome in enumerate(history):
                    table.add_row(str(numero+1),str(nome))
                
                console.print(table)

        elif command[0]=="update":
            if update=="True":
                #DonwloadLib.download_file("https://site.todonwload")#site
                print("download complete")
            else:
                print("no download found")             

        elif command[0].lower()=="sudo":
            if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)==42:
                exit()
            
        elif command[0].lower()=="pwd":print(os.getcwd())

        elif command[0]=="protection":
            if sys_type=="#" and protect==False:
                SetProtection()
                protect=True
                print("ok")
            else:
                print("error")

        elif command[0]=="unprotection":
            if sys_type=="#" and protect==True:
                UnsetProtection()
                protect=False
                print("ok")
            else:
                print("error")


        
        elif command[0].lower()=="wifi":
            if len(command)!=0:
                command.pop(0)
                if wifi.detect_system_lang()[0:2]!=wifi.lang():
                    print("remember to change language to wifi module")
                else:
                    for x in command:
                        if x=="-ssid":
                            print(wifi.get_ssid())
                        elif x=="-auth":
                            print(wifi.get_auth())
                        elif x=="-password":
                            print(wifi.get_password(wifi.get_ssid()))
                        elif x=="-show":
                            wifi.generate_qr_code(wifi.get_ssid(),wifi.get_password(wifi.get_ssid()),wifi.get_auth(),"",True)
                        elif x=="-save":
                            wifi.generate_qr_code(wifi.get_ssid(),wifi.get_password(wifi.get_ssid()),wifi.get_auth(),"ciao.png",False)

            else:
                print("error ")

        elif command[0].lower() in ["cd","changedirectory","chd"]: #change dir
            command.pop(0)
            try:
                directory=command[0]
                if directory=="~":os.chdir(r'C:\\Users\\'+os.getlogin())
                else:
                    directory=r''+directory
                    if os.path.exists(directory) is False:
                        if Confirm.ask("Do you want create a new directory?"):
                            os.mkdir(directory)
                        else:
                            console.print("[red]not create"+"[/]")
                    else:
                        os.chdir(directory)
            except:
                if Confirm.ask("Do you want return to home dir?"):
                    os.chdir(r'C:\\Users\\'+os.getlogin())
                else:
                    console.print("[red]ok"+"[/]")

        elif command[0].lower() in ["md","mkd","mkdir"]: #create dir
            command.pop(0)
            if len(command)==0:
                console.print("[red]error no name in input"+"[/]")
            else:
                if os.path.exists(command[0]):
                    console.print("[red]error directory already exists"+"[/]")
                else:
                    try:
                        os.mkdir(command[0])
                    except Exception as e:
                        print(str(e))
                        error_log("history",str(e))

        elif command[0].lower() in ["getsha","sha256","gtsh","get256"]: #sha256 of file or string
            command.pop(0)
            if os.path.exists(command[0]) and os.path.isdir(command[0])==False:
                input_type= "-file" 
                result=main.asset.secure.file_sha256.File_calcolatore_sha256(command[0])
            else:
                input_type="-string" 
                result=main.asset.secure.file_sha256.String_calcolatore_sha256(command[0])
            
            table=Table(title="info")
            table.add_column("useriput",no_wrap=True,style="blue")
            table.add_column("type",style="magenta")
            table.add_column("sha256",no_wrap=True,style="green")
            table.add_row(command[0],input_type,result)
            console.print(table)

        elif command[0].lower() in ["clear","cls"]:
            command.pop(0)
            if len(command)==0:
                os.system("cls")
            else:
                if command[0]==">":
                    command.pop(0)
                    if os.path.exists(command[0]) and os.path.isdir(command[0]) is False:
                        try:
                            x=open(command[0],"w")
                            x.write("")
                            x.close()
                        except Exception as e:
                            print("error during file writing")
                            error_log("history",str(e))
                    elif command[0].startswith("history"):
                        if command[0]=="history":
                            history=[]
                        else:
                            try:
                                i=7
                                partenza=""
                                while True:
                                    if command[0][i]!=":":
                                        partenza+=command[0][i]
                                    else:
                                        break
                                    i+=1


                                partenza=int(partenza)
                                
                                fine=""
                                i+=1
                                while True:
                                    if i==len(command[0]):break
                                    
                                    if command[0][i].isnumeric() is True:
                                        fine+=command[0][i]
                                    else:
                                        break
                                    i+=1
                                
                                fine=int(partenza)
                                if fine<partenza:
                                    scambio=fine
                                    fine=partenza
                                    partenza=scambio
                                lista_app=[]
                                for numero, stringa in enumerate(history):
                                    if numero+1>=partenza and numero+1 <=fine:#errore elimina numer sbagliati
                                        print(stringa)
                                        
                                    else:
                                        lista_app.append(stringa)
                                history=lista_app

                            except Exception as e:
                                error_log("history",str(e))
                                pass

                else:
                    print("error")

        elif command[0].lower()=="usb":
            print("usb menu active")
            if usb_active==False:
                original_usb=os.getcwd()
            dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
            while True:
                uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
                x = diff(uncheckeddrives, drives)
                x = diff(drives, uncheckeddrives)
                drives = uncheckeddrives
                print("usb on computer " + str(drives[1:]))
                menu=input("1-refresh,2-go on usb,3-exit:")
                if menu=="1":
                    pass
                elif menu=="2":
                    while True:
                        danger=False
                        try:
                            usb=input("select usb: ctrl+c for exit")
                            if usb in drives:
                                break
                            else:
                                print("not found")
                        except KeyboardInterrupt:
                            danger=True
                            break
                    try:
                        os.chdir(usb)
                        usb_active=True
                        break
                    except:
                        if danger==False:
                            print("usb removed")
                    

                elif menu=="3":
                    if usb_active==True:
                        os.chdir(original_usb)
                        break
                    else:
                        break
                else:
                    print("command not found")
            

        elif command[0].lower() in ["rd","random","rnd"]:
            command.pop(0)
            sort=False
            if len(command)>=3:
                start=command[0]
                finish=command[1]
                many=command[2]
                try: 
                    start=int(start)
                    finish=int(finish)
                    many=int(many)
                    if finish<start:
                        app=start
                        start=finish
                        finish=app

                    if "-duplicate" in command:
                        duplicate=True
                    else:
                        duplicate=False
                    if "-sort" in command:
                        sort=True
                    else:
                        sort=False
                    
                    
                    if duplicate == True and (finish-start)<many:
                        print("error too few with duplicate parma will be disable")
                        duplicate=False
                    return_list=[]
                    while True:
                        if len(return_list)==many:
                            break
                        return_list.append(randint(start,finish))
                        if duplicate==True:
                            return_list=list(dict.fromkeys(return_list))
                    if sort==True:
                        return_list.sort()
                    print(return_list)
                except ValueError:
                    print("error string insert on numer request")
                    error_log("history","valueError")
            
            else:
                print("error parma not given in input")

        elif command[0].lower() in ["more","mr"]: # read file head for print first line default is 10 and tail for the last line
            command.pop(0)
            if not len(command)==0:
                if os.path.exists(command[0]):
                    try:
                        if len(command)==1:
                            with open(command[0],'r') as Read_file:
                                file_contenent=Read_file.readlines()
                            number_line_conta=0
                            for number_line,line in enumerate(file_contenent):
                                if number_line_conta==10:
                                    if not Confirm.ask("more"):
                                        break
                                    else:
                                        number_line_conta=0
                                else:
                                    print(line.strip())
                                    number_line_conta+=1
                        else:
                            if command[1].lower()=="-tail":
                                number=10
                                if not len(command)==2:number=int(command[2])
                                with open(command[0],'r') as Read_file:
                                    file_contenent=Read_file.readlines()

                                num_lines = sum(1 for line in open(command[0]))

                                for number_line,line in enumerate(file_contenent):
                                    # x = 21-10


                                    if number_line>=num_lines-number:
                                        print(line.strip())
                                    else:
                                        pass



                                

                            elif command[1].lower()=="-head":
                                number=10
                                if not len(command)==2:number=int(command[2])
                                with open(command[0],'r') as Read_file:
                                    file_contenent=Read_file.readlines()
                                for number_line,line in enumerate(file_contenent):
                                    if number_line==number:break
                                    else:
                                        print(line.strip())


                            else:
                                console.print(f"[red]error parma {command[1]} not found"+"[/]")

                    except Exception as e:
                        console.print("[red]error i cant read file"+"[/]")
                        error_log("history",str(e))
                else:
                    console.print("[red]error file not found"+"[/]")

            else:
                console.print("[red]error no file in input"+"[/]")


        elif command[0].lower() in ["ls","listdir","lsdir"]: #ls command print all file in a dir -l for long description -a for include all subdir and his file
            command.pop(0)#parma
            interupt=False
            if not len(command)==0:
                if os.path.exists(command[0]) and os.path.isdir(command[0]):
                    directory=command[0]
                    command.pop(0)
                else:
                    directory=os.getcwd()
                if not len(command)==0:
                    if len(command)==2 and (command==["-a","-l"] or command==["-l","-a"]):
                        table=Table(title="file")
                        table.add_column("#", style="magenta",)
                        table.add_column("name", style="red")
                        table.add_column("is_dir",style="green")
                        table.add_column("size",style="blue")
                        table.add_column("creation",style="cyan") 
                        table.add_column("read",style="yellow")
                        table.add_column("write",style="#008B8B")
                        numero=0
                        
                        try:
                            for path, subdirs, files in os.walk(directory):
                                if interupt==True:
                                    break
                                else:
                                    for element in files:
                                        nome=os.path.join(path, element)
                                        try:
                                            tempo=datetime.fromtimestamp(os.path.getctime(nome))
                                            tempo=tempo.strftime("%d:%m:%y")
                                            is_dir=str(os.path.isdir(nome))
                                            is_dir=is_dir[0]
                                            size=str(round(os.path.getsize(nome)/(1024*1024),3))
                                            read=str(os.access(nome,os.R_OK))[0]
                                            write=str(os.access(nome,os.W_OK))[0]
                                            table.add_row(str(numero),str(GetShortPathName(path)),is_dir,size,tempo,read,write)
                                            numero+=1
                                        except (Exception,KeyboardInterrupt) as e:
                                            if str(e)=="":
                                                interupt=True
                                                break
                                            pass
                        except KeyboardInterrupt:
                            interupt=True

                        try:
                            if interupt==False:
                                console.print(table)
                        except:pass


                    elif command[0]=="-l":
                        table=Table(title="file")
                        table.add_column("#", style="magenta")
                        table.add_column("name", style="red")
                        table.add_column("is_dir", style="green")
                        table.add_column("size",style="blue")
                        table.add_column("creation",style="cyan") 
                        table.add_column("read",style="yellow")
                        table.add_column("write",style="#008B8B")
                        
                        try:
                            for numero,nome in enumerate(os.listdir(directory)):
                                if interupt==True:
                                    break
                                try:
                                    nome1=nome
                                    nome=r''+directory+"\\"+nome
                                    tempo=datetime.fromtimestamp(os.path.getctime(nome))
                                    tempo=tempo.strftime("%d:%m:%y")
                                    is_dir=str(os.path.isdir(nome))
                                    is_dir=is_dir[0]
                                    size=str(round(os.path.getsize(nome)/(1024*1024),3))
                                    read=str(os.access(nome,os.R_OK))[0]
                                    write=str(os.access(nome,os.W_OK))[0]

                                    table.add_row(str(numero),nome1,is_dir,size,tempo,read,write)
                                except (Exception,KeyboardInterrupt) as e:
                                    if str(e)=="":
                                        interupt=True
                                        break
                                    pass
                        except KeyboardInterrupt:
                            interupt=True

                        try:
                            if interupt==False:
                                console.print(table)
                        except:pass



                    elif command[0]=="-a":
                        table=Table(title="file")
                        table.add_column("nome",style="magenta")
                        
                        try:
                            for path, subdirs, files in os.walk(directory):
                                if interupt==True:
                                    break
                                else:
                                    for element in files:
                                        table.add_row(os.path.join(path, element))
                        except KeyboardInterrupt:
                            interupt=True
                            pass
                        try:
                            if interupt==False:
                                console.print(table)
                        except:pass

                    else:
                        console.print(f"[red]error parma are wrong "  +"[/]")
                else:
                    table=Table(title="file")
                    table.add_column("name",style="magenta")
                    try:
                        for x in os.listdir(directory):
                            if interupt==True:
                                break
                            else:
                                table.add_row(x)
                    except KeyboardInterrupt:
                        interupt=True
                        pass
                    try:
                        if interupt==False:
                            console.print(table)
                    except:pass
            else:
                table=Table(title="file")
                table.add_column("name",style="magenta")
                try:
                    for x in os.listdir():
                        if interupt==True:
                            break
                        else:
                            table.add_row(x)
                except KeyboardInterrupt:
                    interupt=True
                    pass
                try:
                    if interupt==False:
                        console.print(table)
                except:pass



        elif command[0].lower() in ["cp","copy"]: #copy file in another dir
            command.pop(0)
            if len(command)>1:
                if os.path.exists(command[0]):
                    try:
                        ver=False
                        path=os.path.split(command[1])[0]
                        if path=="":
                            path=os.getcwd()
                        for x in os.listdir(path):
                            if r''+path+'\\'+x==command[1]:
                                if Confirm.ask("there are a file with the same do you want replace"):
                                    pass
                                else:
                                    ver=True                           
                        if ver==False:shutil.copyfile(command[0],command[1])
                    except Exception as e:
                        console.print("[red]error i cant create new file "+str(e)+"[/]")
                        error_log("history",str(e))
                else:
                    console.print("[red]file not found"+"[/]")
            else:
                console.print("[red]not parma in input"+"[/]")


        elif command[0].lower() in ["mv","move"]: #move file in another folder
            command.pop(0)
            if len(command)>1:
                if os.path.exists(command[0]):
                    path=os.path.exists(os.path.split(command[1])[0])
                    if path=="":
                        path=os.getcwd()
                    if os.path.exists(path):
                        try:
                            shutil.move(command[0],command[1])
                        except Exception as e:
                            console.print("[red]error i cant create new file "+str(e)+"[/]")
                            error_log("history",str(e))
                    else:
                        console.print("[red]file not found"+"[/]")
                else:
                    console.print("[red]file not found"+"[/]")
            else:
                console.print("[red]not parma in input"+"[/]")

        elif command[0].lower() in ["rm","remove"]: #remove file
            command.pop(0)
            if len(command)==1:
                if command[0]=="-a":
                    for x in os.listdir():
                        if os.path.isdir(x) is False:os.remove(x)
                else:
                    if os.path.exists(command[0]) and os.path.isdir(command[0]) is False:
                        os.remove(command[0])
                    else:
                        print("error i cant delete element")
            elif len(command)==2:
                path=command[0]
                parma=command[1]
                if path=="-a" and parma=="-d":
                    for x in os.listdir():
                        if os.path.isdir(x):
                            shutil.rmtree(x,ignore_errors=True)
                            #os.rmdir(x)
                        else:
                            os.remove(x)

                elif os.path.exists(path) and os.path.isdir(path) and parma=="-d":
                    shutil.rmtree(path,ignore_errors=True)
                    if os.getcwd()!=path:
                        os.rmdir(path)

                elif os.path.exists(path) and os.path.isdir(path) and parma=="-a":
                    for x in os.listdir(path):
                        if os.path.isdir(r''+path+'\\'+x) is False:os.remove(r''+path+'\\'+x)
                else:
                    print("error ")

            elif len(command)==3:
                path=command[0]
                parma1=command[1]
                parma2=command[2]
                if os.path.exists(path) and os.path.isdir(path) and ((parma1=="-a" and parma2=="-d") or (parma1=="-d" or parma2=="-a")):
                    for x in os.listdir(path):
                        if os.path.isdir(r''+path+'\\'+x) is False:os.remove(r''+path+'\\'+x)
                        else:
                            shutil.rmtree(r''+path+'\\'+x,ignore_errors=True)
                            #os.rmdir(r''+path+'\\'+x)
                    if os.getcwd()!=path:
                        os.rmdir(path)
                else:
                    print("error")



            else:
                print("error command wrong")

        elif command[0].lower() in ["if","info"]:
            command.pop(0)
            if len(command)>=1:
                if os.path.exists(command[0]) and os.path.isfile(command[0]):
                    table=Table(title="file")
                    table.add_column("name", style="red")
                    table.add_column("is_dir", style="green")
                    table.add_column("size",style="blue")
                    table.add_column("creation",style="cyan") 
                    table.add_column("read",style="yellow")
                    table.add_column("write",style="#008B8B")
                    nome=command[0]
                    try:
                        nome1=os.path.split(nome)[1]
                        tempo=datetime.fromtimestamp(os.path.getctime(nome))
                        tempo=tempo.strftime("%d:%m:%y")
                        is_dir=str(os.path.isdir(nome))
                        is_dir=is_dir[0]
                        size=str(round(os.path.getsize(nome)/(1024),3))
                        read=str(os.access(nome,os.R_OK))[0]
                        write=str(os.access(nome,os.W_OK))[0]
                        table.add_row(nome1,is_dir,size,tempo,read,write)
                        console.print(table)
                    except Exception as e:
                        print("error "+str(e))
                        error_log("history",str(e))
                else:
                    print("error file not dound or is a dir")
            else:
                print("parma not found")






        elif command[0].lower() in ["srm","secureremove"]: #secure rfemove file
            command.pop(0)
            if len(command)==1:
                if os.path.exists(command[0]) and os.path.isdir(command[0])== False:
                    main.asset.secure.cripta.Delete_File(command[0])
                    os.remove(command[0])
                else:
                    console.print("[red]file not found"+"[/]")
            else:
                console.print("[red]not parma in input"+"[/]")

        elif command[0].lower() in ["grep","grp","gp"]: #print line where a string parma -i for regex use and -s for print only number of line parma -i first
            command.pop(0)
            try:
                count=0
                if os.path.exists(command[0]) and os.path.isdir(command[0])==False:
                    if not len(command)==1:
                        parola=command[1]
                        regex=re.compile(r''+parola)                  
                        with open(command[0],"r") as file:
                            filee=file.readlines()
                        for line in filee:
                            if regex.search(line):
                                if "-s" not in command:
                                    print(str(count) + " "+ line.strip())
                                count+=1
                        print("count " + str(count))

                    else:
                        console.print("[red]not parma in input"+"[/]")

                else:
                    console.print("[red]file not found"+"[/]")
            except Exception as e:
                print("error in regx read")
                error_log("history",str(e))
        
        elif command[0] in ["ex","exit","xexit"]:
            if Confirm.ask("Do you want exit?"):
                print("ok bye have a nice day :)")
                time.sleep(2)
                exit()
            else:
                pass

        elif command[0] in ["dn","down","download"]:
            #! tipo download sito cartella  
            original=os.getcwd()
            command.pop(0)
            if not len(command)==0:
                if command[0]=="-file":
                    command.pop(0)
                    if not len(command)==0:
                        if len(command)==2:
                            if os.path.exists(command[1]):os.chdir(command[1])
                            else:console.print("[red]error dir not found"+"[/]")
                        result=DonwloadLib.download_file(command[0])
                        
                        if not result=="Success":console.print(result)
                        os.chdir(original)
                        
                    else:
                        console.print("[red]error parma dont match"+"[/]")

                elif command[0]=="-site-js":
                    command.pop(0)
                    if not len(command)==0:
                        if len(command)==2:
                            if os.path.exists(command[1]):os.chdir(command[1])
                            else:console.print("[red]error dir not found"+"[/]")
                        result=DonwloadLib.js(command[0])
                        
                        if not result=="Success":console.print(result)
                        os.chdir(original)
                        
                    else:
                        console.print("[red]error parma dont match"+"[/]")

                elif command[0]=="-site-css":
                    command.pop(0)
                    if not len(command)==0:
                        if len(command)==2:
                            if os.path.exists(command[1]):os.chdir(command[1])
                            else:console.print("[red]error dir not found"+"[/]")
                        result=DonwloadLib.css(command[0])
                        
                        if not result=="Success":console.print(result)
                        os.chdir(original)
                        
                    else:
                        console.print("[red]error parma dont match"+"[/]")



                elif command[0]=="-site-image":
                    command.pop(0)
                    if not len(command)==0:
                        if len(command)==2:
                            if os.path.exists(command[1]):os.chdir(command[1])
                            else:console.print("[red]error dir not found"+"[/]")
                        
                        
                        letters = string.ascii_lowercase
                        x= ''.join(random.choice(letters) for i in range(13))
                        print(f"because this command generate a lot of image we create a new temporany dir [{x}]")
                        os.mkdir(x)
                        os.chdir(x)
                        result=DonwloadLib.image(command[0])
                        
                        if not result=="Success":console.print(result)
                        os.chdir(original)
                        
                    else:
                        console.print("[red]error parma dont match"+"[/]")


                else:
                    console.print("[red]error parma dont match"+"[/]")

                        

            else:
                console.print("[red]error no parma in input "+"[/]")
            pass
        

        elif command[0] in ["mrm","multiremove"]:
            #comando path metodo_eliminzaione modalità altro 
            original=os.getcwd()
            command.pop(0)
            if len(command)!=0:
                if command[0]=="$":command[0]=os.getcwd()
                if os.path.exists(command[0]) and os.path.isdir(command[0]):
                    os.chdir(command[0])
                    command.pop(0)
                    if not len(command)==0:

                        if command[0] in ["-srm","-secureremove"]:
                            sicuro=True
                            command.pop(0)
                        else:sicuro=False
                        
                        
                        if not len(command)==0:
                            if command[0]=="-duplicate":
                                file_list=multi_delete.delete_duplicate()

                            elif command[0]=="-ext":
                                command.pop(0)
                                if len(command)!=0:
                                    est=command[0]
                                    command.pop(0)
                                    if len(command)!=0:
                                        if command[0]=="-t":discrimina=True
                                        else:discrimina=False
                                    else:discrimina=False
                                    file_list=multi_delete.delete_ext(est,discrimina)
                                else:
                                    console.print("[red]you miss parma in input "+"[/]")
                                    file_list=[]

                            elif command[0]=="-name":
                                command.pop(0)
                                if len(command)!=0:
                                    name=command[0]
                                    command.pop(0)
                                    if len(command)!=0:
                                        if command[0]=="-t":discrimina=True
                                        else:discrimina=False
                                    else:discrimina=False
                                    file_list=multi_delete.delete_name(name,discrimina)
                            

                                else:
                                    console.print("[red]you miss parma in input "+"[/]")
                                    file_list=[]

                            elif command[0]=="-size":
                                command.pop(0)
                                if len(command)!=0:
                                    size=command[0]
                                    command.pop(0)
                                    try:
                                        size=float(size)
                                        if len(command)!=0:
                                            if command[0] in ["-mag","-min","-umag","-umin"]:
                                                discrimina=command[0]
                                                file_list=multi_delete.delete_size(size,discrimina)
                                            else:
                                                console.print("[red]your parma are wrong "+"[/]")
                                                file_list=[]
                                        else:
                                            console.print("[red]you miss parma in input "+"[/]")
                                            file_list=[]
                                    except ValueError:
                                        console.print("[red]your parma are wrong "+"[/]")
                                        file_list=[]


                                else:
                                    console.print("[red]you miss parma in input "+"[/]")
                                    file_list=[]



                            else:file_list=[]
                                
                                    
                                    
                        else:
                            console.print("[red]error no parma in input "+"[/]")
                            os.chdir(original)




                        if len(file_list)!=0:
                            for element in file_list:
                                if sicuro==True:
                                    main.asset.secure.cripta.Delete_File(element)
                                os.remove(element)
                            os.chdir(original)
                        else:
                            console.print("[red]no file to delete "+"[/]")
                            os.chdir(original)

                        






                    


                    else:
                        console.print("[red]error no parma in input "+"[/]")
                        os.chdir(original)



                else:
                    console.print(f"[red]error {command[0]} dir not found "+"[/]")
                    os.chdir(original)
            else:
                console.print("[red]error no parma in input "+"[/]")
            
    

        elif command[0]=="echo":
            command.pop(0)
            out=""
            out_format="monitor"
            save_number=0
            if len(command)==1 and command[0]=="off":
                if echo_off!="":
                    echo_off=""
                else:
                    echo_off=os.getcwd()
            else:
                for number,under_string in enumerate(command):
                    
                    if under_string in [">",">>"]:
                        save_number=number
                        out_format="file"
                        break
                    if under_string[:5]=="date:":
                        formatto=under_string[5:]
                        formatto=formatto.replace("?"," ")
                        if formatto in [None,""," "]:under_string=str(datetime.now())
                        try:
                            under_string=datetime.now()
                            under_string=str(under_string.strftime(formatto))
                        except Exception as e:
                            print(e)
                            error_log("history",str(e))
                            under_string=str(datetime.now())
                    
                    if under_string=="%pwd":under_string=str(os.getcwd())
                    if test_echo_command_sha256==True:
                        under_string=""
                        test_echo_command_sha256=False
                    if under_string=="%Sha256" and len(command)>number+1:
                        
                        under_string=main.asset.secure.file_sha256.String_calcolatore_sha256(command[number+1])
                        test_echo_command_sha256=True



                    out+=under_string+" "
                if out_format=="monitor":
                    print(out)
                else:

                    if len(command)<save_number+2:
                        console.print("[red]error miss parma "+"[/]")
                    else:
                        try:
                            if command[save_number]==">":
                                with open(command[save_number+1],'w+') as file:
                                    file.write(out)
                            else:
                                with open(command[save_number+1],'a') as file:
                                    file.write("\n"+out)
                        except:
                            console.print("[red]error invalid file name "+"[/]")



        elif command[0] in ["pc","proc","process"]:
            command.pop(0)
            if len(command)!=0:
                if command[0] in ["-kill","-kl"]:
                    command.pop(0)
                    if len(command)!=0:
                        if checkIfProcessRunning(command[0]):
                            try:
                                subprocess.call("taskkill /F /IM " + command[0])
                            except Exception as e:
                                print("error "+str(e))
                                error_log("history",str(e))
                        else:pass
                    else:
                        console.print("[red]error no parma [/]")
                if command[0] in ["-ch","-check","-ck"]:
                    command.pop(0)
                    if len(command)!=0:
                        if checkIfProcessRunning(command[0]):
                            print("running")
                        else:
                            print("not running")
                    else:
                        console.print("[red]error no parma [/]")

                elif command[0] in ["-all","-l"]:
                    table=Table(title="process")
                    table.add_column("name")
                    table.add_column("pid")
                    table.add_column("priority level")
                    table.add_column("memory use (kb)")
                    table.add_column("read kbytes")
                    table.add_column("write kbytes")
                    table.add_column("num threads")
                    table.add_column("status")


                    for proc in psutil.process_iter():
                        try:
                            process_name=proc.name()
                            process_pid=proc.pid
                            nice = int(proc.nice())
                            memory_usage = proc.memory_full_info().uss
                            io_counters = proc.io_counters()
                            read_bytes = io_counters.read_bytes
                            write_bytes = io_counters.write_bytes
                            n_threads = proc.num_threads()
                            
                            status=proc.status()
                            table.add_row(str(process_name),str(process_pid),
                            str(nice),str(memory_usage//1024),str(read_bytes//1024),
                            str(write_bytes//1024),str(n_threads),str(status))
                        
                            

                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                            continue
                    console.print(table)

            else:
                console.print("[red]error no parma [/]")
        





        elif command[0] in ["en","encrypt"]:
            command.pop(0)
            'parma file'
            if len(command)==1:
                if os.path.exists(command[0]):
                    bufferSize = 1024 * 1024
                    if os.path.isdir(command[0]):
                        for file in os.listdir(command[0]):
                            if os.path.isdir(file) is False:
                                file=r''+command[0]+"\\"+file
                                password=getpass(f"give me the password of file {file}: ")
                                with open(file, "rb") as fIn:
                                    with open(file+"aes", "wb") as fOut:
                                        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
                                main.asset.secure.cripta.Delete_File(file)
                                os.remove(file)

                    else:
                        with open(command[0], "rb") as fIn:
                            password=getpass(f"give me the password of file {command[0]}")
                            with open(command[0]+"AES", "wb") as fOut:
                                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
                        main.asset.secure.cripta.Delete_File(command[0])
                        
                        os.remove(command[0])


                else:
                    print("path not found")
            else:
                print("parma npot found")

    
            


                        
        elif command[0] in ["dc","decript"]:
            command.pop(0)
            if len(command)==1:
                if os.path.exists(command[0]):
                    bufferSize = 1024 * 1024
                    if os.path.isdir(command[0]):
                            for file in os.listdir(command[0]):
                                if os.path.isdir(file) is False:
                                    file=r''+command[0]+"\\"+file
                                    password=getpass(f"give me the password of file {file}: ")
                                    encFileSize=os.stat(file).st_size
                                    estensione=input("give me the extension of the output file [important] ")
                                    with open(file, "rb") as fIn:
                                        try:
                                            with open(file+"decriptato."+estensione, "wb") as fOut:
                                                try:
                                                    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
                                                except Exception as e:
                                                    print("password wrong")
                                                    error_log("history",str(e))
                                        except ValueError:
                                            os.remove(file+"decriptato"+estensione)
                                    try:
                                        os.remove(file)
                                    except:
                                        pass
                    else:
                        password=getpass(f"give me the password of file {command[0]}")
                        encFileSize=os.stat(command[0]).st_size
                        estensione=input("give me the extension of the output file [important] ")
                        with open(command[0], "rb") as fIn:
                            try:
                                with open(command[0]+"decriptato."+estensione, "wb") as fOut:
                                    try:
                                        pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
                                    except Exception as e:
                                        print("password wrong")
                                        error_log("history",str(e))
                            except ValueError:
                                os.remove(command[0]+"decriptato"+estensione)
                        try:
                            os.remove(command[0])
                        except:
                            pass

                else:
                    print("path not found")

            else:
                print("parma npot found")
    
        



        elif command[0].lower() in ["scf","search"]:
            #? file_name;exetension;path;special
            command.pop(0)
            type_search_word=False
            if len(command)>=4:
                search=[]
                file=command[0]#input("name file ? for no ")
                file_extension = "."+command[1]
                path= command[2]#"give me the path, $ = actualy dir, ? = all path, ** at end for large search "
                if command[3]=="-one":
                    one=True
                    command.remove("-one")
                    #nome;ext;path
                    if len(command)==3:
                        command.append("?+?")
                else:
                    one=False
                file_word=" ".join(command[3:len(command)])
                try:
                    if path[len(path)-2:]=="**":
                        search_long=True
                    else:
                        search_long=False
                except:
                    path=None

                if path[0]=="?":
                    path=primitive_path
                elif path[0]=="$":
                    path=os.getcwd()
                elif os.path.exists(path) and os.path.isdir(path):
                    path=path
                else:
                    path=None
                if path!=None:
                    if file=="?" and file_extension==".?" and file_word=="?+?":
                        print("error no parma for search file ")
                    else:
                        if search_long:
                            for paths, subdirs, files in os.walk(path):
                                if one==True and len(search)==1:
                                    break
                                for element in files:
                                    if one==True and len(search)==1:
                                        break
                                    nome=os.path.join(paths, element)

                                    if os.path.splitext(element)[0]==file:

                                        if file_extension!=".?" and file_extension==os.path.splitext(element)[1]:
                                            search.append(nome)
                                        elif file_extension==".?":
                                            search.append(nome)

                                    if file_extension == os.path.splitext(nome)[1]:
                                        if file!="?" and os.path.splitext(element)[0]==file:
                                            search.append(nome)
                                        elif file=="?":
                                            search.append(nome)

                                    if (file=="?" and file_extension==".?") and file_word!="?+?":
                                        type_search_word=True
                                        try:
                                            with open(nome,encoding="utf-8") as f:
                                                regex=re.compile(r''+file_word)
                                                file_read=f.readlines()
                                                for line in file_read:
                                                    line=line.strip()
                                                    if regex.search(line):
                                                        search.append(nome)
                                                        break
                                        except Exception as e:
                                            error_log("history",str(e))
                                            pass
                        else:
                            for x in os.listdir(path):
                                if one==True and len(search)==1:
                                    break
                                
                                if  file==os.path.splitext(x)[0]:
                                    if file_extension!=".?" and file_extension==os.path.splitext(x)[1]:
                                        search.append(r''+path+"\\"+x)
                                    
                                    elif file_extension==".?":
                                        search.append(r''+path+"\\"+x)

                                if file_extension == os.path.splitext(r''+path+"\\"+x)[1]:
                                    if file!="?" and file==os.path.splitext(x)[0]:
                                        search.append(r''+path+"\\"+x)
                                    elif file=="?":
                                        search.append(r''+path+"\\"+x)

                                if (file=="?" and file_extension==".?") and file_word!="?+?":
                                    type_search_word=True
                                    try:
                                        with open(r''+path+"\\"+x,encoding="utf-8") as f:
                                            regex=re.compile(r''+file_word)
                                            file_read=f.readlines()
                                            for line in file_read:
                                                line=line.strip()
                                                if regex.search(line):
                                                    search.append(r''+path+"\\"+x)
                                                    break
                                    except Exception as e:
                                        error_log("history",str(e))
                                        pass

                        search=list(set(search))
                        search_final=[]
                        checker=False
                        if file_word!="?+?" and type_search_word==False:

                            checker=True
                            regex=re.compile(r''+file_word)
                            for element in search:
                                try:
                                    with open(element,encoding="utf-8") as f:
                                        file_read=f.readlines()
                                        for line in file_read:
                                            line=line.strip()
                                            if regex.search(line):
                                                search_final.append(element)
                                                break

                                except Exception as e:
                                    error_log("history",str(e))
                                    pass

                        if checker==True:
                            search=search_final 
                        if len(search)==0:
                            search.append("not found")  
                        print(search)

                else:
                    print("error path not found")
            else:
                print("error no parma in input")
        


        elif command[0].lower() in ["editfile","edf","fileedit"]:
            command.pop(0)
            if len(command)==2:
                command.append(1)
            if len(command)>=3:
                file=command[0]
                command.pop(0)
                if os.path.exists(file):
                    try:
                        num_lines = sum(1 for line in open(file))
                    except Exception as e:
                        error_log("history",str(e))
                        print("error during file read ")

                        number_line=0
                    command_file=command[0]
                    line=int(command[1])
                    command.pop(0)
                    command.pop(0)
                    if line>num_lines:
                        print("error line too big")
                    else:
                        phrase=""
                        if len(command)!=0:
                            phrase=" ".join(command)
                        if command_file=="-read":
                            try:
                                with open(file,"r") as file_read:
                                    for line_number, lines in enumerate(file_read):
                                        if line==line_number+1:
                                            print(lines)
                                            break
                            except Exception as e:
                                error_log("history",str(e))
                                print("error during operetion")
                        elif command_file=="-getline":print(num_lines)
                        elif command_file=="-delete":
                            try:
                                with open(file,"r") as file_read:
                                    list_line=file_read.readlines()
                                with open(file,"w") as file_write:
                                    for line_number,lines in enumerate(list_line):
                                        if line_number+1==line:
                                            pass
                                        else:
                                            file_write.write(lines)
                            except Exception as e:
                                print("error during operetion")
                                error_log("history",str(e))
                        elif command_file=="-over":
                            try:
                                with open(file,"r") as file_read:
                                    list_line=file_read.readlines()
                                with open(file,"w") as file_write:
                                    for line_number,lines in enumerate(list_line):
                                        if line_number+1==line:
                                            file_write.write(phrase+"\n")
                                        else:
                                            file_write.write(lines)
                            except Exception as e:
                                print("error during operetion")
                                error_log("history",str(e))
                        elif command_file=="-append":
                            try:
                                with open(file,"r") as file_read:
                                    list_line=file_read.readlines()
                                with open(file,"w") as file_write:
                                    for line_number,lines in enumerate(list_line):
                                        if line_number+1==line:
                                            input(True)
                                            input(line_number+1)
                                            input(line)
                                            file_write.write(lines.strip()+" "+phrase)
                                        else:
                                            file_write.write(lines)   
                            except Exception as e:
                                error_log("history",str(e))
                                print("error during operetion")         


                else:
                    print("error path not found")
            else:
                print("error in command editfile")

        elif command[0]=="help":
            command.pop(0)
            if len(command)!=0:
                if command[0]=="-l":
                    print("history\nsudo\npwd\nprotection\nunprotection\nwifi\ncd\nmkdir\ngetsha\ncls\nusb\nrandom\nmore\nls\ncp\nmv\nrm\ninfo\nsrm\ngrep\nexit\ndownload\nmrm\necho\npc\nen\ndc\nscf\nedf")
                elif command[0]=="history":
                    print("print command hystory\n"+
                    "parma:\n"+
                    "> + file for write history in a file\n"+
                    ">>+ file for append history in a file without lost file data") 
                elif command[0]=="sudo":
                    print("get admin privilage")
                elif command[0]=="pwd":
                    print("current directory")     
                elif command[0]=="protection":
                    print("protect file with a bsod") 
                elif command[0]=="unprotection":
                    print("unprotect file with a bsod") 
                elif command[0]=="wifi":
                    print("help for your saved wifi\n"+
                    "parma:\n"+
                    "-ssid get the ssid\n"+
                    "-auth get the auth type\n"+
                    "-password get the wifi password\n"+
                    "-show show the qr code\n"+
                    "-save save the qr code" )
                elif command[0]=="cd":
                    print("change the current directory usage cd <directory>")
                elif command[0]=="mkdir":
                    print("create a new dir")
                elif command[0]=="getsha":
                    print("get sha256 of file o a word")
                elif command[0]=="cls":
                    print("clean the screen")
                elif command[0]=="usb":
                    print("access to usb menu")
                elif command[0]=="random":
                    print("generate a random number")
                    print("usage\n"+
                    "start number, finish number, many number")
                    print("parma:\n"+
                    "-duplicate\n"+
                    "-sort")
                elif command[0]=="more":
                    print("print the first 10 line of a file or more")
                    print("parma:\n"+
                    "-head + number [default is 10] first line"+
                    "-tail + number [default is 10] last line")
                elif command[0]=="ls":
                    print("print all file in a dir usage ls + dir")
                    print("parma:\n"+
                    "-l print long information\n"+
                    "-a print file in subdir too")
                elif command[0]=="cp":
                    print("copy file in a other directory ")
                elif command[0]=="mv":
                    print("move file in a other directory")
                elif command[0]=="rm":
                    print("remove element")
                    print("usage rm + file name or rm + -a for delete all file in cuurrent dir")
                    print("rm + directory + -d delete all file directory too")
                elif command[0]=="info":
                    print("requires:file_name\nopereation:all info for a file")
                elif command[0]=="srm":
                    print("same thinh of rm but more secure")
                elif command[0]=="grep":
                    print("find a specific word in a file\nusage grep file_name word\nparma search -s print only line number")
                elif command[0]=="exit":
                    print("close program")
                elif command[0]=="down":
                    print("download something on internet")
                    print("usage command + parma + site + dir")
                    print("parma:-file\n-site-js\n-site-css\nsite-image")
                elif command[0]=="mrm":
                    print("multi remove file in a dir")
                    print("usage command + path + parma + (optional) -srm")
                    print("parma:\n-duplicate delete all duplicate\n-ext delete specific extenion + extension (optional) -t delete all except specif extenzion\n-name delete specif name + name + (optiona) -t delete all file except with the specif name\nsize + size + parma (only one) [-mag,-min,-umag,-umin] specif if you want delete with higher size or less  ")
                elif command[0]=="echo":
                    print("print a string")
                    print("parma > or >> same type as history command")
                elif command[0]=="pc":
                    print("check your process")
                    print("parma: -kill + process name kill process\n-ch + process name check if process is running\n-all get information off all process")

                elif command[0]=="en":
                    print("encrypt a file with a password")
                    print("usage command + file name")
                elif command[0]=="dc":
                    print("decrypt a file with a password")
                    print("usage command + file name")
                elif command[0]=="scf":
                    print("search location off a specif file")
                    print("usage:\nfile name if is unknow use ?\n file exention if is unknow use ?\n path  = actualy dir, ? = all path, ** at end for large search\n special -one for only a file or add some text to search (long)")
                elif command[0]=="edf":
                    print("edit a file")
                    print("usage command + parma + line + text")
                    print("parma:\n-read\n-delete\n-over\n-append")
                    print("-geline get line number\n -reed read the specif line\n-delete delete the specif line\n-over over write the specif line\n-append add text at the end of the line")
                else:
                    print("error no command maybe is a allias")

                


                

                

            else:
                print("use help -l for see all command or help <command>")

        elif command[0]=="apt":
            if os.path.exists(plugin_path) is False:
                os.mkdir(plugin_path)
            command.pop(0)
            if len(command)==1:
                file_download=command[0]
                #DonwloadLib.download_file("https:\\site_to_donwload\\"+file_download)
                with zipfile.ZipFile(r''+plugin_path+"\\"+file_download+".zip",'r') as zip_ref:
                    zip_ref.extractall(plugin_path)
                os.remove(r''+plugin_path+"\\"+file_download+".zip")
                print("download done")
            else:
                print("error no file to download")

        elif command[0]=="plugin":
            command.pop(0)
            if len(command)==1:
                plugin_file=command[0]
                sys.path.append(r''+plugin_path+"\\"+plugin_file)
                filename = r''+plugin_path+"\\"+plugin_file+"\\main.py"
                input(filename)
                if os.path.exists(filename):
                    try:
                        exec(compile(open(filename, "rb").read(), filename, 'exec'), globals(), locals())
                    except ImportError:
                        print("error module not found")
                        filename=r''+plugin_path+"\\"+plugin_file+"\\requirements.txt"
                        if os.path.exists(filename):
                            os.system(r"pip install -r "+filename)
                        else:
                            print("error no requirements file found")
                    except Exception as e:
                        error_log("history",str(e))
                        print("unknow error")


        else:
            print("command not found")
            x=Correttore.Correttore(["apt","plugin","update","secret","hs","hy","history","sudo","pwd","protection","unprotection","wifi","cd","changedirectory","chd","md","mkd","mkdir","getsha","sha256","gtsh","get256","clear","cls","usb","more","mr","ls","listdir","lsdir","cp","copy","mv","move","rm","remove","srm","secureremove","grep","grp","gp","ex","exit","xexit","dn","down","download","mrm","multiremove","echo","pc","proc","process","en","encrypt","dc","decript","scf","search","rd","random","rnd","editfile","edf","fileedit"],1,command[0])
            if len(x)>1:
                x=" ".join(x)
            else:
                x="".join(x)
            if len(x)!=0:
                print("similar command " + "".join(x))
    except KeyboardInterrupt:
        pass                
         

                
            

input("press a key to stop")
os.remove(r''+delete_log_file+"\\loghshshshshshshshshhshsh.txt")





#TODO important



#TODO
#! Aggiungere where parma in ls
#! Salvare gli errori su un file di log 
#! autofixer (installa automaticamenti se mancano librerie)





