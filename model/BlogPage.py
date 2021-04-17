from .ImagePath import ImagePath

class BlogPage:
    firstText = ""
    lastText = ""
    sticker = ""

    def __init__(self):
        self.__title = None
        self.__pageUrl = None
        self.__imagePath = ImagePath()
        self.__sticker = None

    def setTitle(self, newTitle):
        self.__title = newTitle

    def setImagePath(self, newImagePath):
        self.__imagePath = newImagePath

    def setPageUrl(self, newPageUrl):
        self.__pageUrl = newPageUrl

    def setSticker(self, newSticker):
        self.__sticker = newSticker

    def getTitle(self):
        return self.__title

    def getImagePath(self):
        return self.__imagePath

    def getPageUrl(self):
        return self.__pageUrl

    def getSticker(self):
        return self.__sticker

