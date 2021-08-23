import joblib
import numpy as np
import pandas as pd
import pickle
import re
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from service.SourceService import SourceService
from service.OcrService import OcrService


class SvmService:

    def __init__(self):
        global okt
        okt = Okt()
        self.__ocr = OcrService()

    def rxSvm(self, i):
        # model load
        model = joblib.load('static/svm_model.pkl')

        SourceService.rxCrawling(i)
        predict = []

        lastText = [i.getLastText()]
        isAd = model.predict(lastText)
        if isAd == 1:
            print("lastText: ", lastText)
            i.setIsAd(isAd)
            predict.append("Ad")
            print(i.getTitle(), " : ", isAd)
            return predict

        self.__ocr.ocr_sticker(i)
        stickerOcr = [i.getStickerOCR()]
        isAd = model.predict(stickerOcr)
        if isAd == 1:
            print("sticker: ", stickerOcr)
            i.setIsAd(isAd)
            predict.append("Ad")
            print(i.getTitle(), " : ", isAd)
            return predict

        self.__ocr.ocr_lastImg(i)
        lastOcr = [i.getLastOCR()]
        isAd = model.predict(lastOcr)
        if isAd == 1:
            print("lastOcr: ", lastOcr)
            i.setIsAd(isAd)
            predict.append("Ad")
            print(i.getTitle(), " : ", isAd)
            return predict

        lastOcrbw = [i.getLastOCRbw()]
        isAd = model.predict(lastOcrbw)
        if isAd == 1:
            print("lastOcrbw: ", lastOcrbw)
            i.setIsAd(isAd)
            predict.append("Ad")
            print(i.getTitle(), " : ", isAd)
            return predict

        title = [i.getTitle()]
        isAd = model.predict(title)
        if isAd == 1:
            print("title: ", title)
            i.setIsAd(isAd)
            predict.append("Ad")
            print(i.getTitle(), " : ", isAd)
            return predict

        firstText = [i.getFirstText()]
        isAd = model.predict(firstText)
        if isAd == 1:
            print("firstText: ", firstText)
            i.setIsAd(isAd)
            predict.append("Ad")
            print(i.getTitle(), " : ", isAd)
            return predict

        i.setIsAd(isAd)  # 광고아님
        predict.append("Review")

        return predict

    def _tokenizer(self, x_data):
        dictionary = {}
        text_results = []

        token = okt.pos(x_data, norm=True, stem=True)
        word = []
        for w in token:
            if not w[1] in ["Josa", "Eomi", "Punctuation"]:
                if len(w[0]) > 1:
                    word.append(w[0])
                if w[0] not in dictionary:
                    dictionary[w[0]] = 0
                dictionary[w[0]] += 1
            # rl = (" ".join(word)).strip()    #문장으로
        text_results.append(word)

        return [w for n in text_results for w in n]

    def svmTraining(self):

        down_url = "/Users/software/Downloads/dataSet.csv"
        data = pd.read_csv(down_url, error_bad_lines=False, encoding='utf-8', header=0)
        print("총 샘플 수 : ", len(data))

        data['class'] = data['class'].replace(['none', 'ad'], [0, 1])
        data.drop_duplicates(subset='문장', inplace=True)

        x_data = data['문장']
        y_data = data['class']

        # D.tr:D.test = 8:2
        n_of_train = int(len(x_data) * 0.8)
        n_of_test = int(len(x_data) - n_of_train)
        print('훈련 데이터의 개수 :', n_of_train)
        print('테스트 데이터의 개수:', n_of_test)

        # X_D.train X_D.test로 나누기
        x_test = x_data[n_of_train:]  # X_data 데이터 중에서 뒤의 1034개의 데이터만 저장
        y_test = np.array(y_data[n_of_train:])  # y_data 데이터 중에서 뒤의 1034개의 데이터만 저장
        x_train = x_data[:n_of_train]  # X_data 데이터 중에서 앞의 4135개의 데이터만 저장
        y_train = np.array(y_data[:n_of_train])  # y_data 데이터 중에서 앞의 4135개의 데이터만 저장
        print("훈련용 이메일 데이터의 크기(shape): ", x_train.shape)
        print("테스트용 이메일 데이터의 크기(shape): ", x_test.shape)
        print("훈련용 레이블의 크기(shape): ", y_train.shape)
        print("테스트용 레이블의 크기(shape): ", y_test.shape)

        # svm생성
        text_clf_svm = Pipeline([('vect', CountVectorizer(tokenizer=self._tokenizer)),
                                 ('tfidf', TfidfTransformer()),
                                 ('clf-svm', SGDClassifier(loss='hinge',
                                                           penalty='l2',
                                                           alpha=1e-3,
                                                           n_iter_no_change=5,
                                                           random_state=42))])
        text_clf_svm = text_clf_svm.fit(x_train, y_train)

        svm_predicted = text_clf_svm.predict(x_test)
        print(np.mean(svm_predicted == y_test))

        # 모델 저장
        joblib.dump(text_clf_svm, "static/svm_model.pkl")


