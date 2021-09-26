# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 00:29:27 2021

@author: Asus
"""

W= input("Input a string: ")
d=dict()
def most_frequent(string):
    for key in string:
        if key not in d:
            d[key]=1
        elif key in d:
            d[key]=d[key]+1
    return d
print(most_frequent(W))