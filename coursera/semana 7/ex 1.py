# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:05:00 2020

@author: Lucino Gabriel
"""

x=int(input("digite a largura:"))
y=int(input("digite a altura:"))
t=x
while y>0:
    x=t
    while x>0:
        print("#",end='')
        x=x-1
    y=y-1
    print()