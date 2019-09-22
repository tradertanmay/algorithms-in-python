# -*- coding: utf-8 -*-
"""Linear Search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CH2UvPudknG5azGrhrBYVbTSjbluLyEc
"""

#1. Create a function linear_search that takes a list and key as arguemnts.
#2. A loop iterates through the list and when an item matching the key is found, the corresponding index is returned.
#3. If no such item is found, -1 is returned.

alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))

def linear_search(alist, key):
    z = [i for i in range(len(alist)) if alist[i] == key ]
    if key not in alist:
        print('{} was not found.'.format(key))
    else:
        print('{} was found at index {}.'.format(key, z[0]))
linear_search(alist,key)


