# -*- coding: utf-8 -*-
"""Python Program to Reverse a Given Number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L7viPpWzmYUHzEApu3LXjQVyFnC_Wodd
"""

#Python Program to Reverse a Given Number
# number = 123
# reverse number = 321

# divide by 10 and take the remainder - we can use n%10 
# remainder = n%10
#and store it in the first -- we can use reverse =  reverse*10+remainder
#remove from the original- for that we can use n//10

def rev():
  n=int(input("enter the number"))
  reverse = 0
  while n >0 :
    remainder = n%10
    reverse = reverse*10 +remainder
    n =n//10
  return(reverse)

rev()

