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

#Wejscie
plik = "dane/sceny/LC81910232015262LGN00_B5.TIF"
sterownik_tif = gdal.GetDriverByName("GTiff")
sterownik_tif.Register()
dane = gdal.Open(plik,gdalconst.GA_ReadOnly)
kanal_5 = dane.GetRasterBand(1)
#nformacje o pliku
x_size = dane.RasterXSize
y_size = dane.RasterYSize
proj = dane.GetProjection()
geotransform = dane.GetGeoTransform()

#Wyjscie
plik_zapis = "wynik/rad_ref_5.bsq"
sterownik_bsq = gdal.GetDriverByName("ENVI")
sterownik_bsq.Register()
zapis = sterownik_bsq.Create(plik_zapis,dane.RasterXSize,dane.RasterYSize,1,gdal.GDT_UInt16)
zapis.SetProjection(proj)
zapis.SetGeoTransform(geotransform)
zapis.SetMetadata(dane.GetMetadata())

#stale do obliczen
RADIANCE_MULT_BAND_5 = 9.8986E-03
RADIANCE_ADD_BAND_5 = -49.49291
TILE_SIZE =128

#tiles jest generatorem ktory na wzroci kafelki jezeli po nim iterujemy
tiles = tile_processing.tile_img_processing(kanal_5 ,TILE_SIZE)

for tile, column, row in tiles:
    #przetwarzanie kafelka
    rad_ref = ((tile* RADIANCE_MULT_BAND_5) + RADIANCE_ADD_BAND_5)*100
    zapis.GetRasterBand(1).WriteArray(rad_ref, column, row)
        
rad_ref=None
zapis = None
plik = None
