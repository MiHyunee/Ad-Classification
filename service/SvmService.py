import joblib
from . import SvmTrainingService as training


def svm(blogArray):
    #model load
    model = joblib.load('static/svm_model.pkl')

    #객체마다 분석
    for i in blogArray:
        title = i.getTitle()
        firstText = i.getFirstText()
        lastText = i.getLastText()
        firstOcr = i.getFirstOCR()
        lastOcr = i.getLastOCR()
        stickerOcr = i.getStickerOCR()
        #text = [title + firstText + lastText + lastOcr + firstOcr + stickerOcr]
        text = [lastOcr]

        print(text)
        isAd = model.predict(text)
        print("yPredict: ", isAd)
        i.setIsAd(isAd)
        print(i.getPageUrl(), " : ", i.getIsAd())

