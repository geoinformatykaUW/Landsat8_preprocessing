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
    kanal=input_dat.GetRasterBand(int(bandX))
    matrix=numpy.array(kanal.ReadAsArray(),dtype=numpy.float32)
    return matrix
    
def band_DOS(source,bandX,MP,AP):
    '''MP = Reflectance multiplicative scaling factor for the band (REFLECTANCEW_MULT_BAND_n from the metadata).
       AP = Reflectance additive scaling factor for the band (REFLECTANCE_ADD_BAND_N from the metadata).'''
    matrix_calibration=upload_band(source,bandX)*MP+AP
    dos_band_matrix=matrix_calibration-min(matrix_calibration[matrix_calibration>0])
    return dos_band_matrix
    
def get_MP():
    '''pobiera wartosc mp z metadanych'''
    MP=0.00002
    return MP    
    
def get_AP():
    '''pobiera wartosc ap z metadanych'''
    AP=-0.1
    return AP
    
def get_matrix_size():
    '''cos'''
    sizeX=7861
    sizeY=7971
    return [sizeX,sizeY]

def save_dos_image(input_landsat,output_bsq,sizeX,sizeY):
    #Funkcja iteruje po
    sterownik=gdal.GetDriverByName('ENVI')
    sterownik.Register()
    zapis=sterownik.Create(output_bsq,sizeX,sizeY,8,gdal.GDT_Float32)#zawsze jest 8 kanalow
    for x in range(8):
        x=x+1
        zapis.GetRasterBand(x).WriteArray(band_DOS(input_landsat,x,get_MP(),get_AP()))#input landsat musi być otwarte przed wywołaniem funkcji
    zapis=None #zwolnienie pamieci
    
def run_correction(input_image,output_image): #jeszcze metadane dla metod get_AP i get_MP
    start=time.time()
    save_dos_image(get_input_dat(input_image),output_image,get_matrix_size()[0],get_matrix_size()[1])
    end=time.time()-start
    print end

#run_correction('D:/studia/progamowanie/rastry/landsat/L8-8band','D:/studia/progamowanie/rastry/landsat/korekcja1.bsq')  




