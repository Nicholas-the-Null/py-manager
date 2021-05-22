import os
try:
    from cryptography.fernet import Fernet
except:
    raise "miss [pip install cryptography]"

import string
import random



def generate_key():
    """Generate key!"""
    f = Fernet.generate_key()
    return f


def create_key(key):
    f = Fernet(key)
    return f


def encrypt(key,filename):
    f=key
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    del f




def load_key(nome="key"):
    try:
        x=open(nome+".key", "rb").read()
        return x
    except Exception as e:
        print(str(e))


def decrypt(key,filename=None):
    
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def secure_delete(path):
    with open(path, "w") as delfile:
        letters = string.ascii_lowercase
        x= ''.join(random.choice(letters) for i in range(200))
        delfile.write(x)
    with open(path, "ba+") as delfile:
        length = delfile.tell()
        for i in range(30000):
            delfile.seek(0)
            delfile.write(os.urandom(length))



def Delete_File(file):
    secure_delete(file)
    key=generate_key()
    key=create_key(key)
    encrypt(key,file)

