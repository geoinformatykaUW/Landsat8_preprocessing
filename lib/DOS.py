# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:59:47 2015

@author: Janek
"""

import landsat_calibration, numpy

input_landsat=landsat_calibration.get_input_dat('D:/studia/progamowanie/rastry/landsat/output1.bsq')

def DOS(source,bandX):
    band_matrix=landsat_calibration.upload_band(source,bandX)
    
    for x,y in band_matrix:
        if y >=0:
            
    
DOS(input_landsat,1)
    
#def DOSggg(input_landsat,output_bsq,sizeX,sizeY):
#    '''Funkcja iteruje po'''
#    sterownik=gdal.GetDriverByName('ENVI')
#    sterownik.Register()
#    zapis=sterownik.Create(output_bsq,sizeX,sizeY,get_band_q(),gdal.GDT_Float32)#zawsze jest 7 kanalow
#    for x in range(get_band_q()):
#        x=x+1
#        zapis.GetRasterBand(x).WriteArray(band_reflectance(input_landsat,x,get_MP(),get_AP()))#input landsat musi być otwarte przed wywołaniem funkcji
#    zapis=None #zwolnienie pamieci