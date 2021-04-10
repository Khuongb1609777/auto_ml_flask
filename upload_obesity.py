from os import path
from data import DATA
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
from function_api import API

# dataset = pd.read_csv("./data_api/data_pre_1.csv")
dataset = pd.read_csv("./data/data_obesity_preprocessing_not_encode.csv")

for i in range(len(dataset)):
    data_post = {
        "gender": float(dataset["Gender"][i]),
        "age": float(dataset["Age"][i]),
        "height": float(dataset["Height"][i]),
        "weight": float(dataset["Weight"][i]),
        "FHWO": float(dataset["family_history_with_overweight"][i]),
        "FAVC": float(dataset["FAVC"][i]),
        "FCVC": float(dataset["FCVC"][i]),
        "NCP": float(dataset["NCP"][i]),
        "CAEC": float(dataset["CAEC"][i]),
        "SMOKE": float(dataset["SMOKE"][i]),
        "CH2O": float(dataset["CH2O"][i]),
        "SCC": float(dataset["SCC"][i]),
        "FAF": float(dataset["FAF"][i]),
        "TUE": float(dataset["TUE"][i]),
        "CALC": float(dataset["CALC"][i]),
        "MTRANS": float(dataset["MTRANS"][i]),
        "NObeyesdad": float(dataset["NObeyesdad"][i]),
    }
    class_name = "DatasetObesity"
    data = API.post(class_name, data_post)