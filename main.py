# -*- coding: utf-8 -*-
import sys, os
#---------------------------------------------
#Dodanie foldera lib do sciezki python
#Umozliwia importowanie modulow z tego foldera
sys.path.append(os.getcwd()+"/lib")
#---------------------------------------------
import unpacking

if __name__ == "__main__":
    
<<<<<<< HEAD
    in_file="dane/LC81910232015262LGN00.tar.gz"
    write_dir="dane/sceny" 
=======
    in_file="dane/LC81910232015182LGN00.tar.gz"
    write_dir="dane/sceny"
>>>>>>> unpacking

    archive = unpacking.UnpackArchive(in_file)
    archive.unpack_into_dir(write_dir)
    