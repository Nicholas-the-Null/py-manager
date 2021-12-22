############## Correttore, Questo modulo correggera il comando e cercera di restituire quello più probabile


def Fix_letter(word1="",word2=""):
    if len(word1)>len(word2):
        passa=word2
        word2=word1
        word1=passa
    result=[]
    char_list=list(set(word1+word2))
    for char in char_list:
        if word1.count(char)==0:
            result.append(char)
        else:
            if word1.count(char)<word2.count(char):
                result.append(char)
            else:
                pass
    return result



def Correttore(commandi,parola)->list:
    """restituisce la lista dei possibili duplicati"""
    differenza_minima=4
    database_possibile=[]
    for command in commandi:
        first_step=(len(command)-len(parola) if len(command)>len(parola) else len(parola)-len(command))*2
        if first_step>=4:pass
        else:
            second_step=len(Fix_letter(command,parola))
            if second_step==len(command):
                second_step=99
            first_step+=second_step
            if first_step>=4:pass
            else:
                if first_step<differenza_minima:
                    differenza_minima=first_step
                    database_possibile=[]
                    database_possibile.append(command)
                elif first_step==differenza_minima:
                    database_possibile.append(command)
    return database_possibile











