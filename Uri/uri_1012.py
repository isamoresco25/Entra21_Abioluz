# -*- coding: utf-8 -*-
"""Uri_1012.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xdGOyqJlqieRjCr39f_lqvoZvXPc3yHn
"""

A, B, C = input().split(" ")
A=float(A)
B=float(B)
C=float(C)
triangulo=(A*C)/2
circulo=3.14159*C**2
trapezio=((A+B)*C)/2
quadrado=B**2
retangulo=A*B
print("""TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}""" .format(triangulo, circulo, trapezio, quadrado, retangulo))