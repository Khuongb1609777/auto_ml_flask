# OVERSAMPLING CÂN BẰNG DỮ LIỆU---------------------
from imblearn.over_sampling import SMOTE
from os import path
from data import DATA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
from function_api import API

dataset = pd.read_csv("./data/data_end.csv")
sm = SMOTE(random_state=2,  k_neighbors=6)

dataset = dataset.drop_duplicates()
dataset = dataset.reset_index(drop = True)

dataset_temp = dataset[dataset['obesity']==1] #Tạo chuẩn dữ liệu cân bằng

dataset_cs_1 = dataset[dataset['obesity']==1] #Tạo dữ liệu cơ sở
dataset_imb = dataset[dataset['obesity'] != 1]#dữ liệu của các lớp theieur số

for i in list(dataset_imb['obesity'].value_counts().index):
    dataset_add = dataset_imb[dataset_imb['obesity'] == i]
    dataset_mer = pd.concat([dataset_temp,dataset_add])
    X = dataset_mer.iloc[:,0:16]
    y = dataset_mer['obesity']
    X_bl, y_bl = sm.fit_resample(X, y)
    data_handling = pd.concat([X_bl, y_bl], axis=1)
    data_after = data_handling[data_handling['obesity']==i]
    dataset_cs_1 = pd.concat([dataset_cs_1,data_after])

export_csv = dataset_cs_1.to_csv(
    r"C:\Users\KHUONG\Desktop\luanvan\auto_ml_flask\data\data_balance_chart.csv",
    index=None,
    header=True,
)
