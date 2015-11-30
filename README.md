# Landsat8 data preprocessing

Projekt przetwarzania danych z satelity Landsat - 8.
Projekt skupia sie na przetworzeniu danych pobranych prosto z earthexplorer w formacie spakowanym (.tar),
a nastepnie przetworzenie go do dalszych prac.

Zakres prac w projekcie:
<ol>
<li> -[ ] 1.Przygotowanie danych:</li>
	<ol>
	<li> -[ ] polacznie danych z sensorow TIRS i OLI w nastepujace zestawy:</li>
			<ol>
			<li>- [ ] Plik z danymi z sensora wielospektralnego OLI, 30m + kompletny header</li>
			<li>- [ ] Plik z kanalem panchromatycznym, 15m + kompletny header</li>
			<li>- [ ] Plik zawierajacy BQA (Band Quality Analysis) + kompletny header</li>
			<li>- [ ] Plik z danymi z sensora TIRS + kompletny header</li>
			</ol>
	<li> -[ ] wyciagniecie danych z pliku z metadanymi (zestaw funkcji do parsownia pliku lub                                       zapisanie tych danych do innego pliku w formacie .csv)</li>
	</ol>	                                            
	<li> -[ ] 2.Wstepne przetwarzanie:</li>
		<ol>
		<li> -[ ] implementacja algorytmu do maskowania chmur i wykrywania cieni</li>
		<li> -[ ] opracowanie mask chmur, cieni i zbiornikow wodnych</li>
		</ol>
	<li> -[ ] 3.Korekcja danych z sensora OLI</li>
</ol>
