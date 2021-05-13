from sklearn import svm, metrics
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import joblib
import pickle
import re

#data load
data_set = pd.read_excel("/Users/smwu/Desktop/data_set.xlsx")
'''
#google drive spreadsheet load
url = "https://docs.google.com/spreadsheets/d/1CGp9VJsO5NSY57AJMM7wmYcfEZpL0lyn9srYlIQVbqo/view?usp=sharing"
file_id = url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?id=' + file_id
data_set = pd.read_excel(dwn_url)
'''
#행, 열 추출 방법1
#x1 = data_set.iloc[:, 0]
#y1 = data_set.iloc[:, 1]

#행, 열 추출 방법2
data = data_set.to_numpy() #pandas객체를 numpy화
x=[]
y=[]
for index, d in enumerate(data)
    p = re.compile("\W+")
    x.append(p.sub(" ",d[0]))
    y.append(d[1])

x=np.array(x)
y=np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

#모델
svm=svm.SVC()
svm.fit(model_train, y_train) #model_train은 벡터화된 x_train

#결과
result = svm.predict(model_test) #model_test는 벡터화된 x_test
print(metrics.accuracy_score(y_test, result))

#최적화
pipe_svc = make_pipeline(StandardScaler(), svm.SVC())
param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
param_grid = [
    {'svc__C' : param_range, 'svc__kernel':['linear']},
    {'svc__C' : param_range, 'svc__gamma':param_range, 'svc__kernel':['rbf']},
]
gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring='accuracy', cv=10, n_jobs=2)
gs = gs.fit(model_train, y_train)
#최적화 결과
result = gs.predict(model_test) #model_test는 벡터화된 x_test
print(metrics.accuracy_score(y_test, result))

#학습된 모델 저장
joblib.dump(svm_best, './svm_vest.pkl')
