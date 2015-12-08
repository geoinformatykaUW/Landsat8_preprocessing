# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 10:11:36 2015

@author: student
"""

def dodawanie(x,y):
    """zwraca sume dwoch liczb"""
    suma=x+y
    return suma
         
def mnozenie(x,y):
    """zwraca iloczyn dwoch liczb"""
    iloczyn=x*y
    return iloczyn
        
if __name__=="__main__":
    print dodawanie(2,3)
    print mnozenie(2,3)