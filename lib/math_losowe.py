# -*- coding: utf-8 -*-
"""
# 12.06.2015
# Technomag
# Zadanie na lekcji
"""

import random

def RandomSum(dlugosc_sekwencji):
    """Zwraca sumę z sekwencji dowolnej długości. Elementy
       sekwencji są losowane <0-1)
    """
    sekwencja = []
    for i in range(dlugosc_sekwencji):
        sekwencja.append(random.random())
    return sum(sekwencja)

def RandomSumRange(dlugosc_sekwencji,koncowa_wartosc):
    """Zwraca sumę z sekwencji dowolnej długości. Elementy
       sekwencji są integerami losowanymi z zakresu
       0 - koncowa_wartosc    
    """
    sekwencja =[]
    for i in range(dlugosc_sekwencji):
        sekwencja.append(random.randint(0,koncowa_wartosc))
    return sum(sekwencja)
    
if __name__ == "__main__":
    print RandomSum(10)
    print RandomSumRange(10,10)
