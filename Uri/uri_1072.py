# -*- coding: utf-8 -*-
"""Uri_1072.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HVuUV0P4lfD2K12nDpHlus7ibCikFqWG
"""

n=int(input())
dentro=0
fora=0
for i in range(n):
  x=int(input())
  if 10<=x<=20:
    dentro+=1
  if x<10 or x>20:
    fora+=1
print("{} in".format(dentro))
print("{} out".format(fora))