# -*- coding: utf-8 -*-
"""#to Find if a Number is Prime or Not Prime Using Recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FX8xBDmngpZwduBiWo4_2KbRAtxlMb6K
"""

#to Find if a Number is Prime or Not Prime Using Recursion

def prime_check_recursion(n,i=2):
    #base case
    if n<=2:     # check1
      if n==2:
         return True
      else:
         return False
    elif n%i==0: # check 2
      return False
    elif i*i >n: # check 3
        return True
    else:
      return(prime_check_recursion,i+1)
# program to check prime
n = int(input("enter the number"))
if prime_check_recursion(n):
  print("prime")
else:
  print("not prime")

