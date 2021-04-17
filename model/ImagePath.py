

class ImagePath:
    def __init__(self):
        self.__firstImage = None
        self.__lastImage = None

    def setFirstImage(self, firstImage):
        self.__firstImage = firstImage

    def setLastImage(self, lastImage):
        self.__lastImage = lastImage

    def getFirstImage(self):
        return self.__firstImage

    def getLastImage(self):
        return self.__lastImage