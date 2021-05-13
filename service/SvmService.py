import joblib

def svm(blogArray):
    #model load
    model = joblib.load('./svm_best.pkl')

    #객체마다 분석
    for i in blogArray:
        test = i.getTitle()+i.getFirstText()+i.getLastText()\
               +i.getFirstOCR+i.getLastOCR()+i.getStickerOCR()

        i.setIsAd(model.predict(test))
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
