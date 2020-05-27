# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:29:23 2019

@author: Lucino Gabriel
"""

x=int(input("Digite um número inteiro: "))
a=0
b = False

while (not b):
    a = a+(x%10)
        
    if (x//10)==0:
        b = True
    else: 
        x=x//10
            
   
print(int(a))            