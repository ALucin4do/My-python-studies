# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:57:47 2020

@author: Lucino Gabriel
"""

n=int(input("digite um numero inteiro"))
def éprimo(n):
    h=2
    t=2
    while h<n :
        if n%h ==0 :
            return False
        else:
            t=t+1
        h=h+1
    if t==n:
        return True
    else:
        return False
w=éprimo(n)
if w==False:
    fator = 2
    multiplicidade = 0
    while n!=1:
        while n%fator == 0:
            multiplicidade = multiplicidade+1
            n= n/fator
        if multiplicidade>0:
            print("fator",fator,"multiplicidade",multiplicidade)
        fator=fator+1
        multiplicidade=0
else:
    print("o número",n,"é um numero primo, portanto, não pode ser fatorado")
        