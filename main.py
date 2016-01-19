# -*- coding: utf-8 -*-
import sys, os
#---------------------------------------------
#Dodanie foldera lib do sciezki python
#Umozliwia importowanie modulow z tego foldera
sys.path.append(os.getcwd()+"/lib")
#---------------------------------------------
import unpacking, metadane,landsat_DOS

if __name__ == "__main__":
    
    in_file="dane/LC81910232015182LGN00.tar.gz"
    write_dir="dane/sceny"

    unpacking.un_gzip_file(in_file, write_dir)

#landsat_DOS.run_correction('D:/studia/progamowanie/rastry/landsat/L8-8band','D:/studia/progamowanie/rastry/landsat/korekcja_sprawdz.bsq',"D:/LC81910232015182LGN00/LC81910232015182LGN00_MTL.txt")
