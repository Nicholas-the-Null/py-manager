


def ListaDeleteLista2(lista,Lista2):
    """Return in a list the different letter!"""
    contatore=0
    ricontatore=len(Lista2)
    while contatore!=ricontatore:
        if Lista2[contatore] in lista:
            eliminare=0
            while eliminare!=len(lista):
                if lista[eliminare]==Lista2[contatore]:
                    lista.pop(eliminare)
                    eliminare-=1
                eliminare+=1
        contatore+=1
    return lista



def Correttore(database,precisione=1,wordo=""):
    ida=0
    check=wordo
    list_possible1=[]
    list_possible_final=[]
    
    
    num_lines = len(database)
    
    while num_lines>ida:
        file = database[ida]  # First Line
        if file is None:
            pass
        check_distanza=len(file)-len(check)
        if check_distanza<0:check_distanza*-1
        if check_distanza>precisione:
            pass
        
        else:
            parola=file
            if parola == check:
                break
            
            file=list(file.lower())
            l=ListaDeleteLista2(file,wordo)
           
            
            if len(l)<=precisione:
                 list_possible1.append(parola)
        ida+=1

    
    for x in list_possible1:
        if len(x)==len(wordo):
            list_possible_final.append(x)
    
    
    if len(list_possible_final)==0:
        list_possible_final=list_possible1
    
    list_possible1=[]
    massimo=0
    for x in list_possible_final:
        attuale=0
        try:
            for posizione,parola in enumerate(x):
                if wordo[posizione]==parola:
                    attuale+=1
            if attuale>massimo:
                list_possible1=[x]
                massimo=attuale
            elif attuale==massimo:
                list_possible1.append(x)
        except:
            pass

    
    list_possible_final=list_possible1

    return list_possible_final












########## confrontare la lunghezza e la presenza di lettere