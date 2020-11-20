#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:55:15 2020

@author: clement
"""

revenu=eval(input("combien avez vous gagné cette année ? "))

def mesImpots(revenu):
     impots=0
     if revenu < 9964 :
         impots=0
     elif revenu > 9964 and revenu < 27519:
         impots=(revenu-9964)(14/100)
     elif revenu < 73779 and revenu > 27519:
         impots=((revenu-27519)(30/100))+((27519-9964)(14/100))
     elif revenu < 156244 and revenu > 73779:
         impots=((revenu-73779)(41/100))+((73779-27519)(30/100))+((27519-9964)(14/100))
     else :
         impots=((revenu-156244)(45/100))+((156244-73779)(41/100))+((73779-27519)(30/100))+((27519-9964)(14/100))
     print(impots)

mesImpots(revenu)
