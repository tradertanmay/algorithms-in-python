# -*- coding: utf-8 -*-
"""Python Program to Accept Three Digits and Print all Possible Combinations from the Digits5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15LKlWn9tquYkCyZ-5Nnvy5t4jdAg5E6q
"""

#Python Program to Accept Three Digits and Print all Possible Combinations from the Digits

a=[int(input("enter 3 digits")) for i in range (3)]
[(a[i], a[j],a[k])for i in range(3) for j in range(3)for k in range(3) 
 if( i!=j and j!=k and k!=i)]
