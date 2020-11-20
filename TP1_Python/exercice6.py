#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:56:27 2020

@author: clement
"""

nombre=eval(input("nombre entier naturel : "))

def syracuse(nombre):
    Lsyr=[nombre]
    while Lsyr[-1] != 1:
        if Lsyr[-1] % 2 == 0:
            Lsyr.append(Lsyr[-1]//2)
        else:
            Lsyr.append(Lsyr[-1]*3+1)

    return Lsyr

print(syracuse(nombre))

Lsyr=syracuse(nombre)

def maxsyr(Lsyr):
    maxi = Lsyr[0]
    for i in Lsyr:
        if i >= maxi:
            maxi = i
    return maxi

print(maxsyr(Lsyr))

def temps_vol(nombre):
     return len(syracuse(nombre))-1

print(temps_vol(nombre)) 

def dernierIndiceMaximum(liste):
    maxi = liste[0]
    longueur=len(liste)
    indice_max = 0
    for i in range(longueur):
        if liste[i] >= maxi:
            maxi = liste[i]
            indice_max = i
    return indice_max

def vol_max_syr():
    L=[]
    for i in range(1,1000):
        T=temps_vol(i)
        L.append(T)
        i=i+1
    res=dernierIndiceMaximum(L)+1
    return "temps de vol max atteind par",res

print(vol_max_syr())

def alt_max_syr():
    L=[]
    for i in range(1,1000):
        x=syracuse(i)
        alt=maxsyr(x)
        L.append(alt)
        i=i+1
    res=dernierIndiceMaximum(L)+1
    return "alt max atteind par",res

print(alt_max_syr())