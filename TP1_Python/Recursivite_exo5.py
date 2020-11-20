#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:55:10 2020

@author: clement
"""

def ToursHanoi(NmbrPalet, tour1, tour2, tour3,compteur):
    compteur = compteur+1
    print(compteur)
    if NmbrPalet > 0:
        ToursHanoi(NmbrPalet-1,tour1, tour3, tour2,compteur)
        print("déplacer le disque du plot",tour1 , "vers le plot ", tour3)
        ToursHanoi(NmbrPalet-1,tour2, tour1, tour3,compteur)
       
    

    
    
ToursHanoi(5,1,2,3,0)    
        
    
    
    