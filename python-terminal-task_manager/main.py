try:
    from rich.console import Console 
except ImportError:
    input("miss rich lib run first installer.py")
    exit()

import os

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
try:
    import win32api
except ImportError:
    input("miss winapi lib please run installer.py")
    exit()
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


from getpass import getpass
import random ,string



console = Console()
history=[]


table = Table(title="info")
table.add_column("time",style="magenta")
table.add_column("os",style="green",no_wrap=True)
table.add_column("version",style="purple",no_wrap=True)
table.add_column("sha256",style="#A52A2A",no_wrap=True)
table.add_column("update",style="cyan",no_wrap=True)

table.add_row(str(datetime.now()),str(platform.uname().system),"1.0",
main.asset.secure.file_sha256.File_calcolatore_sha256(sys.argv[0]),"False")

console.print(table)



while True:
    

        
    command=console.input("[green]"+str(os.getcwd())+"[/]>").split()
    history.append(" ".join(command))

    if command[0].lower() in ["hs","hy","history"]: #history of command
        table = Table(title="history")
        table.add_column("numero",style="magenta")
        table.add_column("command",style="green",no_wrap=True)
        for numero,nome in enumerate(history):
            table.add_row(str(numero),str(nome))
        console.print(table)

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
                os.mkdir(command[0])

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
            if os.path.exists(command[0]) is True:
                if os.path.isdir(command[0]):
                    if len(command)==1:
                        table=Table(title="file")
                        table.add_column("name",style="magenta",no_wrap=True)
                        for element in os.listdir(command[0]):
                            table.add_row(element)
                        console.print(table)
                        
                    elif len(command)==2:
                        if command[1]=="-l":
                            table=Table(title="file")
                            table.add_column("#", style="magenta", no_wrap=True)
                            table.add_column("name", style="red",no_wrap=True)
                            table.add_column("is_dir",no_wrap=True, style="green")
                            table.add_column("size",style="blue",no_wrap=True)
                            table.add_column("creation",style="cyan",no_wrap=True) 
                            table.add_column("read",style="yellow",no_wrap=True)
                            table.add_column("write",style="#008B8B",no_wrap=True)
                            for numero,nome in enumerate(os.listdir(command[0])):
                                try:
                                    nome1=nome
                                    
                                    nome=r''+command[0]+"\\"+nome1
                                    table.add_row(str(numero),nome1,str(os.path.isdir(nome))
                                    ,str(round(os.path.getsize(nome)/(1024*1024),3))
                                    ,str(time.ctime(os.path.getctime(nome)))
                                    ,str(os.access(nome,os.R_OK)),
                                    str(os.access(nome,os.W_OK)))
                                    
                                except:
                                    continue
                            console.print(table)
                        elif command[1]=="-a":
                            table=Table(title="file")
                            table.add_column("nome",style="magenta",no_wrap=True)
                            for path, subdirs, files in os.walk(command[0]):
                                for element in files:
                                    table.add_row(os.path.join(path, element))
                            console.print(table)

                        else:
                            console.print("[red]parma are wrong"+"[/]")

                    else:
                        if (command==[command[0],"-l","-a"] or command==[command[0],"-a","-l"]):
                            table=Table(title="file")
                            table.add_column("#", style="magenta", no_wrap=True)
                            table.add_column("path", style="red",no_wrap=True)
                            table.add_column("is_dir",no_wrap=True, style="green")
                            table.add_column("size",style="blue",no_wrap=True)
                            table.add_column("creation",style="cyan",no_wrap=True) 
                            table.add_column("read",style="yellow",no_wrap=True)
                            table.add_column("write",style="#008B8B",no_wrap=True)
                            numero=0
                            for path, subdirs, files in os.walk(command[0]):
                                    for element in files:
                                        nome=os.path.join(path, element)
                                
                                        try:
                                            table.add_row(str(2)
                                            ,str(win32api.GetShortPathName(path))
                                            ,str(os.path.isdir(nome))
                                            ,str(round(os.path.getsize(nome)/(1024*1024),3))
                                        ,str(time.ctime(os.path.getctime(nome)))
                                        ,str(os.access(nome,os.R_OK)),
                                        str(os.access(nome,os.W_OK)))
                                        
                                        except Exception as e:
                                            print(str(e))
                                            continue
                                        numero+=1
                            console.print(table)
                        else:
                            console.print("[red]parma are wrong"+"[/]")

                else:
                    console.print("[red]is not a dir"+"[/]")
            
            else:

                if len(command)==1:
                   
                    if command[0]=="-l":
                        table=Table(title="file")
                        table.add_column("#", style="magenta", no_wrap=True)
                        table.add_column("name", style="red",no_wrap=True)
                        table.add_column("is_dir",no_wrap=True, style="green")
                        table.add_column("size",style="blue",no_wrap=True)
                        table.add_column("creation",style="cyan",no_wrap=True) 
                        table.add_column("read",style="yellow",no_wrap=True)
                        table.add_column("write",style="#008B8B",no_wrap=True)
                        for numero,nome in enumerate(os.listdir()):
                            try:
                                table.add_row(str(numero),nome,str(os.path.isdir(nome))
                                ,str(round(os.path.getsize(nome)/(1024*1024),3))
                                ,str(time.ctime(os.path.getctime(nome)))
                                ,str(os.access(nome,os.R_OK)),
                                str(os.access(nome,os.W_OK)))
                                
                            except:
                                continue
                        console.print(table)

                    elif command[0]=="-a":
                        table=Table(title="file")
                        table.add_column("name",style="magenta",no_wrap=True)
                        for path, subdirs, files in os.walk(os.getcwd()):
                            for element in files:
                                table.add_row(os.path.join(path, element))
                        console.print(table)

                    else:
                        console.print("[red]is not a exists dir or parma"+"[/]")
                    
                

                elif len(command)==2 and (command==["-l","-a"] or command==["-a","-l"]) :
                    table=Table(title="file")
                    table.add_column("#", style="magenta", no_wrap=True)
                    table.add_column("path", style="red",no_wrap=True)
                    table.add_column("is_dir",no_wrap=True, style="green")
                    table.add_column("size",style="blue",no_wrap=True)
                    table.add_column("creation",style="cyan",no_wrap=True) 
                    table.add_column("read",style="yellow",no_wrap=True)
                    table.add_column("write",style="#008B8B",no_wrap=True)
                    numero=0
                    for path, subdirs, files in os.walk(os.getcwd()):
                            for element in files:
                                nome=os.path.join(path, element)

                                
                                try:
                                    table.add_row(str(2)
                                    ,str(win32api.GetShortPathName(path))
                                    ,str(os.path.isdir(nome))
                                    ,str(round(os.path.getsize(nome)/(1024*1024),3))
                                ,str(time.ctime(os.path.getctime(nome)))
                                ,str(os.access(nome,os.R_OK)),
                                str(os.access(nome,os.W_OK)))
                                
                                except Exception as e:
                                    print(str(e))
                                    continue
                                numero+=1
                    console.print(table)
                else:
                    console.print("[red]parma are wrong"+"[/]")
                    

        else:
            table=Table(title="file")
            table.add_column("name",style="magenta",no_wrap=True)
            for element in os.listdir():
                table.add_row(element)
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
                print(under_string)
                save_number=number
                out_format="file"
                break
            out+=under_string+" "
        if out_format=="monitor":
            print(out)
        else:

            if len(command)<save_number+2:
                console.print("[red]error miss parma "+"[/]")
            else:
                print(command[save_number])
                print(command[save_number+1])
                try:
                    if command[save_number]==">":
                        with open(command[save_number+1],'w+') as file:
                            file.write(out)
                    else:
                        with open(command[save_number+1],'a') as file:
                            file.write("\n"+out)
                except:
                    console.print("[red]error invalid file name "+"[/]")





    
    





            

    

#TODO process info   - criptografia

                
            




