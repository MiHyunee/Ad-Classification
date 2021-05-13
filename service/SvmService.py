from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

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


