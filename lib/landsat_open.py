# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 12:52:27 2015

@author: Janek
"""
"cos"
import gdal, gdalconst, numpy
def get_input_dat(input_path):
	sterownik=gdal.GetDriverByName('ENVI')
	sterownik.Register()
	input_dat=gdal.Open(input_path,gdalconst.GA_ReadOnly)
	return input_dat
def upload_band(input_dat,bandX):
	kanal=input_dat.GetRasterBand(bandX)
	matrix=numpy.array(kanal.ReadAsArray(),dtype=numpy.float32)
	return matrix
input_Landsat=get_input_dat('D:/studia/progamowanie/rastry/LandSat8_Wielkopolska_multispectral_10band-500x500.bsq')
upload_band(input_Landsat,1)