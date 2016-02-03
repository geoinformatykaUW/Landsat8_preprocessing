# -*- coding: utf-8 -*-
import sys, os
#---------------------------------------------
#Dodanie foldera lib do sciezki python
#Umozliwia importowanie modulow z tego foldera
sys.path.append(os.getcwd()+"/lib")
#---------------------------------------------
import unpacking
import metadane 
import landsat_DOS
import utils
import stakowanie

if __name__ == "__main__":
    
    in_file="dane/LC81910232015262LGN00.tar.gz"
    write_dir="dane/sceny"

    #archive = unpacking.UnpackArchive(in_file)
    #archive.unpack_into_dir(write_dir)
    path_to_mtl = utils.find_metadata_file(archive.save_path)
    dane_slownik = metadane.wczytanie_danych(path_to_mtl)
    scena_metadane = metadane.Dane(dane_slownik)
    
    
    stakowanie.stackowanie_kanalow_OLI(archive.save_path,
                                       archive.save_path+"OLI_8band.bsq",
                                       int(scena_metadane.metadane.REFLECTIVE_SAMPLES),
                                       int(scena_metadane.metadane.REFLECTIVE_LINES))
    stakowanie.stackowanie_kanalow_TIRS(archive.save_path,
                                       archive.save_path+"TIRS_2band.bsq",
                                       int(scena_metadane.metadane.THERMAL_SAMPLES),
                                       int(scena_metadane.metadane.THERMAL_LINES))
    landsat_DOS.run_correction(archive.save_path+"OLI_8band.bsq",
                               archive.save_path+"DOS_OLI.bsq",
                               path_to_mtl)
