class File():
    def __init__(self,nome,content,path):
        self.nome = nome
        self.content = content
        self.path = path

    def refactor(self):
        with open(r''+self.path+"\\"+self.nome,'w+',encoding="utf-8") as f:
            for x in self.content:
                f.write(x)
        f.close()

    def toString(self):
        return self.nome+" "+self.path

    