#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 00:19:33 2021

@author: ahmed
"""
## Q1.
def Liste_suite(u0,r,n):
    U = [0]*(n+1)
    U[0] = u0
    for i in range(0, n):
        U[i+1]= r*U[i]*(1-U[i])
       
    return U
## Q2.
h = 4/100
R = []
for i in range(100):
    R.append(i*h)
## Q3.
u0 = 0.5
import matplotlib.pyplot as plt
for n in range(100, 201):
    for r in R:
        plt.plot(r, Liste_suite(u0,r,n)[-1], 'bo', ms =2)
        
plt.title("Diagramme de bifurcation")
plt.xlabel("r")
plt.ylabel(r"$U_n$")
plt.tight_layout()
plt.savefig("bifurcation.pdf")
plt.show()
        
    