

class ImagePath:
    def __init__(self):
        self.__firstImage = ""
        self.__lastImage = ""

    def setLastImage(self, lastImage):
        self.__lastImage = lastImage

    def getLastImage(self):
        return self.__lastImage