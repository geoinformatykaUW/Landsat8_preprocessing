# -*- coding: utf-8 -*-
import sys, os
#---------------------------------------------
#Dodanie foldera lib do sciezki python
#Umozliwia importowanie modulow z tego foldera
sys.path.append(os.getcwd()+"/lib")
#---------------------------------------------
import tile_processing

import gdal
import gdalconst
import numpy
import matplotlib.pyplot as plt
from timeit import default_timer as timer

#Wejscie
plik = "dane/sceny/LC81910232015262LGN00_B5.TIF"
sterownik_tif = gdal.GetDriverByName("GTiff")
sterownik_tif.Register()
dane = gdal.Open(plik,gdalconst.GA_ReadOnly)
kanal_5 = dane.GetRasterBand(1)

#stale do obliczen
RADIANCE_MULT_BAND_5 = 9.8986E-03
RADIANCE_ADD_BAND_5 = -49.49291

#Parametry optymalizacji (wielkosc kafelka)
TILE_SIZE_START = 32
TILE_SIZE_END = 512
TILE_INTERVAL = 8

#liczy czasy przetwarzania dla roznych wielkosci kafelka
proc_times = []
for tile_size in range(TILE_SIZE_START,TILE_SIZE_END+1,TILE_INTERVAL):
    tiles = tile_processing.tile_img_processing(kanal_5 ,tile_size)
    start = timer()
    for tile, column, row in tiles:
        TOA_ref = ((tile* RADIANCE_MULT_BAND_5) + RADIANCE_ADD_BAND_5)
    proc_times.append(str(timer()-start)) 

totals = numpy.asarray(proc_times).astype(numpy.float)/len(proc_times)

#Rysowanie wykresu i zapisanie go na dysku
plt.plot(proc_times)
#os X
plt.xticks(range(0,len(totals)+1,4),range(TILE_SIZE_START,TILE_SIZE_END+1,TILE_INTERVAL*4))
plt.tick_params(axis='x', which='major', labelsize=5)
#os y
plt.yticks([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5],[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
#Dekoracje
plt.title("Rozmiar kafelka a szybkosc przetwarzania")
plt.xlabel("Rozmiar kafelka")
plt.ylabel("sekundy")
plt.grid(True)
plt.savefig("wynik/tile_size_proc_times_PLOT.png",dpi=300)

