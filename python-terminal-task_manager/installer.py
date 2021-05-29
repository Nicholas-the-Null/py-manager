import sys
import os
import platform


if  platform.uname().system!='Windows':
    input("you are not using win")
    exit()

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
        from tqdm import tqdm
    except ImportError:
        os.system("pip install tqdm")

    try:
        import requests
    except ImportError:
        os.system("pip install requests")
    try:
        import qrcode
    except ImportError:
        os.system("pip install qrcode")
    try:
        import pyAesCrypt 
    except ImportError:
        input("pip install pyAesCrypt ")
        exit()
    
    print("i've seen enough i'm satisfied")
    input("success")

    try:
        from tqdm import tqdm
    except ImportError:
        os.system("pip install tqdm")
    try:
        import qrcode
    except ImportError:
        os.system("pip install qrcode")
        
<<<<<<< HEAD
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

=======
        try:
            from tqdm import tqdm
        except ImportError:
            os.system("pip install tqdm")
        try:
            import qrcode
        except ImportError:
            os.system("pip install qrcode")
            
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
>>>>>>> f17394e4974b37f4d46aa80e9d4aa48b8c006dc6
