# -*- coding: utf-8 -*-
"""Recursion-isArraylnSortedOrder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JkK312lOOepthGFcWo21tWv-_Vtf1Goz
"""

def isArraylnSortedOrder(A):
#Base case
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isArraylnSortedOrder(A[ 1:])
A= [1, 2, 6, 7, 9331]
print(isArraylnSortedOrder(A))

