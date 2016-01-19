# -*- coding: utf-8 -*-
#Wyciągnięcie danych z pliku z metadanymi w postaci obiektu i jego atrybutów
import os

	
class Struct(object):
	"""
	Klasa zwraca obiekt o właściwościach odpowiadających kluczom w słowniku
	"""
	def __init__(self,**entries):
		self.__dict__.update(entries)

class Dane(object):
	"""
	Klasa posiadająca atrybuty zgodne z metadanymi
	"""
	def __init__(self):
		pass
		
	def czyt_atrybuty(self):
		"""
		Metoda wczytuje metadane ze słownika
		"""
		obj = Struct(**self.pojemnik)
		del self.pojemnik
		self.metadane = obj
		
	def wczytanie_danych(self,plik):
		"""
		Wczytywanie danych z pliku z metadanymi satelity Landsat 8.
		"""
		p = open(plik, 'r')
		pojemnik = {}
		for linia in p:
			elementy = linia.split("=")
			if len(elementy) == 2:
				wartosc = elementy[1].strip().strip('"')
				try:
					wartosc = float(wartosc)
				except:
					pass
				pojemnik[elementy[0].strip()] = wartosc
		p.close()
		self.pojemnik = pojemnik
	
		

	
if __name__=="__main__":
	try:
		print os.getcwd()
		scena_landsat = Dane()
		scena_landsat.wczytanie_danych("..\dane\sceny\LC81910232015182LGN00_MTL.txt")
		#metadane = Dane(dane_slownik)
		
		scena_landsat.czyt_atrybuty()
		
	except IOError as e:
		print "Nie ma takiego pliku. Sprawdz nazwe lub sciezke"
		sys.exit(2)
	


