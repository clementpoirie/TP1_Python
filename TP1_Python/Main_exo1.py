#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:14:42 2020

@author: clement
"""

from fct_exo1 import ValiditeDate

####################################MAIN####################################
        
jour = int(input ("entrer le jour : "))
mois = int(input ("entrer le mois : "))
annee = int(input ("entrer l'année : "))
    
if ValiditeDate(jour, mois,annee) == True:
    print("Date valide")
else:
    print("Date non Valide")
