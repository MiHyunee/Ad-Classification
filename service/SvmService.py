import joblib
from . import DataMiningService as dm
from tensorflow.keras.preprocessing.sequence import pad_sequences


def svm(blogArray, vecMaxLen):
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
        text = title + firstText + lastText + lastOcr + firstOcr + stickerOcr

        vector = dm.tokenizer2(text)
        x_vector = pad_sequences(vector, maxlen=vecMaxLen)
        print(x_vector)
        isAd = model.predict(x_vector)
        i.setIsAd(isAd)
        print(i.getPageUrl(), " : ", i.getIsAd())
    '''
    #한문장씩 테스트 돌리기
    t = model.predict(i.getTitle())
    ft = model.predict(i.getFirstText())
    lt = model.predict(i.getLastText())
    fo = model.predict(i.getFirstOCR())
    lo = model.predict(i.getLastOCR())
    st = model.predict(i.getStickerOCR())
    if(t+ft+lt_fo+lo+st == 0):
        i.setIsAd(FALSE)
    else:
        i.setIsAd(TRUE)
    '''
