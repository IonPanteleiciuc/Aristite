import numpy as np
import re
import random as rd

def somme_1(dico: dict):
    res = True
    for k in range(1, 6):
        #print(f"Colonne {k}")
        somme = 0

        for i in dico.keys():
            if re.findall(f"^h{k}.", str(i)):
                somme += dico[str(i)]
        if somme != 38: 
            res = False

        #print(somme, res,"\n")
    return res


def somme_2(dico: dict):
    res = False
    s1 = dico["h11"] + dico["h21"] + dico["h31"]
    s2 = dico["h12"] + dico["h22"] + dico["h32"] + dico["h41"]
    s3 = dico["h13"] + dico["h23"] + dico["h33"] + dico["h42"] + dico["h51"]
    s4 = dico["h24"] + dico["h34"] + dico["h32"] + dico["h41"]
    s5 = dico["h35"] + dico["h44"] + dico["h53"]

    print(s1, s2, s3, s4, s5)
    if s1 == s2 == s3 == s4 == s5 == 38:
        res = True
    return res


def somme_3(dico: dict):

    res = False
    s1 = dico["h31"] + dico["h41"] + dico["h51"]
    s2 = dico["h21"] + dico["h32"] + dico["h42"] + dico["h52"]
    s3 = dico["h11"] + dico["h22"] + dico["h33"] + dico["h44"] + dico["h53"]
    s4 = dico["h12"] + dico["h23"] + dico["h34"] + dico["h44"]
    s5 = dico["h13"] + dico["h24"] + dico["h35"]

    print(s1, s2, s3, s4, s5)
    if s1 == s2 == s3 == s4 == s5 == 38:
        res = True  
    return res
    

def remplir1(dico:dict):
    liste = [i for i in range(1, 20)]
    rd.shuffle(liste)
    print("Liste : ", liste)

    for x in dico.keys():
        dico[str(x)] = liste.pop()

    return dico

def remplir2():
    return 0