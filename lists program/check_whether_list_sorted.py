# -*- coding: utf-8 -*-
"""check_whether_list_sorted

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SQ51AS0VjPQSYZtw3-mzjwY-a51Nrl_c
"""

def check_sorted_list(a):
    for i in range(len(a)-1):  
        if a[i+1] <a[i]:
            print("not sorted")
            break

    else:
        print("sorted")

a =[13,14,21,35]

check_sorted_list(a)

