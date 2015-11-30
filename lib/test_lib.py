# -*- coding: utf-8 -*-

#Modul do testowania dzialania importow


def dodaj(a,b):
	return a+b
def znajdz_literke(slowo,literka):
    """Zwraca liste indeksow wszystkich wystapien szukanej literki
       w danym slowie.
       syntax: znajdz_literke(slowo,literka) string,string
    """
    indeksy_literki = []
    for index in range(len(slowo)):
        if slowo[index].lower() == literka:
            indeksy_literki.append(index)
    return indeksy_literki