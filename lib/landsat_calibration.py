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
    
def band_reflectance(source,bandX,MP,AP):
    '''MP = Reflectance multiplicative scaling factor for the band (REFLECTANCEW_MULT_BAND_n from the metadata).
       AP = Reflectance additive scaling factor for the band (REFLECTANCE_ADD_BAND_N from the metadata).'''
    #matrix1=[REFLECTANCEW_MULT_BAND_n*x for x in upload_band(input_Landsat,1)-REFLECTANCE_ADD_BAND_N]
    matrix_calibration=upload_band(source,bandX)*MP+AP
    return matrix_calibration
    
def get_MP():
    '''pobiera wartosc mp z metadanych'''
    MP=0.00002
    return MP    
    
def get_AP():
    '''pobiera wartosc ap z metadanych'''
    AP=-0.1
    return AP
    
def save_cal_image(input_landsat,output_bsq,sizeX,sizeY):
    '''Funkcja iteruje po'''
    sterownik=gdal.GetDriverByName('ENVI')
    sterownik.Register()
    zapis=sterownik.Create(output_bsq,sizeX,sizeY,7,gdal.GDT_Float32)#zawsze jest 7 kanalow
    for x in range(7):
        x=x+1
        zapis.GetRasterBand(x).WriteArray(band_reflectance(input_landsat,x,get_MP(),get_AP()))#input landsat musi być otwarte przed wywołaniem funkcji
    zapis=None #zwolnienie pamieci
    
def run_calibration(input_image,output_image): #jeszcze metadane dla metod get_AP i get_MP
    #print upload_band(input_Landsat,1)
    save_cal_image(get_input_dat(input_image),output_image,500,500)

run_calibration('D:/studia/progamowanie/rastry/LandSat8_Wielkopolska_multispectral_10band-500x500.bsq','D:/studia/progamowanie/rastry/LandSat8_cali_new4.bsq')  



#REFLECTANCE_ADD_BAND_N=-0.1
#REFLECTANCE_MULT_BAND_n=0.00002    
#reflectance(input_Landsat,5
