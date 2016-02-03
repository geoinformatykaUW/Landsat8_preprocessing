# -*- coding: utf-8 -*-
#Zestaw funkcji ogolnego uzycia

import os
import errors


def find_metadata_file(path):
    files = os.listdir(path)        
    for file in files:
        if file.endswith("MTL.txt"):
            return path +"\\" + file
    raise errors.NoMetadataFileError