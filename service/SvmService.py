import joblib
from . import SvmTrainingService as training


def svm(blogArray):
    #model load
    model = joblib.load('static/svm_model.pkl')

    #객체마다 분석
    for i in blogArray:
        print(i.getPageUrl())
        stickerOcr = [i.getStickerOCR()]
        isAd = model.predict(stickerOcr)
        if isAd==1:
            print("sticker: ", stickerOcr)
            i.setIsAd(isAd)
            continue
        lastText = [i.getLastText()]
        isAd = model.predict(lastText)
        if isAd==1:
            print("lastText: ", lastText)
            i.setIsAd(isAd)
            continue
        lastOcr = [i.getLastOCR()]
        isAd = model.predict(lastOcr)
        if isAd==1:
            print("lastOcr: ", lastOcr)
            i.setIsAd(isAd)
            continue
        lastOcrbw = [i.getLastOCRbw()]
        isAd = model.predict(lastOcrbw)
        if isAd==1:
            print("lastOcrbw: ", lastOcrbw)
            i.setIsAd(isAd)
            continue
        title = [i.getTitle()]
        isAd = model.predict(title)
        if isAd==1:
            print("title: ", title)
            i.setIsAd(isAd)
            continue
        firstText = [i.getFirstText()]
        isAd = model.predict(firstText)
        if isAd==1:
            print("firstText: ", firstText)
            i.setIsAd(isAd)
            continue
        i.setIsAd(isAd)   #광고아님

