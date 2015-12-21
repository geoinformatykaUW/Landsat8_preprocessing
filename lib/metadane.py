# -*- coding: utf-8 -*-


def wczytanie_danych(plik):
	"""
	Wczytywanie danych z pliku z metadanymi satelity Landsat 8.
	"""
	p = open(plik, 'r')
	pojemnik = {}
	for linia in p:
		elementy = linia.split("=")
		if len(elementy) == 2:
			pojemnik[elementy[0].strip()] = elementy[1].strip()
	p.close()
	return pojemnik

#class Dane(object):
#	"""
#	Klasa posiadająca atrybuty
#	"""
#	def __init__(self):
#	#zdefiniowanie wartosci domyslnych, ktore bedziemy mogli pozniej zmieniac z uzyciem metody
#		self.nazwa = "Figura"
#		self.kolor = "bialy"

	
if __name__=="__main__":
	try:
		dane = wczytanie_danych("..\dane\sceny\LC81910232015182LGN00_MTL.txt")
	except IOError as e:
        print "Nie ma takiego pliku. Sprawdz nazwe lub sciezke"
        sys.exit(2)
	


