# Landsat8_preprocessing

Projekt przetwarzania danych z satelity Landsat - 8.
Projekt skupia sie na przetworzneniu danych pobranych prosto z earthexplorer w formacie spakowanym (.tar),
a nastepnie przetworznie go do dalszych prac.

Zakres prac w projekcie:
	1.Przygotowanie danych:
		a) polacznie danych z sensorow TIRS i OLI w nastepujace zestawy:
			-Plik z danymi z sensora wielospektralnego OLI, 30m + kompletny header
			-Plik z kanalem panchromatycznym, 15m + kompletny header
			-Plik zawierajacy BQA (Band Quality Analysis) + kompletny header
			-Plik z danymi z sensora TIRS + kompletny header
		b)wyciagniecie danych z pliku z metadanymi (zestaw funkcji do parsownia pliku lub
		                                            zapisanie tych danych do innego pliku w formacie .csv)
	2.Wstepne przetwaranie:
		a) implementacja algorytmu do maskowania chmur i wykrywania cieni
		b) opracowanie mask chmur, cieni i zbiornikow wodnych
	3.Korekcja danych z sensora OLI
