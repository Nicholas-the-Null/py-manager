try:
    from rich.console import Console 
except ImportError:
    input("miss rich lib run first installer.py")
    exit()

import os
import subprocess

try:
    from rich.table import Table
except ImportError:
    input("miss rich lib run first installer.py")
    exit()

try:
    from rich.prompt import Confirm
except ImportError:
    input("miss rich lib run first installer.py")
    exit()
from datetime import datetime
import platform

try:
    import main.asset.secure.file_sha256
    import main.asset.secure.cripta
    import main.asset.Down.DonwloadLib as DonwloadLib
    import main.asset.multi_delete as multi_delete
except ImportError:
    input("you miss some file please run installer.py with this code 1789")
import sys
import time
import shutil
import re
try:
    from tqdm import tqdm
except ImportError:
    input("miss tqm lib run first installer.py")
    exit()
try:
    import pyAesCrypt 
except ImportError:
    input("miss pyAesCrypt lib run first installer.py")
    exit()

try:
    import requests
except ImportError:
    input("miss request lib run first installer.py")


from getpass import getpass,getuser
import random ,string
from datetime import datetime
import urllib.request, json
import psutil

try:
    with urllib.request.urlopen("https://nicholas-the-null.github.io/py_manager_website/stats.json") as url:data = json.loads(url.read().decode())
except:
    data=None


import ctypes, sys

import keyboard



shortcut = 'alt+x' #define your hot-key


def on_triggered(): #define your function to be executed on hot-key press
    pass
    
keyboard.add_hotkey(shortcut, on_triggered) 






console = Console()
history=[]
primitive_path=r'C:\\Users\\'+str(getuser())

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
    

elif data.get("sha256")!=main.asset.secure.file_sha256.File_calcolatore_sha256(sys.argv[0]):
    table.add_column("update",style="red",no_wrap=True)
    update="True"
else:
    table.add_column("update",style="green",no_wrap=True)
    update="False"

table.add_row(str(datetime.now()),str(platform.uname().system),"1.0",
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

while True:
    
    if is_admin():
        sys_type="#"
    else:
        sys_type="$"
        
    command=console.input("[green]"+str(os.getcwd())+" "+sys_type+"[/]>").split()
    history.append(" ".join(command))

    if command[0].lower() in ["hs","hy","history"]: #history of command
        table = Table(title="history")
        table.add_column("numero",style="magenta")
        table.add_column("command",style="green",no_wrap=True)
        for numero,nome in enumerate(history):
            table.add_row(str(numero),str(nome))
        
        console.print(table)

    elif command[0]=="sudo":
        if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)==42:
            exit()
        
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


    
    elif command[0]=="update":
        #downlaod file
        console.print(data)

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

    elif command[0].lower() in ["getsha","sha256","gtsh","get256"]: #sha256 of file or string
        command.pop(0)
        if os.path.exists(command[0]):
            input_type= "File" 
            result=main.asset.secure.file_sha256.File_calcolatore_sha256(command[0])
        else:
            input_type="string" 
            result=main.asset.secure.file_sha256.String_calcolatore_sha256(command[0])
        
        table=Table(title="info")
        table.add_column("useriput",no_wrap=True,style="blue")
        table.add_column("type",style="magenta")
        table.add_column("sha256",no_wrap=True,style="green")
        table.add_row(command[0],input_type,result)
        console.print(table)

    elif command[0].lower() in ["clear","cls"]:
        os.system("cls")

    elif command[0].lower() in ["more","mr"]: # read file head for print first line default is 10 and tail for the last line
        command.pop(0)
        if not len(command)==0:
            if os.path.exists(command[0]):
                try:
                    if len(command)==1:
                        with open(command[0],'r') as Read_file:
                            file_contenent=Read_file.readlines()
                        for number_line,line in enumerate(file_contenent):
                            if number_line==10:
                                if not Confirm.ask("more"):
                                    break
                                else:
                                    number_line=0
                            else:
                                print(line.strip())
                    else:
                        if command[1].lower()=="tail":
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



                            

                        elif command[1].lower()=="head":
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

                except PermissionError:
                    console.print("[red]error i cant read file"+"[/]")
            else:
                console.print("[red]error file not found"+"[/]")

        else:
            console.print("[red]error no file in input"+"[/]")


    elif command[0].lower() in ["ls","listdir","lsdir"]: #ls command print all file in a dir -l for long description -a for include all subdir and his file
        command.pop(0)#parma
        if not len(command)==0:
            if os.path.exists(command[0]):
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
                    for path, subdirs, files in os.walk(directory):
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
                            except Exception as e:
                                print(str(e))
                                continue
                    console.print(table)


                elif command[0]=="-l":
                    table=Table(title="file")
                    table.add_column("#", style="magenta")
                    table.add_column("name", style="red")
                    table.add_column("is_dir", style="green")
                    table.add_column("size",style="blue")
                    table.add_column("creation",style="cyan") 
                    table.add_column("read",style="yellow")
                    table.add_column("write",style="#008B8B")
                    for numero,nome in enumerate(os.listdir(directory)):
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
                        except Exception as e:
                            print(str(e))
                            continue
                    console.print(table)



                elif command[0]=="-a":
                    table=Table(title="file")
                    table.add_column("nome",style="magenta")
                    for path, subdirs, files in os.walk(directory):
                        for element in files:
                            table.add_row(os.path.join(path, element))
                    console.print(table)

                else:
                    console.print(f"[red]error parma are wrong "  +"[/]")
            else:
                table=Table(title="file")
                table.add_column("name",style="magenta")
                for x in os.listdir(directory):
                    table.add_row(x)
                console.print(table)
        else:
            table=Table(title="file")
            table.add_column("name",style="magenta")
            for x in os.listdir():
                table.add_row(x)
            console.print(table)



    elif command[0].lower() in ["cp","copy"]: #copy file in another dir
        command.pop(0)
        if len(command)>1:
            if os.path.exists(command[0]):
                try:
                    shutil.copyfile(command[0],command[1])
                except:
                    console.print("[red]error i cant create new file"+"[/]")
            else:
                console.print("[red]file not found"+"[/]")
        else:
            console.print("[red]not parma in input"+"[/]")

    elif command[0].lower() in ["mv","move"]: #move file in another folder
        command.pop(0)
        if len(command)>1:
            if os.path.exists(command[0]):
                try:
                    shutil.move(command[0],command[1])
                    #os.remove(command[0])
                except:
                    console.print("[red]error i cant create new file"+"[/]")
            else:
                console.print("[red]file not found"+"[/]")
        else:
            console.print("[red]not parma in input"+"[/]")

    elif command[0].lower() in ["rm","remove"]: #remove file
        command.pop(0)
        if len(command)==1:
            if os.path.exists(command[0]):
                os.remove(command[0])
            else:
                console.print("[red]file not found"+"[/]")
        else:
            console.print("[red]not parma in input"+"[/]")
    
    elif command[0].lower() in ["srm","secureremove"]: #secure rfemove file
        command.pop(0)
        if len(command)==1:
            if os.path.exists(command[0]):
                main.asset.secure.cripta.Delete_File(command[0])
                os.remove(command[0])
            else:
                console.print("[red]file not found"+"[/]")
        else:
            console.print("[red]not parma in input"+"[/]")

    elif command[0].lower() in ["grep","grp","gp"]: #print line where a string parma -i for regex use and -s for print only number of line parma -i first
        command.pop(0)
        count=0
        if os.path.exists(command[0]):
            if not len(command)==1:
                
                parola=command[1]
                if len(command)==3:
                    if command[2]=="-i":
                        parola=parola.lower()+"|"+parola[0].capitalize()
                regex=re.compile(parola)
                with open(command[0],"r") as file:
                    filee=file.readlines()
                for line in filee:
                    if regex.search(line):
                        if "-s" not in command:
                            print(line)
                        count+=1
                print(count)

            else:
                console.print("[red]not parma in input"+"[/]")

        else:
            console.print("[red]file not found"+"[/]")
    
    elif command[0] in ["ex","exit"]:
        if Confirm.ask("Do you want exit?"):
            print("ok bye have a nice day :)")
            time.sleep(3)
            exit()
        else:
            pass

    elif command[0] in ["dn","down","download"]:
        #! tipo download sito cartella  
        original=os.getcwd()
        command.pop(0)
        if not len(command)==0:
            if command[0]=="file":
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

            elif command[0]=="site-js":
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

            elif command[0]=="site-css":
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



            elif command[0]=="site-image":
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
        if not len(command)==0:
            if os.path.exists(command[0]):
                os.chdir(command[0])
                command.pop(0)
                if not len(command)==0:

                    if command[0] in ["-srm","-secureremove"]:
                        sicuro=True
                        command.pop(0)
                    else:sicuro=False
                    
                    
                    if not len(command)==0:
                        if command[0]=="-duplicate":
                            print("qui")
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
                console.print("[red]error path not found "+"[/]")
                os.chdir(original)
        else:
            console.print("[red]error no parma in input "+"[/]")
        
    elif command[0] in ["en","encrypt"]:
        command.pop(0)
        if len(command)!=0:
            if os.path.exists(command[0]):
                file=r''+command[0]
                command.pop(0)
                if command[0]=="key":
                    enc=main.asset.secure.cripta.encrypt(file)
                    print(enc)
                    main.asset.secure.cripta.Delete_File(file)
                    os.remove(file)
                    if Confirm.ask("Do you want save password?"):
                        with open("key-"+file+".key", "wb") as key_file:key_file.write(enc)
                    
                elif command[0]=="password":
                    bufferSize = 1024 * 1024
                    password=getpass("give me the password ")
                    with open(file, "rb") as fIn:
                        with open(file+"aes", "wb") as fOut:
                            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
                    main.asset.secure.cripta.Delete_File(file)
                    os.remove(file)
                    
                else:
                    console.print("[red]your parma are wrong "+"[/]")
                
            else:
                console.print("[red]error path not found "+"[/]")


        else:
            console.print("[red]error no parma in input "+"[/]")
        

    elif command[0]=="echo":
        command.pop(0)
        out=""
        out_format="monitor"
        save_number=0
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
                    under_string=str(datetime.now())


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
            if command[0] in ["kill","kl"]:
                command.pop(0)
                if len(command)!=0:
                    if checkIfProcessRunning(command[0]):
                        try:
                            subprocess.call("taskkill /F /IM " + command[0])
                        except Exception as e:
                            print("error "+str(e))
                    else:pass
                else:
                    console.print("[red]error no parma [/]")
            if command[0] in ["ch","check","ck"]:
                command.pop(0)
                if len(command)!=0:
                    if checkIfProcessRunning(command[0]):
                        print("running")
                    else:
                        print("not running")
                else:
                    console.print("[red]error no parma [/]")

            elif command[0] in ["all","l"]:
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





    
    





            

    

#TODO process info   - criptografia

                
            




