# -*- coding: utf-8 -*-
import os ,time
from osgeo import gdal

def znajdz_pliki(folder):
	"""
	funkcja wyszukujaca pliki o rozszerzeniu TIF. nalezy podac 
	sciezke dostepu do folderu w ktorym wyszukujemy pliki.
	"""
	lista_kanalow =[]
	for plik in os.listdir(folder):
		if plik.endswith(".TIF"):
			lista_kanalow.append(plik)
	return lista_kanalow


def utworz_zbiory(lista_kanalow):
	kanaly_OLI = []
	kanaly_TIRS = []
	kanal_BQA = []
	kanal_PAN =[]	
	for kanal in lista_kanalow:
		if kanal.endswith("B10.TIF") or kanal.endswith("B11.TIF"):
			kanaly_TIRS.append(kanal)
		elif kanal.endswith("B8.TIF"):
			kanal_PAN.append(kanal)
		elif kanal.endswith("BQA.TIF"):
			kanal_BQA.append(kanal)
		else:
			kanaly_OLI.append(kanal)		
	return kanaly_TIRS, kanaly_OLI, kanal_BQA, kanal_PAN
	

def stackowanie_kanalow_OLI(folder_wejscia,plik_zapisu):
    """
    funkcja laczaca ze soba pojedyncze kanaly sensora OLI oraz TIRS w dwa oddzielne pliki
    """
    sterownik=gdal.GetDriverByName('ENVI')
    sterownik.Register()
    zapis=sterownik.Create(plik_zapisu,7861,7971,8,gdal.GDT_Int16)#po zmerdzowaniu kodu z innymi trzeba bedzie skorzystac z metody odczytujacej wielkosci rastra z metadanych 
    licznik=-1
    for x in utworz_zbiory(znajdz_pliki(folder_wejscia))[1]:
        licznik+=1
        raster_band=gdal.Open(folder_wejscia+'//'+x).ReadAsArray()
        zapis.GetRasterBand(licznik+1).WriteArray(raster_band)
    zapis=None
    with open(str(plik_zapisu[:-4]+'.hdr'),'a') as metadane:
        metadane.write(''.join('band names = { \n Costal (COSTAL Band 1 (435-451 nm)),\n Blue (BLUE Band 2 (452-512 nm)),\n Green (GREEN Band 3 (533-590 nm)),\n Red (RED Band 4 (636-676 nm)),\n NIR (NIR Band 5 (851-879 nm)),\n SWIR1 (SWIR Band 6 (1566-1651 nm)),\n SWIR2 (SWIR Band 7 (2107-2294 nm)),\n Cirrus (Cirrus Band 9 (1363-1374 nm))\n }\nwavelength = {\n 0.443000, 0.482000, 0.561500, 0.656000, 0.865000, 1.608500, 2.200500, 1.368500\n }'))


def stackowanie_kanalow_TIRS(folder_wejscia,plik_zapisu):
    """
    funkcja laczaca ze soba pojedyncze kanaly sensora OLI oraz TIRS w dwa oddzielne pliki
    """
    sterownik=gdal.GetDriverByName('ENVI')
    sterownik.Register()
    zapis=sterownik.Create(plik_zapisu,7861,7971,2,gdal.GDT_Int16)#po zmerdzowaniu kodu z innymi trzeba bedzie skorzystac z metody odczytujacej wielkosci rastra z metadanych
    licznik=-1
    for x in utworz_zbiory(znajdz_pliki(folder_wejscia))[0]:
        licznik+=1
        raster_band=gdal.Open(folder_wejscia+'//'+x).ReadAsArray()
        zapis.GetRasterBand(licznik+1).WriteArray(raster_band)
    zapis=None
    with open(str(plik_zapisu[:-4]+'.hdr'),'a') as metadane_TIRS:
        metadane_TIRS.write(''.join('band names = {\n TIR-1 (TIR-1 Band 10 (10600-11190 nm)),\n TIR-2 (TIR-2 Band 11 (11500-12510 nm))}\nwavelength = {\n10.895000, 12.005000\n }'))


stackowanie_kanalow_OLI("C:/Studia_2015-2016/Szczesna/Programowanie/Projekt_landsat/Landsat8_preprocessing/dane/sceny",'C:/Studia_2015-2016/Szczesna/Programowanie/Projekt_landsat/Landsat8_preprocessing/dane/sceny/stack8.bsq')
stackowanie_kanalow_TIRS("C:/Studia_2015-2016/Szczesna/Programowanie/Projekt_landsat/Landsat8_preprocessing/dane/sceny",'C:/Studia_2015-2016/Szczesna/Programowanie/Projekt_landsat/Landsat8_preprocessing/dane/sceny/stack8_TIRS.bsq')
