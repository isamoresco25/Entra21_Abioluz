# -*- coding: utf-8 -*-
"""Uri_1018.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xdGOyqJlqieRjCr39f_lqvoZvXPc3yHn
"""

n=int(input())
print(n)
n100=n//100
n=n-n100*100
n50=n// 50
n=n-n50*50
n20=n// 20
n=n-n20*20
n10=n// 10
n=n-n10*10
n5=n// 5
n=n-n5*5
n2=n//2
n=n-n2*2
n1=n// 1
n=n-n1*1
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))
))