#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:30:41 2021

@author: ahmed 
Automate cellulaire
"""

def grille(n):
    M = []
    for i in range(n):
        L =[]
        for j in range(n):
            L.append(0)
        M.append(L)
    return M

