# -*- coding: utf-8 -*-
import sys, os
#---------------------------------------------
#Dodanie foldera lib do sciezki python
#Umozliwia importowanie modulow z tego foldera
sys.path.append(os.getcwd()+"/lib")
#---------------------------------------------
import unpacking
import metadane

if __name__ == "__main__":
	
	in_file="dane/LC81910232015182LGN00.tar.gz"
	write_dir="dane/sceny"
	#unpacking.un_gzip_file(in_file, write_dir)   


	
	
	scena_landsat = metadane.Dane()
	scena_landsat.wczytanie_danych("dane\sceny\LC81910232015182LGN00_MTL.txt")
	scena_landsat.czyt_atrybuty()
	prawdziwe_metadane = scena_landsat.metadane