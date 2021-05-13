from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import joblib
import pickle

#data load
data_set = pd.read_excel("/Users/smwu/Desktop/data_set.xlsx")

#행, 열 추출 방법1
#x1 = data_set.iloc[:, 0]
#y1 = data_set.iloc[:, 1]

#행, 열 추출 방법2
data = data_set.to_numpy() #pandas객체를 numpy화
x=[]
y=[]
for index, d in enumerate(data):
    x.append(d[0])
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
gamma_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
acc = 0
for index,gamma_data in enumerate(gamma_list): # enumerate를 사용한 이유는 enumerate에 익숙해지기 위하여
    # 소수점 테스트
    svm = svm.SVC(C=1,gamma=gamma_data)
    svm.fit(model_train,y_train)
    result=svm.predict(model_test)
    score = metrics.accuracy_score(y_test, result)
    if acc < score:
        acc = score
        svm_best = svm
    # 정수 테스트
    svm = svm.SVC(C=1,gamma=gamma_data*10)
    svm.fit(model_train,y_train)
    result = svm.predict(model_test)
    score = metrics.accuracy_score(y_test, result)
    if acc < score:
        acc = score
        svm_best = svm

#최적화 결과
result = svm_best.predict(model_test) #model_test는 벡터화된 x_test
print(metrics.accuracy_score(y_test, result))

#학습된 모델 저장
joblib.dump(svm_best, './svm_vest.pkl')
