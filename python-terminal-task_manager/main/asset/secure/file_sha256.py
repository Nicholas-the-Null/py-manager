import hashlib

def File_calcolatore_sha256(filename) -> str:
    sha256 = hashlib.sha256()
    with open(filename, "rb") as thefile:
        buf = thefile.read()
        sha256.update(buf)
    return str(sha256.hexdigest())

def String_calcolatore_sha256(string) -> str:
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

