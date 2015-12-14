# -*- coding: utf-8 -*-
#Modul do rozpakowywania spakownych scen w formacie tar.gz 
#Wypadowuje zawartosc archwum do wybranego katalogu

import os
import sys
import tarfile

def un_gzip_file(archive, write_file):
    """
    Wypakowuje zawartosc archium do danego katalogu
    Argumenty:
        archive: sciezka do archiwum (relatywna wzgledem foldera roboczego)
        write_file: nazwa katalogu do ktorego zostana rozpakowane
                    zawartosci archiwum (relatywna wzgledem foldera roboczego)
    """
    try:
        archive_file, save_dir = preapare_paths_dirs(archive, write_file)
        unpack_into_dir(archive_file,save_dir)
        print "Skończono wypakowywanie archiwum"
    except IOError:
        print "Archiwum w złym formacie: " + archive
        
def preapare_paths_dirs(archive, write_file):
    """
    Funkcja sprawdzajaca czy dane archiwum(archive) istnieje.
    Przygotowuje sciezki do przetwarzania
    Zwraca:
        nazwe archiwum,
        absoluta sciezke do katalogu zapisu
    """
    if check_if_archive(archive):
        archive_file = os.path.abspath(archive)  
        save_dir = os.path.abspath(write_file)
        return archive_file, save_dir
    else:
        raise IOError        
        
def check_if_archive(file):
    """
    Sprawdza czy plik konczy sie na .tar.gz -> archiwum    
    """
    return file.endswith("tar.gz")

def unpack_into_dir(archive_file,save_dir):
    """
    Sprawdza czy folder na wynik istneje. Jezeli nie to go tworzy.
    Nastepnie wywoluje funkcje unpack_targz_file(archive_file, save_dir)  
    """
    if check_if_dir_exists(save_dir):
        unpack_targz_file(archive_file,save_dir)     
    else:
        os.mkdir(save_dir)
        unpack_targz_file(archive_file,save_dir)
        
def check_if_dir_exists(dir):
    return os.path.exists(dir)

def unpack_targz_file(archive_file, save_dir):
    """
    Wypakowuje zawartosc archiwum do save_dir(abspath)    
    """
    try:
        with tarfile.open(archive_file) as tar_file:
            tar_file.extractall(path=save_dir) 
    except IOError as e:
        print "Nie ma takiego pliku. Sprawdz nazwe lub sciezke"
        sys.exit(2)