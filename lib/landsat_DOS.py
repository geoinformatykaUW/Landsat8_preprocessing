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
    ktory ma zostac zaimportowany. Wartosci kanału sa dodawane do macierzy.'''
    kanal=input_dat.GetRasterBand(int(bandX))
    matrix=numpy.array(kanal.ReadAsArray(),dtype=numpy.float32)
    return matrix
    
def band_DOS(source,bandX,MP,AP):
    '''Na początku wykonuje kalibracje obrazu, polegającą na przeliczeniu wartości DN na wartości odbicia.
    W tym celu mnoży wartość wartość DN dla każdego piksela na obrazie przez wartość MP a nstępnie dodaje
    do otzrymanego wyniku wartosć AP, gdzie:
    MP = Reflectance multiplicative scaling factor for the band (REFLECTANCE_MULT_BAND_N from the metadata).
    AP = Reflectance additive scaling factor for the band (REFLECTANCE_ADD_BAND_N from the metadata).
    Następnie wykonuje korekcje atmosferyczną metodą Dark Object Subtraction, poprzez odjęcie najnizszej
    dodatniej wartosci odbicia odczytanej z obrazu od wartości odbicia dla pozostałych pikseli na obrazie.
    Jako parametry wejsciowe przyjmuje macierz z wartościam DN, numer kanału oraz wartości MP i AP.'''
    matrix_calibration=upload_band(source,bandX)*MP+AP
    dos_band_matrix=matrix_calibration-min(matrix_calibration[matrix_calibration>0])
    #print min(matrix_calibration[matrix_calibration>0])
    return dos_band_matrix
    
def get_MP(x,metadata_path):
    '''Pobiera wartość MP z metadanych. Jako parametry wejściowe przyjmuje numer analizowanego kanału oraz 
    ścieżkę do pliku z metadanymi. Wykorzystuje utworzony wcześniej skrypt metadane.py.'''
    MP=metadane.wczytanie_danych(metadata_path)['REFLECTANCE_MULT_BAND_'+str(x)]
    return MP    
    
def get_AP(x,metadata_path):
    '''Pobiera wartość AP z metadanych. Jako parametry wejściowe przyjmuje numer analizowanego kanału oraz 
    ścieżkę do pliku z metadanymi.Wykorzystuje utworzony wcześniej skrypt metadane.py.'''
    AP=metadane.wczytanie_danych(metadata_path)['REFLECTANCE_ADD_BAND_'+str(x)]
    return AP
    
def get_matrix_size(metadata_path):
    '''Pobiera wielkość zobrazowania z metadanych. Jako parametry wejściowe przyjmuje
    ścieżkę do pliku z metadanymi. Wykorzystuje utworzony wcześniej skrypt metadane.py.'''
    sizeX=int(metadane.wczytanie_danych(metadata_path)['REFLECTIVE_SAMPLES'])
    sizeY=int(metadane.wczytanie_danych(metadata_path)['REFLECTIVE_LINES'])
    return [sizeX,sizeY]

def save_dos_image(input_landsat,output_bsq,sizeX,sizeY,metadata_path):
    '''Zapisuje obrazy wszystkich kanałow po wykonanych korekcjach do jednego pliku w formacie .bsq.
    Jako parametry wejsciowe przyjmuje otwarty obraz Landsat, ścieżke do zapisu pliku wyjściowego,
    wymiary obrazu wyjściowego oraz ścieżkę dostępu do pliku z metadanymi. Przyjęte zostaje założenie,
    że obraz wejściowy i wyjściowy składa się z 8 kanałow.'''
    print "Wykonuje korekcje obrazu (DOS)"
    sterownik=gdal.GetDriverByName('ENVI')
    sterownik.Register()
    zapis=sterownik.Create(output_bsq,sizeX,sizeY,8,gdal.GDT_Float32)
    for x in range(8):
        x=x+1
        print "Pracuje na kanale"+str(x)
        zapis.GetRasterBand(x).WriteArray(band_DOS(input_landsat,x,get_MP(x,metadata_path),get_AP(x,metadata_path)))#input landsat musi być otwarte przed wywołaniem funkcji
    zapis=None #zwolnienie pamieci
    with open(str(output_bsq[:-4]+'.hdr'),'a') as metadane:
        metadane.write(''.join('band names = { \n Costal (COSTAL Band 1 (435-451 nm)),\n Blue (BLUE Band 2 (452-512 nm)),\n Green (GREEN Band 3 (533-590 nm)),\n Red (RED Band 4 (636-676 nm)),\n NIR (NIR Band 5 (851-879 nm)),\n SWIR1 (SWIR Band 6 (1566-1651 nm)),\n SWIR2 (SWIR Band 7 (2107-2294 nm)),\n Cirrus (Cirrus Band 9 (1363-1374 nm))\n }\nwavelength = {\n 0.443000, 0.482000, 0.561500, 0.656000, 0.865000, 1.608500, 2.200500, 1.368500\n }'))
    
def run_correction(input_image,output_image,metadata_path):
    '''Metoda powoduje wykonanie korekcji atmosferycznej i wszystkich związanych z nią procesow zawartych
    w pozostałych metodach. Jako parametry wejsciowe przyjmuje ścieżke zestackowanego obrazu wejściowego,
    ścieżke do zapisu obrazu po korekcji oraz sciezke do pliku z metadanymi.'''
    save_dos_image(get_input_dat(input_image),output_image,get_matrix_size(metadata_path)[0],get_matrix_size(metadata_path)[1],metadata_path)

#run_correction('D:/studia/progamowanie/rastry/landsat/L8-8band','D:/studia/progamowanie/rastry/landsat/korekcja11.bsq', "D:/Landsat_8_dziewczyny/LC81910232015182LGN00/LC81910232015182LGN00_MTL.txt")  
