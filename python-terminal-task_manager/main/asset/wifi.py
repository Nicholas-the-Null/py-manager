import sys
import subprocess
import re
import os
import qrcode
import ctypes
import locale
import colorama

__version__ = "1.1.1"

###############################################################
#     https://github.com/sdushantha/wifi-password             #                     
#           original code                                     #
###############################################################


########################## edit here ###################

######################### translate ################

auth_var="Autenticazione"      #<------------------
passowrd_lang="Contenuto"      ##<------------------
defaul_lang="it"               #<------------------

def lang():
    return defaul_lang


########################## edit here ###################




def detect_system_lang():
    windll = ctypes.windll.kernel32
    return locale.windows_locale[ windll.GetUserDefaultUILanguage() ]



    
        

def run_command(command: str) -> str:
    """
    Runs a given command using subprocess module
    """
    env = os.environ.copy()
    env["LANG"] = "C"
    output, _ = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True, env=env).communicate()
    return output.decode("utf-8").rstrip("\r\n")


def print_error(text) -> None:
    """
    Shows an error message and exits the program with the status code 1
    """
    print(f"ERROR: {text}", file=sys.stderr)
    sys.exit(1)


def get_ssid() -> str:
    """
    Get the SSID which the computer is currently connected to
    """

    ssid = run_command("netsh wlan show interfaces | findstr SSID")
    if ssid == "":
        print_error("SSID was not found")

    ssid = re.findall(r"[^B]SSID\s+:\s(.*)", ssid)[0]

    return ssid


def get_auth() -> str:
    auth=run_command("netsh wlan show interfaces | findstr " + auth_var) 
    auth=re.findall(r"[^B]"+auth_var+"\s+:\s(.*)", auth)[0] #change
    return auth



def get_password(ssid: str) -> str:
    """
    Gets the password for a given SSID
    """

    if ssid != "":
        
        password = run_command(f"netsh wlan show profile name=\"{ssid}\" key=clear | findstr " + passowrd_lang)
        
        password = re.findall(r''+passowrd_lang+" chiave\s+:\s(.*)", password)[0] #change

    if password == "":
        print_error("Could not find password")

    return password





def generate_qr_code(ssid: str, password: str, auth:str, path: str, show_qr: bool) -> None:
    """
    Generate a QR code based on the given SSID and password
    """

    # Source: https://git.io/JtLIv
    text = f"WIFI:T:{auth};S:{ssid};P:{password};;"

    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)
    qr.add_data(text)

    if show_qr:
        # This will emulate support for ANSI escape sequences, which is needed
        # in order to display the QR code on Windows
        colorama.init()
        qr.make()
        qr.print_tty()

    if path:
        file_name = ssid.replace(" ", "_") + ".png"

        if path == "STORE_LOCALLY":
            path = file_name

        try:
            img = qr.make_image()
            img.save(path)
        except FileNotFoundError:
            print_error(f"No such file/directory: '{path}'")

        print(f"QR code has been saved to {path}")



#generate_qr_code(get_ssid(),get_password(get_ssid()),"WPA2-EAP","ciao.png",True)









#python-terminal-task_manager\main\asset\Setup
