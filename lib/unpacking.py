# -*- coding: utf-8 -*-
#Modul do rozpakowywania spakownych scen w formacie tar.gz 
#Wypadowuje zawartosc archwum do wybranego katalogu

import os
import sys
import tarfile


class UnpackArchive(object):
    """
    Klasa do wypakowania archiwum tar.gz do wybranego katalogu
    
    Wlasciwosci:
        self.archive_path :absolutna sciezka do archiwum
        self.save_path :absolutna sciezka do miejsca wypakowania zawartosci archiwum
        self.sucess :True jezeli wypakowywanie skonczylo sie sukcesem
        
    Metody publiczne:
        unpack_into_dir(save_directory): wypakowuje zawartosc archiwum do wskazanego miejsca
    """
    def __init__(self,file):
        if self._check_archive(file):
            self.archive_path = os.path.abspath(file)
        else:
            #jak plik nie jest archiwum zakończ bez tworzenia obiektu
            raise IOError("Plik nie jest archiwum tar.gz")
            
    def _check_archive(self,file):
        """
        Sprawdza czy plik konczy sie na .tar.gz -> archiwum    
        """
        return file.endswith("tar.gz")

    def unpack_into_dir(self, save_directory):
        """
        Wypakowuje zawartosc archiwum do save_directory.
        Jezeli save_directory nie istnieje to tworzy nowy folder/nowe foldery.
        """
        self.save_path =  os.path.abspath(save_directory)
        if self._check_if_dir_exists(save_directory) == False:
            self._unpack_targz_file()
        else:
            os.mkdir(self.save_path)
            self._unpack_targz_file()
        
    def _check_if_dir_exists(self, directory):
        """
        Sprawdza czy plik konczy sie na .tar.gz -> archiwum    
        """
        return os.path.exists(directory)   
        
    def _unpack_targz_file(self):
        """
        wypakowuje archiwum przy uzyciu modulu tarfile  
        """
        try:
            with tarfile.open(self.archive_path) as tar_file:
                tar_file.extractall(path=self.save_path) 
            self.sucess = True
        except IOError as e:
            self.sucess = False
            print e
    
    
    
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
