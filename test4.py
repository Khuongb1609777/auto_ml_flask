from os import path
from data import DATA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
from function_api import API

# dataset = pd.read_csv("./data_api/data_pre_1.csv")
dataset = pd.read_csv("./data_api/ObesityDataSet_raw_and_data_sinthetic.csv")

for i in range(len(dataset)):
    data_post = {
        "gender": str(dataset["Gender"][i]),
        "age": float(dataset["Age"][i]),
        "height": float(dataset["Height"][i]),
        "weight": float(dataset["Weight"][i]),
        "FHWO": str(dataset["family_history_with_overweight"][i]),
        "FAVC": str(dataset["FAVC"][i]),
        "FCVC": float(dataset["FCVC"][i]),
        "NCP": float(dataset["NCP"][i]),
        "CAEC": str(dataset["CAEC"][i]),
        "SMOKE": str(dataset["SMOKE"][i]),
        "CH2O": float(dataset["CH2O"][i]),
        "SCC": str(dataset["SCC"][i]),
        "FAF": float(dataset["FAF"][i]),
        "TUE": float(dataset["TUE"][i]),
        "CALC": str(dataset["CALC"][i]),
        "MTRANS": str(dataset["MTRANS"][i]),
        "NObeyesdad": str(dataset["NObeyesdad"][i]),
    }
    class_name = "DatasetObesityRaw"
    data = API.post(class_name, data_post)