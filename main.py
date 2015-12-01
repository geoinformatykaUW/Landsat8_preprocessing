# -*- coding: utf-8 -*-
#import test_lib
import os
import sys
#---------------------------------------------
#Dodanie foldera lib do sciezki python
#Umozliwia importowanie modulow z tego foldera
sys.path.append(os.getcwd()+"/lib")
#---------------------------------------------

import test_lib

import gdal

if __name__ == "__main__":
    print test_lib.dodaj(3,2)
    print test_lib.znajdz_literke("Geografia","a")