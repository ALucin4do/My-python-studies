# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:47:15 2019

@author: Lucino Gabriel
"""

x=int(input("Digite o valor de n: "))
i=x
while x>1:
    
    i=i*(x-1)
    x=x-1
if x!=0:
    print(i)
else:
   print(1)