from sklearn import svm, metrics
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import joblib
import pickle
import re
from DataMiningService import tokenizer, token2vec

#data load
dwn_url = "/Users/smwu/Desktop/data_set.csv"
data = pd.read_csv(dwn_url, error_bad_lines=False, encoding='utf-8', header=0)
print("총 샘플 수 : ", len(data))

data['class'] = data['class'].replace(['none', 'ad'], [0, 1])
data.drop_duplicates(subset='문장', inplace=True)

#data x,y로 나누기
x = data['문장']
y = data['class']
print('text 수:', len(x))
print('class 수: ', len(y))

#D.train, D.test로 나누기
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

#x데이터 토큰화
model_train = token2vec(tokenizer(x_train))
model_test = token2vec(tokenizer(x_test))

#모델
svm=svm.SVC()
svm.fit(model_train, y_train)

#결과
result = svm.predict(model_test)
print(metrics.accuracy_score(y_test, result))

#최적화
pipe_svc = make_pipeline(StandardScaler(), svm.SVC())
param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
param_grid = [
    {'svc__C': param_range, 'svc__kernel': ['linear']},
    {'svc__C': param_range, 'svc__gamma': param_range, 'svc__kernel': ['rbf']},
]
gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring='accuracy', cv=10, n_jobs=2)
gs = gs.fit(model_train, y_train)

#최적화 결과
result = gs.predict(model_test)
print(metrics.accuracy_score(y_test, result))

#학습된 모델 저장
joblib.dump(gs, './svm_vest.pkl')

