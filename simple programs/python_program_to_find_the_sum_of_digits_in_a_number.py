# -*- coding: utf-8 -*-
"""Python Program to Find the Sum of Digits in a Number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OLJVBRHwkAEwFpKExwReMSy3u6AfA0FQ
"""

#Python Program to Find the Sum of Digits in a Number

n= int(input("enter the numer"))
x =0
while(n>0):
  
    x=x +n%10
    n = n//10
print(x)

