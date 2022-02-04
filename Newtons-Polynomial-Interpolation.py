" Title: Newton's Polynomial Interpolation
" Author: Gustavo O Ramirez <ogustavoramirezo@gmail.com>
" License: MIT
" Source: https://github.com/GustavoOctavio/Numerical-Analysis-with-Phyton
" Description: The Newton's polynomial interpolation use the interpolation with
" a set of data points.  
" Last Change: 4-02-2022 

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x = sp.Symbol('x')
n=int(input("Ingrese el valor de n:"))
xi=np.zeros(n)
i=0
p=0
ps=0
while i<n:
    xi[i]=float(input("Ingrese el valor de x_i:"))
    i=i+1
f=np.zeros((n,n))
i=0
while i<n:
    f[i][0]=float(input("Ingrese el valor de f_i:"))
    i=i+1
i=0
j=0
while j<n-1:
    while i<n-j-1:
        f[i][j+1]=(f[i+1][j]-f[i][j])/(xi[i+j+1]-xi[i])
        print(f[i][j+1])
        i=i+1
    j=j+1
    i=0
print(f)
p=f[0][0]
i=0
j=0
l=1
while i<n-1:
    while j<i+1:
        l=l*(x-xi[j])
        j=j+1
    p=p+f[0][i+1]*l
    i=i+1
    l=1
    j=0
ps=p.expand()
print(ps)


