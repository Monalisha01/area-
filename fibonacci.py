# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:09:53 2021

@author: Asus
"""

# Fibonacci numbers
 
n= int(input("Enter the number of terms: "))
n1=0
n2=1
count=0
print("The fibonacci numbers are: ")
while count<n:
    print (n1,end=",")
    nth= n1+n2
    n1=n2
    n2=nth
    count +=1