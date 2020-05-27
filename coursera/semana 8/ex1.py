# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:14:45 2020

@author: Lucino Gabriel
"""

def remove_repetidos(l):
    for x in l:
        i=0
        p=0
        while i<len(l):
            k=l[i]
            if x==k:
                p=p+1
            if x==k and p>1:
                del l[i]
            i=i+1
    l=sorted(l)
    return l

remove_repetidos([1,2,2,2,3,3,4])
