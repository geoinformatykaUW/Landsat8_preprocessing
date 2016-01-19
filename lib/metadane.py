# -*- coding: utf-8 -*-
#Wyciągnięcie danych z pliku z metadanymi w postaci obiektu i jego atrybutów

def wczytanie_danych(plik):
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
	return pojemnik
	
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
	def __init__(self,slownik):
		self.dane = slownik
		#self.data = slownik['DATE_ACQUIRED']
	def czyt_atrybuty(self):
		"""
		Metoda wczytuje metadane ze słownika
		"""
		obj = Struct(**self.dane)
		self.metadane = obj
		

	
if __name__=="__main__":
	try:
		print os.getcwd()
		dane_slownik = wczytanie_danych("D:/Landsat_8_dziewczyny/LC81910232015182LGN00/LC81910232015182LGN00_MTL.txt")
		metadane = Dane(dane_slownik)
		
	except IOError as e:
		print "Nie ma takiego pliku. Sprawdz nazwe lub sciezke"
		sys.exit(2)
	