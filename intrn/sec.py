# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 12:04:52 2023

@author: DS
"""

from mithun import summation,multiplication  
#it will import only the summation() from calculation.py  
a = int(input("Enter the first number"))  
b = int(input("Enter the second number"))  
print("Sum = ",summation(a,b))

print("mulply = ",multiplication(a,b))