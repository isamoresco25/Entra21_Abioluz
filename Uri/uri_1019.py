# -*- coding: utf-8 -*-
"""Uri_1019.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xdGOyqJlqieRjCr39f_lqvoZvXPc3yHn
"""

N=int(input())
h=N//3600
m=(N-(h*3600))//60
s=N-(h*3600)-(m*60)
print("{}:{}:{}".format(h,m,s))