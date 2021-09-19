# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:08:19 2021

@author: Asus
"""

A=input('enter the string ')
def most_frequent(string):
    d=dict()
    for key in d:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d 
s= most_frequent(A)
print(s)
