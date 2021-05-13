import joblib

def svm(blogArray):
    #model load
    model = joblib.load('./svm_best.pkl')

    #객체마다 분석
    for i in blogArray:
        test = i.getTitle()+i.getFirstText()+i.getLastText()\
               +i.getFirstOCR+i.getLastOCR()+i.getStickerOCR()

        i.setIsAd(model.predict(test))
