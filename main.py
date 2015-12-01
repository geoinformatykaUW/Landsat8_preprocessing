# -*- coding: utf-8 -*-
import os
import sys
#Edwin
#---------------------------------------------
#Dodanie foldera lib do sciezki python
#Umozliwia importowanie modulow z tego foldera
sys.path.append(os.getcwd()+"/lib")
#---------------------------------------------


import test_lib


if __name__ == "__main__":
    print test_lib.dodaj(3,2)
    print test_lib.znajdz_literke("Geografia","a")