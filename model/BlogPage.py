from .ImagePath import ImagePath

class BlogPage:

    def __init__(self):
        self.__title = None
        self.__pageUrl = None
        self.__imagePath = ImagePath()
        self.__sticker = None
        self.__firstText = None
        self.__lastText = None

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

