import os
try:
    from cryptography.fernet import Fernet
except:
    raise "miss [pip install cryptography]"

import string
import random

    
       
def encrypt(filename):
    f = Fernet.generate_key()
    f = Fernet(f)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    del f


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
    encrypt(file)

