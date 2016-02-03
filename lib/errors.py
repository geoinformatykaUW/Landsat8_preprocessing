class NoMetadataFileError(Exception):
    def __init__(self):
        super(Exception,self).__init__()
        self.msg = "Nie znaleziono pliku z metadanymi"
    
    def __str__(self):
        return repr(self.msg)