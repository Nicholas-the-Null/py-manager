class File():
    def __init__(self,nome,content,path):
        self.nome = nome
        self.content = content
        self.path = path

    def refactor(self):
        textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
        is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

        if is_binary_string(self.content):
            with open(r''+self.path+"\\"+self.nome,"wb") as f:
                f.write(self.content)
        else:
            with open(r''+self.path+"\\"+self.nome,'w+',encoding="utf-8") as f:
                for x in self.content:
                    f.write(x)
        f.close()

    def toString(self):
        return self.nome+" "+self.path

    