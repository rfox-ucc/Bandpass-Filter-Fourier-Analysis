# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GOn_qjIJGbZTZOnMF6eewCtrEgNC0UeQ
"""

import math
diff1 = math.log(1000000,10) - math.log(100,10)
diff2 = math.log(1000000,10) - math.log(1,10)
k=50
resistances = []
capacitances = []
for i in range(1,k+1):
  x = 10 ** (math.log(100,10)+((i-1)*diff1)/k)
  resistances.append(x)
for i in range(1,k+1):
  x = 10 ** (math.log(1,10)+((i-1)*diff2)/k)
  capacitances.append(x)
f = open("RCvalues.csv", "w")
for C in capacitances:
  c = C * 1e-9
  for R1 in resistances:
    for R2 in resistances:
      G = (R2/(2*R1))
      W0 = 1/(6.28*c*(R1*R2)**0.5)
      Q = 0.5*(R2/R1)**0.5
      DW = 2/(6.28*(R2*c))
      if (W0 < 150):
        continue
      if (W0 > 100000):
        continue
      if (G > 1000):
        continue
      f.write(f"{C},{R1},{R2},{G},{Q},{W0},{DW}\n")
f.close()