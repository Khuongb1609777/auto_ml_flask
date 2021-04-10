from os import path
from data import DATA
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
from function_api import API

dataset = pd.read_csv("./data/data_balance_chart.csv")
dataset = dataset.sort_values(by ='obesity')
dataset = dataset.reset_index(drop = True)
dataset_no = pd.read_csv("./data/data_chart.csv")
dataset_no = dataset_no.sort_values(by ='obesity')
dataset_no = dataset_no.reset_index(drop = True)


# plot.plot(dataset_no.iloc[0:216, 0], dataset_no.iloc[0:216,1], 'bo')
# plot.plot(dataset_no.iloc[216:543, 0], dataset_no.iloc[216:543,1], 'rx')
# plot.plot(dataset_no.iloc[543:629, 0], dataset_no.iloc[543:629,1], 'go')
# plot.plot(dataset_no.iloc[629:684, 0], dataset_no.iloc[629:684,1], 'ro')
# plot.plot(dataset_no.iloc[684:, 0], dataset_no.iloc[684:,1], 'bx')


plot.plot(dataset.iloc[0:324, 0], dataset.iloc[0:324,1], 'bo')
plot.plot(dataset.iloc[324:647, 0], dataset.iloc[324:647,1], 'rx')
plot.plot(dataset.iloc[647:972, 0], dataset.iloc[647:972,1], 'go')
plot.plot(dataset.iloc[972:1296, 0], dataset.iloc[972:1296,1], 'ro')
plot.plot(dataset.iloc[1296:, 0], dataset.iloc[1296:,1], 'bx')


plot.show()

