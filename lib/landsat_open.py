# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 12:52:27 2015

@author: Janek Mazur, Hubert Zieliński, Paweł Przychodzień
"""
import gdal, gdalconst, numpy, time

def get_input_dat(input_path):
    '''Otwiera obraz Landsata 8. Jako parametr wejściowy przyjmuje scieżkę
    do pliku .bsq'''
    sterownik=gdal.GetDriverByName('ENVI')
    sterownik.Register()
    input_dat=gdal.Open(input_path,gdalconst.GA_ReadOnly)
    return input_dat
    
def upload_band(input_dat,bandX):
    '''Pobiera wartości zadanego kanału z określonego zobrazowania landsat 8.
    Jako parametry wejściowe przyjmuje cieżkę do pliku obrazu *.bsq i numer kanału
    ktory ma zostac zaimportowany. Wartosci kanału sa dodawane do macieży.'''
    kanal=input_dat.GetRasterBand(bandX)
    matrix=numpy.array(kanal.ReadAsArray(),dtype=numpy.float32)
    return matrix
    
input_Landsat=get_input_dat('D:/studia/progamowanie/rastry/LandSat8_Wielkopolska_multispectral_10band-500x500.bsq')
#print upload_band(input_Landsat,1)

REFLECTANCE_ADD_BAND_N=-0.1
REFLECTANCE_MULT_BAND_n=0.00002
def reflectance(source,bandX):
    start_time=time.time()
    #matrix1=[REFLECTANCEW_MULT_BAND_n*x for x in upload_band(input_Landsat,1)-REFLECTANCE_ADD_BAND_N]
    matx=upload_band(input_Landsat,1)*REFLECTANCE_MULT_BAND_n+REFLECTANCE_ADD_BAND_N
    end_time=time.time()-start_time
    return matx
    
reflectance(input_Landsat,5)    


sterownik=gdal.GetDriverByName('ENVI')
sterownik.Register()
zapis=sterownik.Create('D:/studia/progamowanie/rastry/JAKIES_COS1.bsq',500,500,1,gdal.GDT_Float32)
zapis.GetRasterBand(1).WriteArray(reflectance(input_Landsat,1))
zapis=None
