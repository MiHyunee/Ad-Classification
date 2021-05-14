from sklearn import svm, metrics
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import joblib
import pickle
import re
from tensorflow.keras.preprocessing.sequence import pad_sequences


def svmTraining(x_sequence, y_data):

    #D.tr:D.test = 8:2
    n_of_train = int(len(x_sequence) * 0.8)
    n_of_test = int(len(x_sequence) - n_of_train)
    print('훈련 데이터의 개수 :', n_of_train)
    print('테스트 데이터의 개수:', n_of_test)

    max_len = max(len(l) for l in x_sequence)
    x_data = pad_sequences(x_sequence, maxlen=max_len)

    #X_D.train X_D.test로 나누기
    x_test = x_data[n_of_train:]  # X_data 데이터 중에서 뒤의 1034개의 데이터만 저장
    y_test = np.array(y_data[n_of_train:])  # y_data 데이터 중에서 뒤의 1034개의 데이터만 저장
    x_train = x_data[:n_of_train]  # X_data 데이터 중에서 앞의 4135개의 데이터만 저장
    y_train = np.array(y_data[:n_of_train])  # y_data 데이터 중에서 앞의 4135개의 데이터만 저장
    print("훈련용 이메일 데이터의 크기(shape): ", x_train.shape)
    print("테스트용 이메일 데이터의 크기(shape): ", x_test.shape)
    print("훈련용 레이블의 크기(shape): ", y_train.shape)
    print("테스트용 레이블의 크기(shape): ", y_test.shape)

    #모델
    svm_model = svm.SVC()
    svm_model.fit(x_train, y_train)

    #결과
    result = svm_model.predict(x_test)
    print("Test Accuracy: ", metrics.accuracy_score(y_test, result))

    #최적화
    pipe_svc = make_pipeline(StandardScaler(), svm.SVC())
    param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    param_grid = [
        {'svc__C': param_range, 'svc__kernel': ['linear']},
        {'svc__C': param_range, 'svc__gamma': param_range, 'svc__kernel': ['rbf']},
    ]
    gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring='accuracy', cv=10, n_jobs=2)
    gs = gs.fit(x_train, y_train)

    #최적화 결과
    result = gs.predict(x_test)
    print("Test accuracy after Optimization:" , metrics.accuracy_score(y_test, result))

    #학습된 모델 저장
    #joblib.dump(gs, './svm_vest.pkl')

