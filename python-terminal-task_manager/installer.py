import os
import platform
try:
    import requests  #######installare prima
except:
    pass
from getpass import getuser
try:
    from tqdm import tqdm #installare prima
except ImportError:
    pass


path_original=r''+os.getcwd()+"\\main"
def download_file(link):
    if requests.get(link).status_code==200:
        buffer_size = 1024
        response = requests.get(link, stream=True)
        file_size = int(response.headers.get("Content-Length", 0))
        filename = link.split("/")[-1]
        progress_bar(response,buffer_size,file_size,filename)
        return "Success"
    else:
        print("error")
        return "[red]site not found "+"[/red]"

def progress_bar(response,buffer_size,file_size,filename):
    progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            f.write(data)
            progress.update(len(data))



x=input("press a key:")
if x=="1789":
    if os.path.exists(path_original) is False:
        os.mkdir(path_original)
        os.chdir(path_original)
        with open("__init__.py","w+") as create:
            create.close()
        os.mkdir("asset")
        path_original=r''+os.getcwd()+"\\asset"
        os.chdir(path_original)
    else:
        path_original=r''+os.getcwd()+"\\main\\asset"
        os.chdir(path_original)
    with open("__init__.py","w+") as create:
            create.close()
    try:
        import main.asset.secure.file_sha256
    except ImportError:
        path=r''+path_original+"\\secure"
        if os.path.exists(path) is False:
            os.mkdir(path)
            os.chdir(path)
            with open("__init__.py","w+") as create:
                create.close()
        else:
            os.chdir(path)
        download_file("https://nicholas-the-null.github.io/py_manager_website/file_sha256.py")
        os.chdir(path_original)
    try:
        import main.asset.secure.cripta
    except:
        path=r''+path_original+"\\secure"
        if os.path.exists(path) is False:
            os.mkdir(path)
            os.chdir(path)
            with open("__init__.py","w+") as create:
                create.close()
        else:
            os.chdir(path)
        download_file("https://nicholas-the-null.github.io/py_manager_website/cripta.py")
        os.chdir(path_original)
    try:
        import main.asset.Down.DonwloadLib
    except:
        path=r''+path_original+"\\Down"
        if os.path.exists(path) is False:
            os.mkdir(path)
            os.chdir(path)
            with open("__init__.py","w+") as create:
                create.close()
        else:
            os.chdir(path)
        download_file("https://nicholas-the-null.github.io/py_manager_website/DonwloadLib.py")
        os.chdir(path_original)
    try:
        import main.asset.multi_delete
    except:
        download_file("https://nicholas-the-null.github.io/py_manager_website/multi_delete.py")
    try:
        import main.asset.correttore as Correttore
    except:
        download_file("https://nicholas-the-null.github.io/py_manager_website/correttore.py")
    try:
        import main.asset.wifi
    except:
        download_file("https://nicholas-the-null.github.io/py_manager_website/wifi.py")
    exit()
        
        
        
        
        
        
    



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
        import youtube_dl
    except ImportError:
        os.system("pip install youtube_dl")
    
    try:
        import pyperclip
    except ImportError:
        os.system("pip install pyperclip")

    
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
        os.system("pip install pyAesCrypt ")
        

    try:
        import bs4
    except ImportError:
        os.system("pip install BeautifulSoup4")

    try:
        import psutil
    except ImportError:
        os.system("pip install psutil")

    os.system("pip install prompt_toolkit")
        
    
    print("i've seen enough i'm satisfied")
    input("success")

