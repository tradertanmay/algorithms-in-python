# -*- coding: utf-8 -*-
"""creating sublist in a list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jn-pOZIP7oPz_Px4zPkpD7t1fmMvOlAO
"""

# creating sublist in a list
x =int(input("enter the number of sublist you want to create"))
y =int(input("no of items in a sublist"))
[[int(input("enter the elem")) for i in range(y)] for j in range(x)]

