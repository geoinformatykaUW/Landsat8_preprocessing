def tile_img_processing(raster_band,tile_size):
    """Funkcja zwraca generator ktory przy iteracji zwraca poszczegolne
    kafelki z danego obrazu (raster_band)
    Argumenty:
        raster_band : obiekt klasy Band z modulu gdal
        tile_size: rozmiar pojedynczego kafelka (w pikselach)
    Zwraca macierz o wymiarach kafelka
    """
    img_y_size = raster_band.YSize
    img_x_size = raster_band.XSize
 
    for UL_y_cooridnate in range(0,img_y_size,tile_size):
        if UL_y_cooridnate + tile_size < img_y_size:
            numRows = tile_size
        else:
            numRows = img_y_size - UL_y_cooridnate
        for UL_x_cooridnate in range(0,img_x_size,tile_size):
            if UL_x_cooridnate + tile_size < img_x_size:
                numCols = tile_size
            else:
                numCols = img_x_size - UL_x_cooridnate
            #zwraca kafelek + wspolrzedne x i y lewego gornego rogu przetwarzanego kafelka    
            yield raster_band.ReadAsArray(UL_x_cooridnate,UL_y_cooridnate, numCols, numRows), UL_x_cooridnate, UL_y_cooridnate