# -*- coding: utf-8 -*-
"""to Find the Factorial of a Number Using Recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-nx5F5IjKAXZd1bEgHyaVCAcCFWYhvrq
"""

#to Find the Factorial of a Number Using Recursion

n=int(input("enter the factorial you want"))

def factorial(n):
  if n ==1: # base case
    return(1)
  else:
    return(n*factorial(n-1))
  
factorial(n)

