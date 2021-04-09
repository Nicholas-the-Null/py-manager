from rich.console import Console 
import os
from rich.table import Table
from rich.prompt import Confirm
from datetime import datetime
import platform
import asset.file_sha256
import sys

console = Console()
history=[]


table = Table(title="info")
table.add_column("time",style="magenta")
table.add_column("os",style="green",no_wrap=True)
table.add_column("version",style="purple",no_wrap=True)
table.add_column("sha256",style="#A52A2A",no_wrap=True)
table.add_column("update",style="cyan",no_wrap=True)

table.add_row(str(datetime.now()),str(platform.uname().system),"1.0",
asset.file_sha256.File_calcolatore_sha256(sys.argv[0]),"False")

console.print(table)





    






while True:
    command=console.input("[green]"+str(os.getcwd())+"[/]>").split()
    history.append(" ".join(command))
    if command[0].lower() in ["hs","hy","history"]:
        table = Table(title="history")
        table.add_column("numero",style="magenta")
        table.add_column("command",style="green",no_wrap=True)
        for numero,nome in enumerate(history):
            table.add_row(str(numero),str(nome))
        console.print(table)
    elif command[0].lower() in ["cd","changedirectory","chd"]:
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
    elif command[0].lower() in ["md","mkd","mkdir"]:
        command.pop(0)
        if len(command)==0:
            console.print("[red]error no name in input"+"[/]")
        else:
            if os.path.exist(command[0]):
                console.print("[red]error directory already exists"+"[/]")
            else:
                os.mkdir(command[0])
    elif command[0].lower() in ["getsha","sha256","gtsh","get256"]:
        command.pop(0)
        if os.path.exists(command[0]):
            input_type= "File" 
            result=asset.file_sha256.File_calcolatore_sha256(command[0])
        else:
            input_type="string" 
            result=asset.file_sha256.String_calcolatore_sha256(command[0])
        
        table=Table(title="info")
        table.add_column("useriput",no_wrap=True,style="blue")
        table.add_column("type",style="magenta")
        table.add_column("sha256",no_wrap=True,style="green")
        table.add_row(command[0],input_type,result)
        console.print(table)

    elif command[0].lower() in ["clear","cls"]:
        os.system("cls")

    elif command[0].lower() in ["more","mr"]:
        command.pop(0)
        if not len(command)==0:
            if os.path.exists(command[0]):
                if os.access(command,os.R_OK):
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

                else:
                    console.print("[red]error file not found"+"[/]")
            else:
                console.print("[red]i cant read file"+"[/]")

        else:
            console.print("[red]error no file in input"+"[/]")


                
            



#? taskkill /F /IM explorer.exe & start explorer command restarta explora
