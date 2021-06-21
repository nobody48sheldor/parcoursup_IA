import numpy as np
import matplotlib.pyplot as plt
from math import *
import data as dt

data = dt.main()

print(data)
print(len(data))


#entrer les infos importantes

#av_prem = float(input("moyenne de l'annee de 1ere = "))
#av_term1 = float(input("moyenne du 1er trimestre de terminal = "))
#av_term2 = float(input("moyenne du 2eme trimestre de terminal = "))
#av_mp_prem = float(input("moyenne des spé (maths/physique) de premiere = "))
#av_mp_term1 = float(input("moyenne des spé (maths/physique) de terminal (1er trimestre) = "))
#av_mp_term2 = float(input("moyenne des spé (maths/physique) de terminal (2eme trimestre) = "))

def score(dict):
    return(1)

def score_eleve():
    return(1)

score_eleve = score_eleve()

score_ecole = []

for i in range(len(data)):
    dictionary_score = {}
    dictionary_score[data[i]['Ã‰tablissement']] = score(data[i]['Ã‰tablissement'])
    score_ecole.append(dictionary_score)

print(score_ecole)

def ecole_possible():
    S = []
    for i in range(len(score_ecole)):
        for cle, value in score_ecole[i].items():
            if int(value) <= score_eleve:
                S.append(cle)
    return(S)

print(ecole_possible())
