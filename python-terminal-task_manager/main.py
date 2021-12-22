nice_conta_file=0
test_echo_command_sha256=False
sys_type="$"


all_command_name_list=["load","echo","secret","hs","hy","history","update","sudo","pwd","protection","unprotection","wifi","cd","changedirectory","chd",
"md","mkd","mkdir","getsha","sha256","gtsh","get256","usb","rd","random","rnd","more","mr","-tail","-head","ls","listdir","lsdir",
"where","&dir","&file","&read","&write","&type","&size","cp","copy","mv","move","rm","remove","if","info","srm","secureremove",
"grep","grp","gp","ex","exit","xexit","clear","cls","tree","title","sleep","dn","down","download","-file","-name","-site-js","-site-css",
"-site-image","mrm","multiremove","-duplicate","pc","proc","process","en","encrypt","dc","decript","scf","search",
"editfile","edf","fileedit","help","apt","plugin","track","cat","convertroman","sort","uniq","wc","wc_word","wc_line","wc_character",
"wc_word_line","wc_character_line","wc_word_character","wc_word_character_line","diff","diff_line_word","diff_line","diff_character",
"du","chattr","gawk","watch","rev","send","get","randomfile","randomword","rank","findServer","rdemail","neofetch","touch","randomwordfromlist","song"]


#'\033[32m'

import os
import string
import platform
import stat
uname=platform.uname()

import msvcrt
os.system("")
try:
    from rich.console import Console 
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss rich lib run first installer.py")
    exit()

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
    input('\033[31m'+"you miss some file or file are corrupted please run installer.py with this code 1789")
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


try:
    import youtube_dl
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss youtube_dl lib run first installer.py")
    exit()

try:
    import pyperclip
    print(f"[+] success {nice_conta_file}")
    nice_conta_file+=1
except ImportError:
    input('\033[31m'+"miss pyperclip lib run first installer.py")
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
import webbrowser
    
print("press a key to continue")
msvcrt.getch()
os.system('cls' if os.name=='nt' else 'clear')



try:
    with urllib.request.urlopen("https://nicholas-the-null.github.io/py_manager_website/stats.json") as url:data = json.loads(url.read().decode())
except:
    data=None

try:
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter
    from prompt_toolkit.shortcuts import message_dialog
    from prompt_toolkit.application import in_terminal, run_in_terminal
    from prompt_toolkit.key_binding import KeyBindings
    bindings = KeyBindings()


    

except ImportError:
    input('\033[31m'+"miss prompt lib run first installer.py")
    exit()

import ctypes

counter_error_passer=0



usb_active=False



#######################################################freeboting function original author in command section #########################################################################



def generateUserName():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))
    return username

def extract():
    getUserName = re.search(r'login=(.*)&',newMail).group(1)
    getDomain = re.search(r'domain=(.*)', newMail).group(1)
    return [getUserName, getDomain]

# Got this from https://stackoverflow.com/a/43952192/13276219
def print_statusline(msg: str):
    last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    print_statusline.last_msg = msg

def deleteMail():
    url = 'https://www.1secmail.com/mailbox'
    data = {
        'action': 'deleteMailbox',
        'login': f'{extract()[0]}',
        'domain': f'{extract()[1]}'
    }

    print_statusline("Disposing your email address - " + mail + '\n')
    req = requests.post(url, data=data)

def checkMails():
    reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
    req = requests.get(reqLink).json()
    length = len(req)
    if length == 0:
        print_statusline("Your mailbox is empty. Hold tight. Mailbox is refreshed automatically every 5 seconds.")
    else:
        idList = []
        for i in req:
            for k,v in i.items():
                if k == 'id':
                    mailId = v
                    idList.append(mailId)

        x = 'mails' if length > 1 else 'mail'
        print_statusline(f"You received {length} {x}. (Mailbox is refreshed automatically every 5 seconds.)")

        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'All Mails')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        for i in idList:
            msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
            req = requests.get(msgRead).json()
            for k,v in req.items():
                if k == 'from':
                    sender = v
                if k == 'subject':
                    subject = v
                if k == 'date':
                    date = v
                if k == 'textBody':
                    content = v

            mail_file_path = os.path.join(final_directory, f'{i}.txt')

            with open(mail_file_path,'w') as file:
                file.write("Sender: " + sender + '\n' + "To: " + mail + '\n' + "Subject: " + subject + '\n' + "Date: " + date + '\n' + "Content: " + content + '\n')





#############################################################################################################################################################################
console = Console()
history=[]
primitive_path=r'C:\\Users\\'+str(getuser())
var_old=0

correct_path=r''+__file__
correct_path=correct_path[:-8]
original_usb=os.getcwd()
load_var=False

setup_path=r''+correct_path+"\\"+"setup.txt"
under_watch=False
plugin_path=r''+correct_path+"\\plugin"
error_log_path=r''+correct_path+"\\log.txt"
setup_path=r''+correct_path+"\\setup.txt"
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
    with open(error_log_path,"a",encoding="utf-8") as logs:
        logs.write("error at "+ora+" in command " + command + " with this message " + error +"\n")
    if counter_error_passer%5==0:
        print("error if you want report please send log.txt file text to https://github.com/Nicholas-the-Null/py-manager/issues")

def save_debug(command,text):
    ora=datetime.now()
    ora=ora.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    test_list=[]
    with open(setup_path,"r") as file:
        for x in file.readlines():test_list.append(x.split(' '))
    file.close()
    if test_list[2][1].strip()=="True":
        with open(r''+correct_path+"\\debug.txt","a",encoding="utf-8") as logs:
            logs.write("debug at "+ora+" in command " + str(command) +" " + str(text) +"\n")



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
    return False

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


def get_display_name():
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = 3
 
    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)
 
    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    return nameBuffer.value


forbidden_charter_data_set={'/':'',':':'','*':'','?':'','"':'','<':'','>':'','|':''}

def forbidden_charter(text,dict=forbidden_charter_data_set):
    for i, j in dict.items():
        text = text.replace(i, j)
    return text

def convert_to_roman(number):
    roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman_num = ''
    for i in sorted(roman.keys())[::-1]:
        roman_num += roman[i] * (number // i)
        number %= i
    return roman_num

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



if update=="True":

    test_list=[]
    with open(setup_path,"r") as file:
        for x in file.readlines():test_list.append(x.split(' '))
    if test_list[0][1].strip()=="True":
        message_dialog(
        title='update',
        text='a new update is online ').run()



################################################################################################
##############################shortcuts########################################################
@bindings.add("f4")
def _(event):
    exit()
        #event.app.current_buffer.insert_text("hello world")
@bindings.add("f5")
async def _(event):
    global var_old
    #ctypes.windll.user32.MessageBoxW(0, str(var_old), "Your title", 1)
    try:
        event.app.current_buffer.text=""
        
        #ctypes.windll.user32.MessageBoxW(0, str(len(history)-var_old-1), "Your title", 1)
        #ctypes.windll.user32.MessageBoxW(0, str(len(history)-1), "Your title", 1)
        event.app.current_buffer.insert_text(history[len(history)-var_old-1])
        var_old+=1
    except Exception as e:
        pass
        #ctypes.windll.user32.MessageBoxW(0, str(e), "errore di debug", 1)




@bindings.add("f6")
def _(event):
    try:
        event.app.current_buffer.insert_text(pyperclip.paste())
    except Exception as e:
        pass


################################################################################################
##############################shortcuts########################################################


console.print("""[green] 
  _____       __  __                                   
 |  __ \     |  \/  |                                  
 | |__) |   _| \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 |  ___/ | | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |   | |_| | |  | | (_| | | | | (_| | (_| |  __/ |   
 |_|    \__, |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
         __/ |                          __/ |          
        |___/                          |___/           
""" +"[/green]")

print("")

protect=False

multiple_command=[]
multi_command_parse=[]
multi_command_string=""
multi_command_parse_string=""

save_debug("start","terminal started")

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
            ##all_command_name_list
            if load_var==False:
                auto_completer=WordCompleter(all_command_name_list,ignore_case=True)
            else:
                auto_completer=WordCompleter(all_command_name_list+os.listdir(),ignore_case=True)

            command=prompt(str(echo_off)+" "+sys_type+">",completer=auto_completer,key_bindings=bindings).split()
            save_debug(command,"input")
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
            var_old=0
            

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
                save_debug("usb error","usb removed or else")
            
        if len(command)==0:
            command=["echo","no command in input"]

        if command[0].lower() in ["hs","hy","history"]:#history of command
            if len(command)==3:
                commando=command[1]
                file=command[2]
                try:
                    if os.path.exists(file) is False:
                        file=forbidden_charter(file)
                        x=open(file,"w+")
                        x.close()
                except Exception as e:
                    error_log("history",str(e))
                if commando==">":commando="w"
                elif commando==">>":commando="a"
                else:commando=None
                if commando !=None:
                    try:
                        with open(file,commando,encoding="utf-8") as f:
                            for numero,nome in enumerate(history):
                                f.write(str(numero+1)+ " " +str(nome)+"\n")
                    except Exception as e:
                        print("error file not valid "+ str(e))
                        error_log("history",str(e))
                        save_debug("history",str(e))

                else:
                    print("error invalid operator")
                    save_debug("history","invalid operator")
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
            test_list=[]
            with open(setup_path,"r") as file:
                for x in file.readlines():
                    test_list.append(x.split(' '))
            if test_list[1][1].strip()=="True":
                password=prompt("password: your name ", is_password=True)
                if password==get_display_name():
                    if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)==42:
                        exit()
                    else:
                        save_debug("sudo","abbort")
                else:
                    save_debug("sudo","wrong password")
            else:
                print("sudo is disable")
                save_debug("sudo","disable")
          
            
        elif command[0].lower()=="pwd":print(os.getcwd())

        elif command[0]=="protection":
            if sys_type=="#" and protect==False:
                SetProtection()
                protect=True
                print("ok")
            else:
                print("error")
                save_debug("protection","no sudo")

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
                        os.chdir(directory)
                        save_debug("cd","create a new directory "+ directory)
            except Exception as e:
                if Confirm.ask("Do you want return to home dir?"):
                    os.chdir(r'C:\\Users\\'+os.getlogin())
                    save_debug("cd","return to home dir")
                else:
                    console.print("[red]ok"+"[/red]")


        elif command[0].lower()=="song":
            command.pop(0)
            if len(command)==0:
                print("error no command")
            else:
                song=" ".join(command)
                info = youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{1}:{song}", download=False, ie_key="YoutubeSearch")
                result=[]
                for x in info["entries"]:
                    result.append("https://www.youtube.com/watch?v="+x["id"])
                webbrowser.open(result[0])
                save_debug("song","open "+result[0])

        elif command[0].lower() in ["md","mkd","mkdir"]: #create dir
            #create dir use forbidden_charter()  function for check dir name
            #-p for create parent directory
            command.pop(0)
            if len(command)==0:
                console.print("[red]error no name in input"+"[/red]")
            else:
                if os.path.exists(command[0]):
                    console.print("[red]error directory already exists"+"[/red]")
                    save_debug("md","directory already exists")
                else:
                    try:
                        file_name=forbidden_charter(command[0])
                        if "-p" in command:
                            os.makedirs(file_name,exist_ok=True)
                            save_debug("md","create directory "+file_name+" with parent directory")
                        else:
                            file_name=file_name.replace("\\","")
                            save_debug("md","create directory "+file_name)
                            os.mkdir(file_name)
                    except Exception as e:
                        print(str(e))
                        error_log("mkd",str(e))

        elif command[0].lower() in ["getsha","sha256","gtsh","get256"]: #sha256 of file or string
            command.pop(0)
            if os.path.exists(command[0]) and os.path.isdir(command[0])==False:
                input_type= "-file" 
                result=main.asset.secure.file_sha256.File_calcolatore_sha256(command[0])
                save_debug("getsha","sha256 of file "+command[0])
            else:
                input_type="-string" 
                result=main.asset.secure.file_sha256.String_calcolatore_sha256(command[0])
                save_debug("getsha","sha256 of string "+command[0])
            
            table=Table(title="info")
            table.add_column("useriput",no_wrap=True,style="blue")
            table.add_column("type",style="magenta")
            table.add_column("sha256",no_wrap=True,style="green")
            table.add_row(command[0],input_type,result)
            console.print(table)

        

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
                        save_debug("usb","go on usb "+usb)
                        break
                    except:
                        if danger==False:
                            print("usb removed")
                            save_debug("usb","usb removed")
                    

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
                        save_debug("rd","error too few with duplicate parma will be disable")
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
                    save_debug("rd","random "+str(start)+" "+str(finish)+" "+str(many) + str(return_list))
                except ValueError:
                    save_debug("rd","error value")
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
                            with open(command[0],'r',encoding="utf-8") as Read_file:
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
                            save_debug("more","read file "+command[0])
                        else:
                            if command[1].lower()=="-tail":
                                number=10
                                if not len(command)==2:number=int(command[2])
                                with open(command[0],'r',encoding="utf-8") as Read_file:
                                    file_contenent=Read_file.readlines()

                                num_lines = sum(1 for line in open(command[0]))

                                for number_line,line in enumerate(file_contenent):
                                    # x = 21-10


                                    if number_line>=num_lines-number:
                                        print(line.strip())
                                        save_debug("more","tail "+str(number)+" "+command[0])
                                    else:
                                        pass



                                

                            elif command[1].lower()=="-head":
                                number=10
                                if not len(command)==2:number=int(command[2])
                                with open(command[0],'r',encoding="utf-8") as Read_file:
                                    file_contenent=Read_file.readlines()
                                for number_line,line in enumerate(file_contenent):
                                    if number_line==number:break
                                    else:
                                        print(line.strip())
                                        save_debug("more","more -head "+command[0])


                            else:
                                console.print(f"[red]error parma {command[1]} not found"+"[/red]")
                                save_debug("more","error parma "+command[1]+" not found")

                    except Exception as e:
                        console.print("[red]error i cant read file"+"[/red]")
                        error_log("more",str(e))
                        save_debug("more",str(e))
                else:
                    console.print("[red]error file not found"+"[/red]")
                    save_debug("more","file not found")

            else:
                console.print("[red]error no file in input"+"[/red]")
                save_debug("more","no file in input")


        


        elif command[0].lower() in ["ls","listdir","lsdir"]: #ls command print all file in a dir -l for long description -a for include all subdir and his file
            command.pop(0)#parma
            interupt=False
            parameter=None
            output_ls=True
            checker=5
            if len(command)==5:checker=4
            if not len(command)==0:
                if os.path.exists(command[0]) and os.path.isdir(command[0]):
                    directory=command[0]
                    command.pop(0)
                else:
                    directory=os.getcwd()
                if "where" in command:
                    pos=command.index("where")
                    if pos!=len(command)-1:

                        parameter=command[pos+1]
                        if parameter not in ["&dir","&file","&read","&write","&type","&size"]:
                            parameter=None
                            command.pop(pos)
                        else:
                            
                            if parameter=="&size":
                                if len(command)-1>=checker:
                                    typus=[command[pos+2],command[pos+3]]
                                    command.pop(pos)
                                    command.pop(pos)
                                else:
                                    parameter=None
                                    typus=[None,"None"]

                            if parameter=="&type":
                                if pos+1!=len(command)-1:
                                    typus=command[pos+2]
                                    command.pop(pos)
                                else:
                                    typus=None
                            command.pop(pos)
                            command.pop(pos)
                    else:
                        parameter=None
                        command.pop(pos)
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
                                            size=str(round(os.path.getsize(nome)/(1024),3))
                                            read=str(os.access(nome,os.R_OK))[0]
                                            write=str(os.access(nome,os.W_OK))[0]

                                            if parameter!=None:
                                               

                                                if (parameter=="&size" and typus[0]!=None) and (typus[0] in [">",">=","<=","<","=="] and typus[1].isnumeric()):
                                                    if typus[0]==">" and int(float(size)) > int(typus[1]):
                                                        output_ls=True
                                                    
                                                    elif typus[0]==">=" and int(float(size))>=int(typus[1]):
                                                        output_ls=True
                                            
                                                    elif typus[0]=="<" and int(typus[1])>int(float(size)):
                                                        output_ls=True
                                                    elif typus[0]=="<=" and int(typus[1]) >= int(float(size)):
                                                        output_ls=True
                                                    
                                                    elif typus[0]=="==" and int(typus[1]) == int(float(size)):
                                                        output_ls=True
                                                    
                                                    else:
                                                        output_ls=False
                                                    



                                                if parameter=="&type" and typus!=os.path.splitext(nome)[1]:
                                                    output_ls=False
                                                if parameter=="&read" and read=="T":
                                                    output_ls=False
                                                if parameter=="&write" and write=="T":
                                                    output_ls=False
                                                if output_ls==True:
                                                    table.add_row(str(numero),str(GetShortPathName(nome)),is_dir,size,tempo,read,write)
                                                    numero+=1
                                                if output_ls==False:
                                                    output_ls=True
                                            else:
                                                table.add_row(str(numero),str(GetShortPathName(nome)),is_dir,size,tempo,read,write)
                                                numero+=1
                                        except (Exception,KeyboardInterrupt) as e:
                                            print(e)
                                            if str(e)=="":
                                                interupt=True
                                                break
                                            pass
                        except KeyboardInterrupt:
                            interupt=True

                        try:
                            if interupt==False:
                                console.print(table)
                        except :pass


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
                                    size=str(round(os.path.getsize(nome)/(1024),3))
                                    read=str(os.access(nome,os.R_OK))[0]
                                    write=str(os.access(nome,os.W_OK))[0]

                                    if parameter!=None:
                                        if (parameter=="&size" and typus[0]!=None) and (typus[0] in [">",">=","<=","<","=="] and typus[1].isnumeric()):
                                            if typus[0]==">" and int(float(size)) > int(typus[1]):
                                                output_ls=True
                                            
                                            elif typus[0]==">=" and int(float(size))>=int(typus[1]):
                                                output_ls=True
                                    
                                            elif typus[0]=="<" and int(typus[1])>int(float(size)):
                                                output_ls=True
                                            elif typus[0]=="<=" and int(typus[1]) >= int(float(size)):
                                                output_ls=True
                                            
                                            elif typus[0]=="==" and int(typus[1]) == int(float(size)):
                                                output_ls=True
                                            
                                            else:
                                                output_ls=False
                                        if parameter=="&type" and typus!=os.path.splitext(nome)[1]:
                                            output_ls=False
                                        if parameter=="&dir" and is_dir=="T":
                                            output_ls=False
                                        if parameter=="&file" and is_dir=="F":
                                            output_ls=False
                                        if parameter=="&read" and read=="F":
                                            output_ls=False
                                        if parameter=="&write" and write=="F":
                                            output_ls=False
                                        if output_ls==True:
                                            table.add_row(str(numero),str(GetShortPathName(nome)),is_dir,size,tempo,read,write)
                                            numero+=1
                                        else:
                                            output_ls=True
                                    else:
                                        
                                        table.add_row(str(numero),str(GetShortPathName(nome)),is_dir,size,tempo,read,write)
                                        numero+=1

                                except (Exception,KeyboardInterrupt) as e:
                                    print(e)
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
                        console.print(f"[red]error parma are wrong "  +"[/red]")
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
                        console.print("[red]error i cant create new file "+str(e)+"[/red]")
                        error_log("cp",str(e))
                        save_debug("cp",str(e))
                else:
                    console.print("[red]file not found"+"[/red]")
                    save_debug("cp","file not found")
            else:
                console.print("[red]not parma in input"+"[/red]")
                save_debug("cp","not parma in input")



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
                            save_debug("mv",f"file {command[0]} moved in {command[1]}")
                        except Exception as e:
                            console.print("[red]error i cant create new file "+str(e)+"[/red]")
                            error_log("move",str(e))
                            save_debug("move",str(e))
                    else:
                        console.print("[red]file not found"+"[/red]")
                        save_debug("move","file not found")
                else:
                    console.print("[red]file not found"+"[/red]")
                    save_debug("move","file not found")
            else:
                console.print("[red]not parma in input"+"[/red]")
                save_debug("move","not parma in input")

        

        elif command[0].lower() in ["rm","remove"]: #remove file
            command.pop(0)
            path_command=os.getcwd()
            for x in command:
                if x=="$":
                    path_command=os.getcwd()
                    break
                if x.startswith("$"):
                    path_command=x
                    path_command=path_command.replace("$","")
            if path_command!=os.getcwd():
                command.remove("$"+path_command)
            if os.path.isdir(path_command):
                pass
            else:
                if os.path.exists(r''+os.getcwd()+"\\"+path_command):
                    path_command=r''+os.getcwd()+"\\"+path_command
                else:
                    print("path not found")
                    command=["paass"]
            if len(command)>0:
                for parma in command:
                    if parma=="*":
                        for x in os.listdir(path_command):
                            try:
                                if os.path.isdir(r''+path_command+"\\"+x):
                                    shutil.rmtree(x,ignore_errors=True)
                                else:
                                    os.remove(r''+path_command+"\\"+x)
                            except Exception as e:
                                print(f"i cant remove this file {x} for this reason {e} ")

                    elif parma.startswith("*"):
                        #if start with parma delete file
                        parma=parma.replace("*","")
                        for x in os.listdir(path_command):
                            if x.startswith(parma):
                                try:
                                    if os.path.isdir(r''+path_command+"\\"+x):pass
                                    else:os.remove(r''+path_command+"\\"+x)
                                except Exception as e:
                                    print(f"i cant remove this file {x} for this reason {e} ")
                    elif parma.endswith("*"):
                        #if end with parma no ext delete file
                        parma=parma.replace("*","")
                        for x in os.listdir(path_command):
                            filename= os.path.splitext(x)[0]
                            if filename.endswith(parma):
                                try:
                                    if os.path.isdir(r''+path_command+"\\"+x):pass
                                    else:os.remove(r''+path_command+"\\"+x)
                                except Exception as e:
                                    print(f"i cant remove this file {x} for this reason {e} ")
                    else:
                        if os.path.isfile(parma):
                            try:
                                os.remove(parma)
                            except Exception:
                                print("error i cant remove file")
                        elif os.path.isdir(parma):
                            if "-d" in command:
                                shutil.rmtree(parma,ignore_errors=True)
                            else:
                                for x in os.listdir(parma):
                                    path=r''+parma+"\\"+x
                                    try:
                                        if os.path.isfile(path):
                                            os.remove(path)
                                        else:
                                            pass
                                    except Exception as e:
                                        pass
                        else:
                            if os.path.isdir(r''+os.getcwd()+"\\"+parma):
                                if "-d" in command:
                                    shutil.rmtree(parma,ignore_errors=True)
                                    os.rmdir(r''+os.getcwd()+"\\"+parma)
                            else:
                                pass
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
                        error_log("info",str(e))
                else:
                    print("error file not dound or is a dir")
            else:
                print("parma not found")




        elif command[0].lower()=="export":
            command.pop(0)
            if len(command)>=1:
                file=command[0]
                file=forbidden_charter(file)
                with open(file,"w") as f:
                    for x in history:
                        f.write(x+"\n")
            else:
                print("parma not found")

        elif command[0].lower() in ["srm","secureremove"]: #secure rfemove file
            command.pop(0)
            if len(command)==1:
                if os.path.exists(command[0]) and os.path.isdir(command[0])== False:
                    main.asset.secure.cripta.Delete_File(command[0])
                    os.remove(command[0])
                else:
                    console.print("[red]file not found"+"[/red]")
            else:
                console.print("[red]not parma in input"+"[/red]")

        elif command[0].lower() in ["grep","grp","gp"]: #print line where a string parma -i for regex use and -s for print only number of line parma -i first
            command.pop(0)
            try:
                count=0
                if os.path.exists(command[0]) and os.path.isdir(command[0])==False:
                    if not len(command)==1:
                        parola=command[1]
                        if parola=="%email%":
                            parola="""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
                        elif parola=="%ipv4%":
                            parola="""'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b'"""
                        regex=re.compile(r''+parola)                  
                        with open(command[0],"r",encoding="utf-8") as file:
                            filee=file.readlines()
                        for line in filee:
                            if regex.search(line):
                                if "-s" not in command:
                                    #print(str(count) + " "+ line.strip())
                                    stringa_completa="" 
                                    line_list=line.split()
                                    for x in line_list:
                                        if regex.search(x) is not None:
                                            x="[red]"+x+"[/red]"
                                        else:
                                            x="[grey]"+x+"[/grey]"
                                        x=x.replace("'","")
                                        stringa_completa+=x+" "
                                    if stringa_completa=="":
                                        stringa_completa=line
                                    try:
                                        console.print(str(count)+" "+stringa_completa.replace("\n",""))
                                    except:
                                        stringa_completa=stringa_completa.replace("[grey]","")
                                        stringa_completa=stringa_completa.replace("[/grey]","")
                                        stringa_completa=stringa_completa.replace("[red]","")
                                        stringa_completa=stringa_completa.replace("[/red]","")
                                        print(str(count)+" "+stringa_completa.replace("\n",""))



                                count+=1
                        print("count " + str(count))

                    else:
                        console.print("[red]not parma in input"+"[/red]")

                else:
                    console.print("[red]file not found"+"[/red]")
            except Exception as e:
                print("error in regx read")
                error_log("grep",str(e))
        
        elif command[0] in ["ex","exit","xexit"]:
            #exit to porgram ask conferm use Confirm.ask("do you want to exit")
            #-f for force exit
            #-s for save history on file name of in input
            #-fa for force exit and save history on file name of in input
            #create a new for save history on file
            #use try except for save history on file
            #time.sleep(2)
            if "-f" in command:
                exit()
            elif "-s" in command:
                if len(command)==2:
                    try:
                        with open(command[1],"w",encoding="utf-8") as file:
                            file.write(str(console.history))
                    except Exception as e:
                        print("error in save history on file")
                        error_log("exit",str(e))
                else:
                    console.print("[red]not parma in input"+"[/red]")
            elif "-fa" in command:
                if len(command)==2:
                    try:
                        with open(command[1],"w",encoding="utf-8") as file:
                            file.write(str(console.history))
                    except Exception as e:
                        print("error in save history on file")
                        error_log("exit",str(e))
                else:
                    console.print("[red]not parma in input"+"[/red]")
                exit()
            else:
                if Confirm.ask("do you want to exit"):
                    exit()
                else:
                    console.print("[red]exit canceled"+"[/red]")

        elif command[0] in ["clear","cls"]:
            #clear screen
            #-h for clean history
            #-f 
            #-hs for clean screen and history
            if len(command)==1:
                os.system("cls")
            elif "-h" in command:
                history=[]
                var_old=0
            elif "-hs" in command:
                history=[]
                os.system("cls")
                var_old=0
            else:
                pass
        
        elif command[0]=="tree":
            #create directory tree
            command.pop(0)
            if len(command)==0:
                console.print("[red]not parma in input"+"[/red]")
            else:
                try:
                    for x in command:
                        if x=="$":x=os.getcwd()
                        if os.path.isdir(x):
                            print(x)
                            for root, dirs, files in os.walk(x):
                                level = root.replace(x, '').count(os.sep)
                                indent = ' ' * 4 * (level)
                                print('{}{}/'.format(indent, os.path.basename(root)))
                                subindent = ' ' * 4 * (level + 1)
                                for f in files:
                                    print('{}{}'.format(subindent, f))
                        else:
                            console.print("[red]file not found"+"[/red]")
                except Exception as e:
                    print("error in tree")
                    error_log("tree",str(e))
        

        elif command[0]=="title":
            #change title of console
            #title + command
            command.pop(0)
            if len(command)>=1:
                title=command[0]
                os.system("title "+title)
            else:
                console.print("[red]not parma in input"+"[/red]")
        
        
        











        elif command[0]=="sleep":
            #sleep for time in input
            command.pop(0)
            if len(command)>0:
                try:
                    timer_sleep=int(command[0])
                    time.sleep(timer_sleep)

                except ValueError:
                    print("requires a number")
            else:
                pass
        


        elif command[0] in ["dn","down","download"]:
            #! tipo download sito cartella 
            #download something from site to folder
            #type of download url directory
            name=None 
            path=None
            original=os.getcwd()
            command.pop(0)
            if not len(command)==0:
                if command[0]=="-file":
                    command.pop(0)
                    #link path -name name 
                    if len(command)!=0:
                        link=command[0]
                        command.pop(0)
                        if len(command)!=0:
                            if os.path.exists(command[0]) and os.path.isdir(command[0]):
                                path=command[0]
                                os.chdir(path)
                                command.pop(0)
                            elif command[0]=="-name":
                                path=None
                                pass
                            else:
                                print("error path not found")
                                path=None
                            if command[0]=="-name" and len(command)==2:
                                name=command[1]
                            else:
                                name=None

                        result=DonwloadLib.download_file(link)
                        if result[0]=="success":
                            if name!=None:
                                try:
                                    os.rename(result[1],name)
                                except Exception:
                                    print("Error name not valid")
                            if path!=None:
                                os.chdir(original)
                        else:
                            console.print(result)
                    else:
                        console.print("[red]error parma dont match"+"[/red]")

                elif command[0]=="-site-js":
                    command.pop(0)
                    if not len(command)==0:
                        if len(command)==2:
                            if os.path.exists(command[1]):os.chdir(command[1])
                            else:console.print("[red]error dir not found"+"[/red]")
                        result=DonwloadLib.js(command[0])
                        
                        if not result=="Success":console.print(result)
                        os.chdir(original)
                        
                    else:
                        console.print("[red]error parma dont match"+"[/red]")

                elif command[0]=="-site-css":
                    command.pop(0)
                    if not len(command)==0:
                        if len(command)==2:
                            if os.path.exists(command[1]):os.chdir(command[1])
                            else:console.print("[red]error dir not found"+"[/red]")
                        result=DonwloadLib.css(command[0])
                        
                        if not result=="Success":console.print(result)
                        os.chdir(original)
                        
                    else:
                        console.print("[red]error parma dont match"+"[/red]")



                elif command[0]=="-site-image":
                    command.pop(0)
                    if not len(command)==0:
                        if len(command)==2:
                            if os.path.exists(command[1]):os.chdir(command[1])
                            else:console.print("[red]error dir not found"+"[/red]")
                        
                        
                        letters = string.ascii_lowercase
                        x= ''.join(random.choice(letters) for i in range(13))
                        print(f"because this command generate a lot of image we create a new temporany dir [{x}]")
                        os.mkdir(x)
                        os.chdir(x)
                        result=DonwloadLib.image(command[0])
                        
                        if not result=="Success":console.print(result)
                        os.chdir(original)
                        
                    else:
                        console.print("[red]error parma dont match"+"[/red]")


                else:
                    console.print("[red]error parma dont match"+"[/red]")

                        

            else:
                console.print("[red]error no parma in input "+"[/red]")
            pass
        

        

        elif command[0] in ["mrm","multiremove"]:
            #sistemare eccezione per file non eliminabuli
            
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
                                    console.print("[red]you miss parma in input "+"[/red]")
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
                                    console.print("[red]you miss parma in input "+"[/red]")
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
                                                console.print("[red]your parma are wrong "+"[/red]")
                                                file_list=[]
                                        else:
                                            console.print("[red]you miss parma in input "+"[/red]")
                                            file_list=[]
                                    except ValueError:
                                        console.print("[red]your parma are wrong "+"[/red]")
                                        file_list=[]


                                else:
                                    console.print("[red]you miss parma in input "+"[/red]")
                                    file_list=[]



                            else:file_list=[]
                                
                                    
                                    
                        else:
                            console.print("[red]error no parma in input "+"[/red]")
                            os.chdir(original)




                        if len(file_list)!=0:
                            for element in file_list:
                                if sicuro==True:
                                    try:
                                        main.asset.secure.cripta.Delete_File(element)
                                    except Exception:
                                        pass
                                try:
                                    os.remove(element)
                                except Exception:
                                    pass
                            os.chdir(original)
                        else:
                            console.print("[red]no file to delete "+"[/red]")
                            os.chdir(original)

                        






                    


                    else:
                        console.print("[red]error no parma in input "+"[/red]")
                        os.chdir(original)



                else:
                    console.print(f"[red]error {command[0]} dir not found "+"[/red]")
                    os.chdir(original)
            else:
                console.print("[red]error no parma in input "+"[/red]")
            
    

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
                            error_log("echo",str(e))
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
                        console.print("[red]error miss parma "+"[/red]")
                    else:
                        try:
                            if command[save_number]==">":
                                file_name=forbidden_charter(command[save_number+1])
                                with open(file_name,'w+',encoding="utf-8") as file:
                                    file.write(out)
                            else:
                                with open(file_name,'a',encoding="utf-8") as file:
                                    file.write("\n"+out)
                        except:
                            console.print("[red]error invalid file name "+"[/red]")



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
                                error_log("pc",str(e))
                        else:pass
                    else:
                        console.print("[red]error no parma [/red]")
                if command[0] in ["-ch","-check","-ck"]:
                    command.pop(0)
                    if len(command)!=0:
                        if checkIfProcessRunning(command[0]):
                            print("running")
                        else:
                            print("not running")
                    else:
                        console.print("[red]error no parma [/red]")

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
                console.print("[red]error no parma [/red]")
        





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
                        check=True
                        if command[0][len(command[0])-3:]=="AES":
                            sure=input("this file syntax match with our encrypt style are you sure y wanna encrypt again?[y/other]").lower()
                            if sure=="n":
                                check=False
                        if check==True:
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
            delete=None
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
                                                    delete=True
                                                except Exception as e:
                                                    print("password wrong")
                                                    error_log("decript",str(e))
                                        except ValueError:
                                            os.remove(file+"decriptato"+estensione)
                                    try:
                                        
                                        if delete==True:
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
                                        delete=True
                                        print("password wrong")
                                        error_log("decript",str(e))
                                        if os.path.exists(command[0]+"decriptato"+estensione):
                                            os.remove(command[0]+"decriptato"+estensione)
                                        
                            except ValueError:
                                if os.path.exists(command[0]+"decriptato"+estensione):
                                    os.remove(command[0]+"decriptato"+estensione)
                        try:
                            if delete==True:
                                os.remove(file)
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
                                            error_log("scf",str(e))
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
                                        error_log("scf",str(e))
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
                                    error_log("scf",str(e))
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
                        num_lines = sum(1 for line in open(file,encoding="utf-8"))
                    except Exception as e:
                        error_log("edf",str(e))
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
                                with open(file,"r",encoding="utf-8") as file_read:
                                    for line_number, lines in enumerate(file_read):
                                        if line==line_number+1:
                                            if lines=="\n":
                                                pass
                                            else:
                                                print(lines)
                                            break
                            except Exception as e:
                                error_log("edf",str(e))
                                print("error during operetion")
                        elif command_file=="-getline":print(num_lines)
                        elif command_file=="-delete":
                            try:
                                with open(file,"r",encoding="utf-8") as file_read:
                                    list_line=file_read.readlines()
                                with open(file,"w",encoding="utf-8") as file_write:
                                    for line_number,lines in enumerate(list_line):
                                        if line_number+1==line:
                                            pass
                                        else:
                                            file_write.write(lines)
                            except Exception as e:
                                print("error during operetion")
                                error_log("edf",str(e))
                        elif command_file=="-over":
                            try:
                                with open(file,"r",encoding="utf-8") as file_read:
                                    list_line=file_read.readlines()
                                with open(file,"w",encoding="utf-8") as file_write:
                                    for line_number,lines in enumerate(list_line):
                                        if line_number+1==line:
                                            file_write.write(phrase+"\n")
                                        else:
                                            file_write.write(lines)
                            except Exception as e:
                                print("error during operetion")
                                error_log("edf",str(e))
                        elif command_file=="-append":
                            try:
                                with open(file,"r",encoding="utf-8") as file_read:
                                    list_line=file_read.readlines()
                                with open(file,"w",encoding="utf-8") as file_write:
                                    for line_number,lines in enumerate(list_line):
                                        if line_number+1==line:
                                            file_write.write(lines.strip()+" "+phrase)
                                        else:
                                            file_write.write(lines)   
                            except Exception as e:
                                error_log("edf",str(e))
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
                elif command[0]=="apt":
                    print("install a plugin usage apt link_plugin")
                elif command[0]=="plugin":
                    print("use a installed plugib usage plugin plugin_name")
                elif command[0]=="track":
                    print("parma ip address")
                    print("track ip")
                elif command[0]=="cat":
                    print("concatenete two file usage cat file1 file2")
                    print("parma you can use file3 for concatene text in a single file if you use file 3 you can use -duplicate for not add duplicate sentence")
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
            if len(command)>=1:
                plugin_file=command[0]
                if plugin_file=="-list":
                    if os.path.exists(plugin_path) is False:
                        os.mkdir(plugin_path)
                        print("dir was not found created")
                    else:
                        counter=0
                        for file in os.listdir(plugin_path):
                            if os.path.isdir(r''+plugin_path+"\\"+plugin_file):
                                print(file)
                                counter+=1
                        if counter==0:
                            print("no file found")
                elif plugin_file=="-hash":
                    if len(command)>=2:
                        sys.path.append(r''+plugin_path+"\\"+command[1])
                        filename = r''+plugin_path+"\\"+command[1]+"\\main.py"
                        print(main.asset.secure.file_sha256.File_calcolatore_sha256(filename))

                    else:
                        print("no file in input")
                elif plugin_file=="-remove":
                    if len(command)>=2:
                        sys.path.append(r''+plugin_path+"\\"+command[1])
                        filename = r''+plugin_path+"\\"+command[1]
                        shutil.rmtree(filename,ignore_errors=True)
                        
                        

                    else:
                        print("no file in input")
                else:
                    sys.path.append(r''+plugin_path+"\\"+plugin_file)
                    filename = r''+plugin_path+"\\"+plugin_file+"\\main.py"
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
        elif command[0]=="track":
            command.pop(0)
            if len(command)>=1:
                ip=command[0]
                link="http://ip-api.com/json/"+ip
                response=requests.get(link)
                if response.status_code==200:
                    response=response.json()
                    if response["status"]=="success":
                        print("country:"+response["country"]+"\nregion Name:"+response["regionName"]+"\ncity:"+response["city"]+"\nisp:"+response["isp"])
                        pass
                    else:
                        print("ip not found")
                else:
                    print("error site down")
            else:
                print("error no ip in command")

        elif command[0]=="cat":
            command.pop(0)
            duplicate=None
            if len(command)>=2:
                if (os.path.exists(command[0]) and os.path.isfile(command[0])) and (os.path.exists(command[0]) and os.path.isfile(command[1])):
                    file1=command[0]
                    file2=command[1]
                else:
                    file1=None
                if len(command)>=3:
                    file3=command[2]
                    if len(command)>3:
                        if command[3]=="-duplicate":
                            duplicate=True

                else:
                    file3=None
                
                if file1!=None:
                    if file3 == None:
                        with open(file1,"r",encoding="utf-8") as file_read:
                            file_read_dataset=file_read.readlines()
                        file_read.close()
                        with open(file2,"a",encoding="utf-8") as file_write:
                            for sentence in file_read_dataset:
                                file_write.write(sentence)
                        file_write.close()
                    else:
                        with open(file1,"r",encoding="utf-8") as file_read:
                            file_read_dataset_1=file_read.readlines()
                        file_read.close()
                        with open(file2,"r",encoding="utf-8") as file_read:
                            file_read_dataset_2=file_read.readlines()
                        file_read.close()
                        try:
                            file3=forbidden_charter(file3)
                            with open(file3,"w",encoding="utf-8") as file_write:
                                data_set=file_read_dataset_1+file_read_dataset_2
                                if duplicate==True:
                                    data_set=list(set(data_set))
                                for sentence in data_set:file_write.write(sentence)
                        except Exception:
                            print(f"error file name not valid for {file3} ")

                else:
                    print("error in file input")

            else:
                print("error no parma in input")



        elif command[0]=="convertroman":
            #function to number convert to roman number format
            command.pop(0)
            if len(command)>=1:
                number=command[0]
                if number.isdigit():
                    number=int(number)
                else:
                    number=None
                if number!=None:
                    #convert number to roman numeral
                    roman_number=convert_to_roman(number)
                    print(roman_number)
                    
                
            else:
                print("error")

        
                

           
            




        elif command[0]=="sort":
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]

                if len(command)>=2:
                    try:
                        if command[1]=="-line":
                            if len(command)>=3:
                                if command[2].isdigit():
                                    position=int(command[2])
                                    if position>=1:
                                        if os.path.exists(file_name):
                                            with open(file_name,"r",encoding="utf-8") as file_read:
                                                file_read_dataset=file_read.readlines()
                                            file_read.close()
                                            file_read_dataset.sort(key=lambda x: x.split(" ")[position-1])
                                            with open(file_name,"w",encoding="utf-8") as file_write:
                                                for sentence in file_read_dataset:
                                                    file_write.write(sentence)
                                            file_write.close()
                                        else:
                                            print("error file not found")
                                    else:
                                        print("error position not valid")
                                else:
                                    print("error position not valid")
                            else:
                                print("error no position in input")
                    except:
                        pass
                    else:
                        print("error no option in input")
                else:
                    print("error no option in input")


        elif command[0] == "uniq":
            #delete duplicate line in a file 
            #-d optional for write duplicate line in a another file
            #else delete duplicate line in the same file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if len(command)>=2:
                    if command[1]=="-d":
                        if len(command)>=3:
                            if os.path.exists(file_name):
                                with open(file_name,"r",encoding="utf-8") as file_read:
                                    file_read_dataset=file_read.readlines()
                                file_read.close()
                                file_read_dataset=list(set(file_read_dataset))
                                with open(command[2],"w",encoding="utf-8") as file_write:
                                    for sentence in file_read_dataset:
                                        file_write.write(sentence)
                                file_write.close()
                            else:
                                print("error file not found")
                        else:
                            print("error no file in input")
                    else:
                        with open(file_name,"w",encoding="utf-8") as file_write:
                            for sentence in file_read_dataset:
                                file_write.write(sentence)
                        file_write.close()
                else:
                    print("error no option in input")
        
        elif command[0]=="wc":
            #count the number of line,word and character in a file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    line_count=0
                    word_count=0
                    character_count=0
                    for sentence in file_read_dataset:
                        line_count+=1
                        word_count+=len(sentence.split(" "))
                        character_count+=len(sentence)
                    print(f"{line_count} {word_count} {character_count}")
                else:
                    print("error file not found")
            else:
                print("error no file in input")

        elif command[0]=="wc_word":
            #count the number of word in a file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    word_count=0
                    for sentence in file_read_dataset:
                        word_count+=len(sentence.split(" "))
                    print(word_count)
                else:
                    print("error file not found")
            else:
                print("error no file in input")

        elif command[0]=="wc_line":
            #count the number of line in a file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    line_count=0
                    for sentence in file_read_dataset:
                        line_count+=1
                    print(line_count)
                else:
                    print("error file not found")
            else:
                print("error no file in input")

        elif command[0]=="wc_character":
            #count the number of character in a file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    character_count=0
                    for sentence in file_read_dataset:
                        character_count+=len(sentence)
                    print(character_count)
                else:
                    print("error file not found")
            else:
                print("error no file in input")

        elif command[0]=="wc_word_line":
            #count the number of word and line in a file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    line_count=0    
                    word_count=0
                    for sentence in file_read_dataset:
                        line_count+=1
                        word_count+=len(sentence.split(" "))
                    print(f"{line_count} {word_count}")
                else:  
                    print("error file not found")
            else:
                print("error no file in input")
        
        elif command[0]=="wc_character_line":  
            #count the number of character and line in a file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    line_count=0    
                    character_count=0
                    for sentence in file_read_dataset:
                        line_count+=1
                        character_count+=len(sentence)
                    print(f"{line_count} {character_count}")
                else:  
                    print("error file not found")
            else:
                print("error no file in input")

        elif command[0]=="wc_word_character":
            #count the number of word and character in a file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    word_count=0    
                    character_count=0
                    for sentence in file_read_dataset:
                        word_count+=len(sentence.split(" "))
                        character_count+=len(sentence)
                    print(f"{word_count} {character_count}")
                else:  
                    print("error file not found")
            else:
                print("error no file in input")

        elif command[0]=="wc_word_character_line":
            #count the number of word,character and line in a file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    line_count=0    
                    word_count=0
                    character_count=0
                    for sentence in file_read_dataset:
                        line_count+=1
                        word_count+=len(sentence.split(" "))
                        character_count+=len(sentence)
                    print(f"{line_count} {word_count} {character_count}")
                else:  
                    print("error file not found")
            else:
                print("error no file in input")



        


        
        elif command[0]=="diff":
            #compare two file
            command.pop(0)
            if len(command)>=2:
                file_name1=command[0]
                file_name2=command[1]
                if os.path.exists(file_name1) and os.path.exists(file_name2):
                    with open(file_name1,"r",encoding="utf-8") as file_read1:
                        file_read_dataset1=file_read1.readlines()
                    file_read1.close()
                    with open(file_name2,"r",encoding="utf-8") as file_read2:
                        file_read_dataset2=file_read2.readlines()
                    file_read2.close()
                    if len(file_read_dataset1)==len(file_read_dataset2):
                        for i in range(len(file_read_dataset1)):
                            if file_read_dataset1[i]!=file_read_dataset2[i]:
                                print(f"{i+1} {file_read_dataset1[i]}")
                    else:
                        print("error file not same")
                else:
                    print("error file not found")
            else:
                print("error no file in input")

        elif command[0]=="diff_word":
            #compare two file
            command.pop(0)
            if len(command)>=2:
                file_name1=command[0]
                file_name2=command[1]
                if os.path.exists(file_name1) and os.path.exists(file_name2):
                    with open(file_name1,"r",encoding="utf-8") as file_read1:
                        file_read_dataset1=file_read1.readlines()
                    file_read1.close()
                    with open(file_name2,"r",encoding="utf-8") as file_read2:
                        file_read_dataset2=file_read2.readlines()
                    file_read2.close()
                    if len(file_read_dataset1)==len(file_read_dataset2):
                        for i in range(len(file_read_dataset1)):
                            if file_read_dataset1[i].split(" ")!=file_read_dataset2[i].split(" "):
                                print(f"{i+1} {file_read_dataset1[i]}")
                    else:
                        print("error file not same")
                else:
                    print("error file not found")
            else:
                print("error no file in input")

        elif command[0]=="diff_character":
            #compare two file
            command.pop(0)
            if len(command)>=2:
                file_name1=command[0]
                file_name2=command[1]
                if os.path.exists(file_name1) and os.path.exists(file_name2):
                    with open(file_name1,"r",encoding="utf-8") as file_read1:
                        file_read_dataset1=file_read1.readlines()
                    file_read1.close()
                    with open(file_name2,"r",encoding="utf-8") as file_read2:
                        file_read_dataset2=file_read2.readlines()
                    file_read2.close()
                    if len(file_read_dataset1)==len(file_read_dataset2):
                        for i in range(len(file_read_dataset1)):
                            if file_read_dataset1[i]!=file_read_dataset2[i]:
                                print(f"{i+1} {file_read_dataset1[i]}")
                    else:
                        print("error file not same")
                else:
                    print("error file not found")
            else:
                print("error no file in input")

        elif command[0]=="diff_line":
            #compare two file
            command.pop(0)
            if len(command)>=2:
                file_name1=command[0]
                file_name2=command[1]
                if os.path.exists(file_name1) and os.path.exists(file_name2):
                    with open(file_name1,"r",encoding="utf-8") as file_read1:
                        file_read_dataset1=file_read1.readlines()
                    file_read1.close()
                    with open(file_name2,"r",encoding="utf-8") as file_read2:
                        file_read_dataset2=file_read2.readlines()
                    file_read2.close()
                    if len(file_read_dataset1)==len(file_read_dataset2):
                        for i in range(len(file_read_dataset1)):
                            if file_read_dataset1[i].split(" ")!=file_read_dataset2[i].split(" "):
                                print(f"{i+1} {file_read_dataset1[i]}")
                    else:
                        print("error file not same")
                else:
                    print("error file not found")

        elif command[0]=="diff_line_word":
            #compare two file
            command.pop(0)
            if len(command)>=2:
                file_name1=command[0]
                file_name2=command[1]
                if os.path.exists(file_name1) and os.path.exists(file_name2):
                    with open(file_name1,"r",encoding="utf-8") as file_read1:
                        file_read_dataset1=file_read1.readlines()
                    file_read1.close()
                    with open(file_name2,"r",encoding="utf-8") as file_read2:
                        file_read_dataset2=file_read2.readlines()
                    file_read2.close()
                    if len(file_read_dataset1)==len(file_read_dataset2):
                        for i in range(len(file_read_dataset1)):
                            if file_read_dataset1[i].split(" ")!=file_read_dataset2[i].split(" "):
                                print(f"{i+1} {file_read_dataset1[i]}")
                    else:
                        print("error file not same")
                else:
                    print("error file not found")

        elif command[0]=="du":
            #calcolate directory size
            command.pop(0)
            if len(command)>=1:
                directory_name=command[0]
                if os.path.exists(directory_name):
                    directory_size=0
                    for root, dirs, files in os.walk(directory_name):
                        for file in files:
                            file_path = os.path.join(root, file)
                            directory_size += os.path.getsize(file_path)
                    print(f"{directory_size}")
                else:
                    print("error directory not found")
            else:
                print("error no directory in input")
        
        elif command[0]=="chattr":
            #change attribute of file
            command.pop(0)
            if len(command)>=2:
                file_name=command[0]
                attribute=command[1]
                if os.path.exists(file_name):
                    if attribute=="+i":
                        os.chmod(file_name,stat.S_IWUSR)
                    elif attribute=="-i":
                        os.chmod(file_name,stat.S_IWUSR|stat.S_IWGRP|stat.S_IWOTH)
                    elif attribute=="+r":
                        os.chmod(file_name,stat.S_IRUSR)
                    elif attribute=="-r":
                        os.chmod(file_name,stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH)
                    elif attribute=="+w":
                        os.chmod(file_name,stat.S_IWUSR)
                    elif attribute=="-w":
                        os.chmod(file_name,stat.S_IWUSR|stat.S_IWGRP|stat.S_IWOTH)
                    elif attribute=="+x":
                        os.chmod(file_name,stat.S_IXUSR)
                    elif attribute=="-x":
                        os.chmod(file_name,stat.S_IXUSR|stat.S_IXGRP|stat.S_IXOTH)
                    else:
                        print("error attribute not found")
                else:
                    print("error file not found")
            else:
                print("error no file in input")
        
        elif command[0]=="gawk":
            #filter file
            command.pop(0)
            if len(command)>=2:
                file_name=command[0]
                filter_word=command[1]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    for i in range(len(file_read_dataset)):
                        if filter_word in file_read_dataset[i]:
                            print(f"{i+1} {file_read_dataset[i]}")
                else:
                    print("error file not found")
            else:
                print("error no file in input")
        
        elif command[0] == "watch":
            #watch file and save in TempoLOG .txt and change under_watch variable
            # if under_watch==True:
            # if file change then save log and print log
            # if file not change then dont print log
            # if file not exist then dont print log
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    if under_watch==False:
                        under_watch=True
                        with open(file_name,"r",encoding="utf-8") as file_read:
                            file_read_dataset=file_read.readlines()
                        file_read.close()
                        with open("TempoLOG.txt","w",encoding="utf-8") as file_write:
                            for i in range(len(file_read_dataset)):
                                file_write.write(f"{i+1} {file_read_dataset[i]}")
                        file_write.close()
                        print("TempoLOG.txt created")
                    else:
                        with open(file_name,"r",encoding="utf-8") as file_read:
                            file_read_dataset=file_read.readlines()
                        file_read.close()
                        with open("TempoLOG.txt","r",encoding="utf-8") as file_read_log:
                            file_read_log_dataset=file_read_log.readlines()
                        file_read_log.close()
                        if len(file_read_dataset)==len(file_read_log_dataset):
                            for i in range(len(file_read_dataset)):
                                if file_read_dataset[i].split(" ")!=file_read_log_dataset[i].split(" "):
                                    print(f"{i+1} {file_read_dataset[i]}")
                                    with open("TempoLOG.txt","w",encoding="utf-8") as file_write:
                                        for i in range(len(file_read_dataset)):
                                            file_write.write(f"{i+1} {file_read_dataset[i]}")
                                    file_write.close()
                                    under_watch=False
                        else:
                            print("error file have more line")
                            under_watch=False
                            os.remove("TempoLOG.txt")
                else:
                    print("error file not found")
            else:
                print("error no file in input")
    
        elif command[0]=="rev":
            #reverse file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    file_read_dataset.reverse()
                    with open(file_name,"w",encoding="utf-8") as file_write:
                        for i in range(len(file_read_dataset)):
                            file_write.write(f"{i+1} {file_read_dataset[i]}")
                    file_write.close()
                else:
                    print("error file not found")
            else:
                print("error no file in input")
        
        elif command[0]=="send":
            #send data to remote server using requests.post() method
            #optional username and password
            command.pop(0)
            if len(command)>=2:
                url=command[0]
                data=command[1]
                if len(command)>=3:
                    username=command[2]
                    password=command[3]
                    r=requests.post(url,data=data,auth=(username,password))
                else:
                    r=requests.post(url,data=data)
                print(r.text)
            else:
                print("error no url or data in input")
        
        elif command[0]=="get":
            #get data from remote server using requests.get() method
            #optional username and password
            command.pop(0)
            if len(command)>=1:
                url=command[0]
                if len(command)>=3:
                    username=command[2]
                    password=command[3]
                    r=requests.get(url,auth=(username,password))
                else:
                    r=requests.get(url)
                print(r.text)
            else:
                print("error no url in input")


        elif command[0]=="randomwordfromlist":
            command.pop(0)
            print(random.choice(command))

        elif command[0]=="load":
            if load_var==False:
                load_var=True
                print("load")
            else:
                load_var=False
                print("unload")
    
        elif command[0]=="randomfile":
            #seach random file in directory
            #optional directory
            command.pop(0)
            if len(command)>=1:
                directory=command[0]
                if directory=="$":
                    directory=os.getcwd()
                if os.path.exists(directory):
                    file_list=os.listdir(directory)
                    random_file=random.choice(file_list)
                    print(f"{directory}/{random_file}")
                else:
                    print("error directory not found")
            else:
                print("error no directory in input")


        elif command[0]=="randomword":
            #random word in a file in input
            #optional file
            command.pop(0)
            if len(command)>=1:
                file_name=command[0]
                if os.path.exists(file_name):
                    with open(file_name,"r",encoding="utf-8") as file_read:
                        file_read_dataset=file_read.readlines()
                    file_read.close()
                    random_word=random.choice(file_read_dataset)
                    print(random_word)
                else:
                    print("error file not found")
            else:
                print("error no file in input")
        

            



            




    
        elif command[0]=="rank":
            #rank file in directory on size
            #-i for compare only files with same extension
            #-r for reversed rank
            reverse=False
            file_list=[]
            command.pop(0)
            if len(command)>=1:
                directory=command[0]
                if directory=="$":
                    directory=os.getcwd()
                if os.path.exists(directory) and os.path.isdir(directory):
                    if "-r" in command:
                        reverse=True
                    if "-i" in command:
                        try:
                            extension=command[command.index("-i")+1]
                        except Exception as e:
                            print(e)
                            print("error no extension in input")
                            extension=""
                        if extension!="":
                            file_list=os.listdir(directory)
                            file_list_extension=[]
                            for i in range(len(file_list)):
                                if file_list[i].split(".")[-1]==extension:
                                    file_list_extension.append(file_list[i])
                            file_list=file_list_extension
                    else:
                        file_list=os.listdir(directory)
                    file_list_size=[]
                    for i in range(len(file_list)):
                        file_list_size.append(os.path.getsize(f"{directory}/{file_list[i]}"))
                    file_list_size_rank=[]
                    for i in range(len(file_list_size)):
                        file_list_size_rank.append(file_list_size[i])
                    if reverse==True:
                        file_list_size_rank.sort(reverse=True)
                    else:
                        file_list_size_rank.sort()
                    for i in range(len(file_list_size_rank)):
                        for j in range(len(file_list)):
                            if file_list_size_rank[i]==file_list_size[j]:
                                print(f"{i+1} {file_list[j]}")
                                break
                else:
                    print("error directory not found")
            else:
                print("error no directory in input")

        
        elif command[0]=="findServer":
            #find file in dir remote server in input
            #optional username and password
            command.pop(0)
            if len(command)>=1:
                server_url=command[0]
                if len(command)>=2:
                    data=command[1]
                    if len(command)>=4:
                        username=command[2]
                        password=command[3]
                        r=requests.get(server_url,data=data,auth=(username,password))
                    else:
                        r=requests.get(server_url,data=data)
                    print(r.text)
                else:
                    print("error no data in input")
            else:
                print("error no url in input")

        
        elif command[0]=="rdemail":
            #by https://github.com/sameera-madushan/Mail-Swipe
            #name Sameera Madushan
            #thank you for create this awesome repository
            API = 'https://www.1secmail.com/api/v1/'
            domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
            domain = random.choice(domainList)
            command.pop(0)
            domaint="N"
            if len(command)==2:
                if command[0].lower()=="y":
                    domaint=command[1]
                    newMail = f"{API}?login={domaint}&domain={domain}"
            else:newMail = f"{API}?login={generateUserName()}&domain={domain}"
            reqMail = requests.get(newMail)
            mail = f"{extract()[0]}@{extract()[1]}"
            print("\nYour temporary email is " + mail + " (Email address copied to clipboard.)" + "\n")
            print(f"---------------------------- | Inbox of {mail} | ----------------------------\n")
            print("CTRL+C=exit from this command")
            try:
                while True:
                    checkMails()
                    time.sleep(5)
            except KeyboardInterrupt:
                deleteMail()
            
            

        elif command[0]=="neofetch":
            boot_time_timestamp = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time_timestamp)
            print(f""" 
                       /\_____/\\
                      /  o   o  \\
                     ( ==  ^  == )
                      )         (
                     (          )
                    ( (  )   (  ) )
                   (__(__)___(__)__)\n
                   system : {uname.system} {uname.version}\n
                   terminal version {version}\n
                   boot time {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n
                   processor info {uname.processor}\n 
                   memory info {psutil.virtual_memory().total//(1024*1024*1024)}GB""")
        elif command[0]=="touch":
            #file1.txt file.txt file3.txt file4.txt
            #file 1 to 4 ext
            command.pop(0)
            create=True
            if "to" in command:
                miin=0
                maxi=0
                step=1
                if len(command)-1>=4:

                    name=forbidden_charter(command[0])
                    try:
                        miin=int(command[1])
                        maxi=int(command[3])
                    except ValueError:
                        create=False
                        pass
                    if miin>maxi:
                        maxi,miin=miin,maxi
                    if len(command)-1==5:
                        try:
                            step=int(command[5])
                        except:
                            pass
                    if create==True:
                        for miin in range(miin,maxi+1,step):
                            with open(name+str(miin)+"."+command[4],"w+") as file_create:
                                file_create.close()
                    else:
                        print("error")

                else:
                    print("error in parma insertion")
            else:
                if len(command)!=0:
                    for x in command:
                        x=forbidden_charter(x)
                        with open(x,"w+") as file_create:
                            file_create.close()
                else:
                    print("no file in input")

        else:
            print("command not found")
            x=Correttore.Correttore(all_command_name_list,command[0])
            if len(x)>1:
                x=" ".join(x)
            else:
                x="".join(x)
            if len(x)!=0:
                print("similar command " + "".join(x))
    except KeyboardInterrupt:
        print("\n")
        pass                
         

                
            


#TODO
#add command to create file in dir with random name
#add command to create file in dir with random name and random ext
#add command to create file in dir with random name and random ext and random size
#add command for find 