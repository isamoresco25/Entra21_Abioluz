# -*- coding: utf-8 -*-
"""Uri_1036.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xdGOyqJlqieRjCr39f_lqvoZvXPc3yHn
"""

A,B,C=input().split()
A=float(A)
B=float(B)
C=float(C)
delta=B**2-4*A*C
if A==0.0 or delta<0:
    print("Impossivel calcular")
else:
    x1=(-B+delta**(1/2))/(2*A)
    x2=(-B-delta**(1/2))/(2*A)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))