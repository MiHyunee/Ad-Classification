from .ImagePath import ImagePath

class BlogPage:

    def __init__(self):
        self.__title = ""
        self.__pageUrl = "" #불필
        self.__imagePath = ImagePath() #불필
        self.__sticker = "" #불필
        self.__firstText = ""
        self.__lastText = ""  #2
        self.__lastOCR = ""  #3
        self.__lastOCRbw = ""  #4
        self.__stickerOCR = ""  #1
        self.__isAd = ""

    def setTitle(self, newTitle):
        self.__title = newTitle

    def setImagePath(self, newImagePath):
        self.__imagePath = newImagePath

    def setPageUrl(self, newPageUrl):
        self.__pageUrl = newPageUrl

    def setSticker(self, newSticker):
        self.__sticker = newSticker

    def setFirstText(self, newFirstText):
        self.__firstText = newFirstText

    def setLastText(self, newLastText):
        self.__lastText = newLastText

    def setLastOCR(self, newLastOCR):
        self.__lastOCR = newLastOCR

    def setLastOCRbw(self, newLastOCRbw):
        self.__lastOCRbw = newLastOCRbw

    def setStickerOCR(self, newStickerOCR):
        self.__stickerOCR = newStickerOCR

    def setIsAd(self, newIsAd):
        self.__isAd = newIsAd

    def getTitle(self):
        return self.__title

    def getImagePath(self):
        return self.__imagePath

    def getPageUrl(self):
        return self.__pageUrl

    def getSticker(self):
        return self.__sticker

    def getFirstText(self):
        return self.__firstText

    def getLastText(self):
        return self.__lastText

    def getFirstOCR(self):
        return self.__firstOCR

    def getLastOCR(self):
        return self.__lastOCR

    def getLastOCRbw(self):
        return self.__lastOCRbw

    def getStickerOCR(self):
        return self.__stickerOCR

    def getIsAd(self):
        return self.__isAd
