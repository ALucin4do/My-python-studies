# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:01:08 2019

@author: Lucino Gabriel
"""

def éprimo(w):
    h=2
    t=2
    while h<w :
        if w%h ==0 :
            return False
        else:
            t=t+1
        h=h+1
    if t==w:
        return True
    else:
        return False
def maior_primo(k):
    if k<=2:
        return 2
    else :
        i=n=3
       
        while i<=k:                
            if  éprimo(i) == True :
                n=i
                i=i+1
            else:
                i=i+1
                
    return n
                    