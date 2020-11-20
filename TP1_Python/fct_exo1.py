# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#2/calendrier

def bissextile (annee) :
    if annee % 400 ==0:
        return(True)
    else:
        return(False)

def NombreJourMois (numeroMois, annee) :
    Liste_31j =[1,3,5,7,8,10,10]
    Liste_30j = [4,6,9,11]
    nombreJour =0
    if numeroMois == 2:
        if bissextile(annee) == True:
            nombreJour=28
        else:
            nombreJour=29      
    for i in Liste_31j:
        if i == numeroMois:
            nombreJour=31
    for j in Liste_30j:
        if j == numeroMois:
            nombreJour=30
    return(nombreJour)
            
    
def ValiditeDate (jour, Numeromois, annee):
    BonJour=NombreJourMois(Numeromois,annee)
    if Numeromois > 12:
        return(False)
    if BonJour >= jour:
        return(True)
    if BonJour < jour:
        return(False)
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    