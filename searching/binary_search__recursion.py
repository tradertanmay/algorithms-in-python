# -*- coding: utf-8 -*-
"""Binary_Search_ Recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hazpHlMmxlxT2lMmGHUNnp35bP8r2ryu
"""

def _binary_search_rec(a, x, lo, hi):
    if lo > hi:
        return None
    mid = lo + (hi-lo) // 2
    if x < a[mid]:
        return _binary_search_rec(a, x, lo, mid-1) # function call
    elif x > a[mid]:
        return _binary_search_rec(a, x, mid+1, hi)  # function call
    else:
        return mid  # base case

a = [0,1,2,3,4,5,6,7,8,9,10]
print(_binary_search_rec(a,11,0,len(a)-1))

