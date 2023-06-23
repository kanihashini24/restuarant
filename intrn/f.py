# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:54:13 2023

@author: DS
"""

from cal import summation    ,multiplication
#it will import only the summation() from calculation.py  
a = int(input("Enter the first number"))  
b = int(input("Enter the second number"))  
print("Sum = ",summation(a,b))
print("multiply = ",multiplication(a,b))
