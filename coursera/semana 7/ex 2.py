# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:08:49 2020

@author: Lucino Gabriel
"""
x=int(input("digite a largura:"))
y=int(input("digite a altura:"))
w=y
t=x
while y>0:
    x=t
    while x>0:
        if y==w or y==1:
            print("#",end='')
        else:
           if x==t or x==1:
              print("#",end='')
           else:  
              print(" ",end='')
        x=x-1
    y=y-1
    print()