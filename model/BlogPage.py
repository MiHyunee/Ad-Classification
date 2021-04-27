from .ImagePath import ImagePath

class BlogPage:

    def __init__(self):
        self.__title = None
        self.__pageUrl = None
        self.__imagePath = ImagePath()
        self.__sticker = None
        self.__firstText = None
        self.__lastText = None
        self.__firstOCR = None
        self.__lastOCR = None
        self.__stickerOCR = None

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

    def setFirstOCR(self, newFirstOCR):
        self.__firstOCR = newFirstOCR

    def setLastOCR(self, newLastOCR):
        self.__lastOCR = newLastOCR

    def setStickerOCR(self, newStickerOCR):
        self.__stickerOCR = newStickerOCR

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

    def getStickerOCR(self):
        return self.__stickerOCR
