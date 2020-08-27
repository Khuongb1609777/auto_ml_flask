from os import path
from data import DATA

dataFrame = DATA.read("csv", "./download_temp/data.csv")
col_feature = [3, 4, 5]
cols_temp = list(dataFrame.columns[col_feature])
for i in range(len(cols_temp)):
    print(cols_temp[i])
    a = dataFrame.cols_temp[i]
    dataFrame = dataFrame.drop(
        dataFrame[(dataFrame.loc[:, i] == "")].index)

for i in col_feature:
    dataFrame = dataFrame.drop(
        dataFrame[(dataFrame.iloc[:, i] == "")].index)
