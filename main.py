# -*- coding: utf-8 -*-
<<<<<<< HEAD
import sys, os
=======
import sys,os
>>>>>>> master
#---------------------------------------------
#Dodanie foldera lib do sciezki python
#Umozliwia importowanie modulow z tego foldera
sys.path.append(os.getcwd()+"/lib")
#---------------------------------------------

<<<<<<< HEAD
import unpacking

if __name__ == "__main__":
    
    in_file="dane/LC81910232015262LGN00.tar.gz"
    write_dir="dane/sceny"
    
    unpacking.un_gzip_file(in_file, write_dir)   
=======
if __name__ == "__main__":
    pass
>>>>>>> master
