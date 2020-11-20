#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:20:07 2020

@author: clement
"""

def multiplication (B,C):
    A=[[],[],[]]
    for i in [0,1,2]:
        L1 = B[0][i]*C[i][0]
        L2 = B[1][i]*C[i][1]
        L3 = B[2][i]*C[i][2]
        
        A[0].append(L1) 
        A[1].append(L2) 
        A[2].append(L3) 
    return (A)




#####################################MAIN####################################
    
B=[[1,2,3],[4,5,6],[7,8,9]]
C=[[1,2,3],[4,5,6],[7,8,9]]
print("A =" , multiplication(B,C))
