# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 12:52:27 2015

@author: Janek Mazur, Hubert Zieliński, Paweł Przychodzień
"""
import gdal, gdalconst, numpy, metadane

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
    #print min(matrix_calibration[matrix_calibration>0])
    return dos_band_matrix
    
def get_MP(x,metadata_path):
    '''pobiera wartosc mp z metadanych'''
    MP=metadane.wczytanie_danych(metadata_path)['REFLECTANCE_MULT_BAND_'+str(x)]
    return MP    
    
def get_AP(x,metadata_path):
    '''pobiera wartosc ap z metadanych'''
    AP=metadane.wczytanie_danych(metadata_path)['REFLECTANCE_ADD_BAND_'+str(x)]
    return AP
    
def get_matrix_size(metadata_path):
    '''cos'''
    sizeX=int(metadane.wczytanie_danych(metadata_path)['REFLECTIVE_SAMPLES'])
    sizeY=int(metadane.wczytanie_danych(metadata_path)['REFLECTIVE_LINES'])
    return [sizeX,sizeY]

def save_dos_image(input_landsat,output_bsq,sizeX,sizeY,metadata_path):
    #Funkcja iteruje po
    sterownik=gdal.GetDriverByName('ENVI')
    sterownik.Register()
    zapis=sterownik.Create(output_bsq,sizeX,sizeY,8,gdal.GDT_Float32)#zawsze jest 8 kanalow
    for x in range(8):
        x=x+1
        zapis.GetRasterBand(x).WriteArray(band_DOS(input_landsat,x,get_MP(x,metadata_path),get_AP(x,metadata_path)))#input landsat musi być otwarte przed wywołaniem funkcji
    zapis=None #zwolnienie pamieci
    
def run_correction(input_image,output_image,metadata_path): #jeszcze metadane dla metod get_AP i get_MP
    save_dos_image(get_input_dat(input_image),output_image,get_matrix_size(metadata_path)[0],get_matrix_size(metadata_path)[1],metadata_path)

#run_correction('D:/studia/progamowanie/rastry/landsat/L8-8band','D:/studia/progamowanie/rastry/landsat/korekcja8.bsq', "D:/Landsat_8_dziewczyny/LC81910232015182LGN00/LC81910232015182LGN00_MTL.txt")  





    
  




