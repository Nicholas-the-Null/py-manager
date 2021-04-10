import sys
import os
import platform


if  platform.uname().system!='Windows':
    input("you are not using win")
    exit()

else:
    code=input("insert code or tab any key for continue ")

    if code=="1789":
        pass #Download lib package

    else:
        print("Welcome to the installation procedure :)")
    
            

        try:
            from cryptography.fernet import Fernet
        except:
            os.system("pip install cryptography")

        try:
            from rich.console import Console 
        except ImportError:
            os.system("pip install rich")

        try:
            import win32api
        except ImportError:
            os.system("pip install pywin32")
        
        try:
            from tqdm import tqdm
        except ImportError:
            os.system("pip install tqdm")

        try:
            import requests
        except ImportError:
            os.system("pip install requests")
        try:
            import pyAesCrypt 
        except ImportError:
            input("pip install pyAesCrypt ")
            exit()
        
        print("i've seen enough i'm satisfied")
        input("success")