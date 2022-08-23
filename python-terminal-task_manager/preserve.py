class File():
    def __init__(self,nome,content,path,type):
        self.nome = nome
        self.content = content
        self.path = path
        self.type = type
        

    def refactor(self):
        """check if self.content is binary or text
        if binary, use wb to write
        if text, use w to write
        if self.content is empty do nothing"""
        if self.checkIfIsEmpty():
            return
        if self.type == 'text':
            with open(r''+self.path+"\\"+self.nome,"w+",encoding="utf-8") as f:
                f.write(self.content)
        else:
            with open(r''+self.path+"\\"+self.nome,"wb") as f:
                f.write(self.content)

        f.close()

    def toString(self):
        return self.nome+" "+self.path

    def checkIfIsEmpty(self):
        if self.content == "":
            return True
        else:
            return False

    