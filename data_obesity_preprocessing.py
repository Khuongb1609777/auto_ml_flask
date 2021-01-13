from os import path
from data import DATA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
from function_api import API
import random
import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix

dataset = pd.read_csv("./data/ObesityDataSet_raw_and_data_sinthetic.csv")

#  #   Column                          Non-Null Count  Dtype
# ---  ------                          --------------  -----
#  0   Gender                          2111 non-null   object
#  1   Age                             2111 non-null   float64
#  2   Height                          2111 non-null   float64
#  3   Weight                          2111 non-null   float64
#  4   family_history_with_overweight  2111 non-null   object
#  5   FAVC                            2111 non-null   object   Frequent consumption of high caloric food Thường xuyên tiêu thụ thực phẩm giàu calo
#  6   FCVC                            2111 non-null   float64
#  7   NCP                             2111 non-null   float64
#  8   CAEC                            2111 non-null   object
#  9   SMOKE                           2111 non-null   object
#  10  CH2O                            2111 non-null   float64
#  11  SCC                             2111 non-null   object
#  12  FAF                             2111 non-null   float64
#  13  TUE                             2111 non-null   float64
#  14  CALC                            2111 non-null   object
#  15  MTRANS                          2111 non-null   object
#  16  NObeyesdad                      2111 non-null   object

#   Ham chuyen doi du lieu co thu tu
def transform_encoder_level(dataset, feature_name, feature_values, feture_values_level):
    for i in range(len(dataset)):
        for j in range(len(feature_values)):
            if dataset[feature_name][i] == feature_values[j]:
                dataset[feature_name][i] = int(feture_values_level[j])
    return dataset


gender_values = ["Female", "Male"]
gender_values_preprocessing = [0, 1]

dataset = transform_encoder_level(
    dataset,
    "Gender",
    gender_values,
    gender_values_preprocessing,
)


family_history_with_overweight_values = ["yes", "no"]
family_history_with_overweight_values_pre = [1, 0]
dataset = transform_encoder_level(
    dataset,
    "family_history_with_overweight",
    family_history_with_overweight_values,
    family_history_with_overweight_values_pre,
)

dataset = transform_encoder_level(
    dataset,
    "FAVC",
    ["yes", "no"],
    [1, 0],
)

dataset = transform_encoder_level(
    dataset,
    "CAEC",
    ["no", "Sometimes", "Frequently", "Always"],
    [0, 1, 2, 3],
)

dataset = transform_encoder_level(
    dataset,
    "SMOKE",
    ["no", "yes"],
    [0, 1],
)

dataset = transform_encoder_level(
    dataset,
    "SCC",
    ["no", "yes"],
    [0, 1],
)

dataset = transform_encoder_level(
    dataset,
    "CALC",
    ["no", "Sometimes", "Frequently", "Always"],
    [0, 1, 2, 3],
)

dataset = transform_encoder_level(
    dataset,
    "CALC",
    ["no", "Sometimes", "Frequently", "Always"],
    [0, 1, 2, 3],
)

dataset = transform_encoder_level(
    dataset,
    "MTRANS",
    ["Public_Transportation", "Automobile", "Walking", "Motorbike", "Bike"],
    [0, 1, 2, 3, 4],
)

dataset = transform_encoder_level(
    dataset,
    "NObeyesdad",
    [
        "Obesity_Type_I",
        "Obesity_Type_III",
        "Obesity_Type_II",
        "Overweight_Level_II",
        "Overweight_Level_I",
        "Normal_Weight",
        "Insufficient_Weight",
    ],
    [4, 6, 5, 3, 2, 1, 0],
)

# dataset['CH2O'] = dataset['CH2O']*10
# dataset = dataset[(dataset.CH2O) % 10 == 0]

# dataset['NCP'] = dataset['NCP']*10
# dataset = dataset[(dataset.NCP) % 10 == 0]

# dataset["Age"] = dataset["Age"] * 10
# dataset = dataset[(dataset.Age) % 10 == 0]
# dataset["Age"] = dataset["Age"] / 10
# dataset = dataset.reset_index(drop=True)

# age_list = []

# for i in range(len(dataset)):
#     if dataset["Age"][i] < 20:
#         age_list.append(0)
#     elif dataset["Age"][i] >= 20 and dataset["Age"][i] < 30:
#         age_list.append(1)
#     elif dataset["Age"][i] >= 30 and dataset["Age"][i] < 40:
#         age_list.append(2)
#     elif dataset["Age"][i] >= 40 and dataset["Age"][i] < 50:
#         age_list.append(3)
#     elif dataset["Age"][i] >= 50 and dataset["Age"][i] < 60:
#         age_list.append(4)
#     elif dataset["Age"][i] > 60:
#         age_list.append(5)

# dataset["Age"] = age_list

# height_list = []
# for i in range(len(dataset)):
#     if dataset["Height"][i] < 1.5:
#         height_list.append(0)
#     elif dataset["Height"][i] >= 1.5 and dataset["Height"][i] < 1.55:
#         height_list.append(1)
#     elif dataset["Height"][i] >= 1.55 and dataset["Height"][i] < 1.6:
#         height_list.append(2)
#     elif dataset["Height"][i] >= 1.6 and dataset["Height"][i] < 1.65:
#         height_list.append(3)
#     elif dataset["Height"][i] >= 1.65 and dataset["Height"][i] < 1.7:
#         height_list.append(4)
#     elif dataset["Height"][i] >= 1.7 and dataset["Height"][i] < 1.75:
#         height_list.append(5)
#     elif dataset["Height"][i] >= 1.75 and dataset["Height"][i] < 1.8:
#         height_list.append(6)
#     elif dataset["Height"][i] >= 1.8 and dataset["Height"][i] < 1.85:
#         height_list.append(7)
#     elif dataset["Height"][i] >= 1.85 and dataset["Height"][i] < 1.9:
#         height_list.append(8)
#     elif dataset["Height"][i] >= 1.9:
#         height_list.append(9)

# dataset["Height"] = height_list


# Weight_list = []
# for i in range(len(dataset)):
#     if dataset["Weight"][i] < 45:
#         Weight_list.append(0)
#     elif dataset["Weight"][i] >= 45 and dataset["Weight"][i] < 50:
#         Weight_list.append(1)
#     elif dataset["Weight"][i] >= 50 and dataset["Weight"][i] < 55:
#         Weight_list.append(2)
#     elif dataset["Weight"][i] >= 55 and dataset["Weight"][i] < 60:
#         Weight_list.append(3)
#     elif dataset["Weight"][i] >= 60 and dataset["Weight"][i] < 65:
#         Weight_list.append(4)
#     elif dataset["Weight"][i] >= 65 and dataset["Weight"][i] < 70:
#         Weight_list.append(5)
#     elif dataset["Weight"][i] >= 70 and dataset["Weight"][i] < 75:
#         Weight_list.append(6)
#     elif dataset["Weight"][i] >= 75 and dataset["Weight"][i] < 80:
#         Weight_list.append(7)
#     elif dataset["Weight"][i] >= 80 and dataset["Weight"][i] < 85:
#         Weight_list.append(8)
#     elif dataset["Weight"][i] >= 85 and dataset["Weight"][i] < 90:
#         Weight_list.append(9)
#     elif dataset["Weight"][i] >= 90:
#         Weight_list.append(10)


# dataset["Weight"] = Weight_list

# for i in range(len(dataset)):
#     for fea in list(dataset.columns):
#         dataset[fea][i] = int(round(dataset[fea][i]))


# dataset = dataset[(dataset.NCP) % 10 == 0]

export_csv = dataset.to_csv(
    r"C:\Users\KHUONG\Desktop\luanvan\auto_ml_flask\data\data_obesity_preprocessing_not_endcode.csv",
    index=None,
    header=True,
)

import numpy as np
from numpy.core.fromnumeric import argmax
from numpy.core.numeric import full
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from numpy.linalg import matrix_rank
import math

from sklearn.utils import shuffle

# dataset = pd.read_csv("./data_api/data_obesity_before.csv")
# dataset["BMI"] = dataset["weight"] / (dataset["height"] * dataset["height"])

# class_values = []
# for i in range(len(dataset)):
#     if (dataset["BMI"][i]) < 18.5:
#         class_values.append(0)
#     elif (dataset["BMI"][i]) >= 18.5 and (dataset["BMI"][i]) < 23:
#         class_values.append(1)
#     elif (dataset["BMI"][i] >= 23) and (dataset["BMI"][i]) < 25:
#         class_values.append(2)
#     elif (dataset["BMI"][i]) >= 25 and (dataset["BMI"][i]) < 30:
#         class_values.append(3)
#     elif (dataset["BMI"][i] >= 30) and (dataset["BMI"][i]) < 40:
#         class_values.append(4)
#     else:
#         class_values.append(5)

# dataset["nobesity"] = class_values


# def transform_encoder(feature_name, array_feature):
#     le = preprocessing.LabelEncoder()
#     le.fit(array_feature)
#     dataset[feature_name] = le.transform(dataset[feature_name])
#     return dataset


# dataset = transform_encoder("tk", value_counts_for_decode.index)

#   --------------------------------------------------------------Khởi tạo hàm -------------------------------------------------------------


#   --------------------DECISION TREE ------------------------------------


#   Create calculate_entropy function-------------------------------------
def calculate_entropy(df_label, w):
    classes, class_counts = np.unique(df_label, return_counts=True)
    entropy_value = 0
    for i in range(len(classes)):
        entropy_value = entropy_value + (
            -(w[i] / (w[0] + w[1])) * np.log2(w[i] / (w[0] + w[1]))
        )
    return entropy_value


#   Calculate_entropy t node-----------------------------------------------
def calculate_entropy_node(df_label, w):
    classes, class_counts = np.unique(df_label, return_counts=True)
    entropy_value = 0
    for i in range(len(classes)):
        entropy_value = entropy_value + (
            -(
                (class_counts[i] * w[i])
                / np.sum([((w[v] * class_counts[v])) for v in range(len(class_counts))])
            )
            * np.log2(
                (class_counts[i] * w[i])
                / np.sum([((w[k] * class_counts[k])) for k in range(len(class_counts))])
            )
        )
        # print(entropy_value)
    return entropy_value


#   Create function information gain---------------------------------------
def calculate_information_gain(dataset, feature, label, w):
    # Calculate the dataset entropy
    dataset_entropy = calculate_entropy(dataset[label], w)
    values, feat_counts = np.unique(dataset[feature], return_counts=True)
    # Calculate the weighted feature entropy
    # Call the calculate_entropy function
    weighted_feature_entropy = np.sum(
        [
            (feat_counts[i] / np.sum(feat_counts))
            * calculate_entropy_node(
                dataset.where(dataset[feature] == values[i]).dropna()[label], w
            )
            for i in range(len(values))
        ]
    )
    feature_info_gain = dataset_entropy - weighted_feature_entropy
    return feature_info_gain


# create decision tree ---------------------------------------------------------
def create_decision_tree(dataset, df, features, label, parent, w):
    data_t = np.unique(df[label], return_counts=True)
    unique_data = np.unique(dataset[label])
    if len(unique_data) <= 1:
        return unique_data[0]
    elif (len(dataset)) == 0:
        return unique_data[np.argmax[data_t[1]]]
    elif len(features) == 0:
        return parent
    else:
        parent = unique_data[np.argmax(data_t[1])]
        item_values = [
            calculate_information_gain(dataset, feature, label, w)
            for feature in features
        ]
        optimum_feature_index = np.argmax(item_values)
        optimum_feature = features[optimum_feature_index]
        decision_tree = {optimum_feature: {}}
        features = [i for i in features if i != optimum_feature]
        for value in np.unique(dataset[optimum_feature]):
            min_data = dataset.where(dataset[optimum_feature] == value).dropna()
            min_tree = create_decision_tree(min_data, df, features, label, parent, w)
            decision_tree[optimum_feature][value] = min_tree
        return decision_tree


#   Create function predict form data and tree---------------------------------------------
def predict(test_data, decision_tree):
    for nodes in list(decision_tree.keys()):
        value = test_data[nodes]
        try:
            decision_tree = decision_tree[nodes][value]
            prediction = 0
        except:
            return float(random.randint(4, 6))
        if type(decision_tree) is dict:
            prediction = predict(test_data, decision_tree)
        else:
            prediction = decision_tree
            break
    return prediction


# ------------------------------------------COST SENSITIVE----------------------------------

# find cm[x][y] x,y != min, max DK 1: One 1 ------------------------------------------------
def create_cm1(k, label_min, label_max):
    x_random = np.random.randint(k)
    y_random = np.random.randint(k)
    if ((x_random, y_random) == (label_min, label_max)) or (
        (x_random, y_random) == (label_max, label_min)
    ):
        (x_random, y_random) = create_cm1(k, label_min, label_max)
        return (x_random, y_random)
    else:
        return (x_random, y_random)


#   Create Cost_sensitive matrix------------------------------------------------------------
def create_random_cm_matrix(n, k_input, label_min, label_max):
    vector_cv = []
    for i in range(k_input):
        vector_cv.append(np.random.randint(n))
    matrix = np.random.randint(n + 1, size=(k_input, k_input))
    (x, y) = create_cm1(k_input, label_min, label_max)
    matrix[x, y] = 1  #   DDK1: One 1
    # return(matrix)
    if matrix.max() < n:
        # Cost for cm(min,max) = max
        matrix[label_min, label_max] = matrix.max() + 1
    else:
        # Cost for cm(min,max) = max
        matrix[label_min, label_max] = matrix.max()
    if matrix.min() > 0:
        matrix[label_max, label_min] = 0  # Cost for cm(max,min) = min DK3
    else:
        # Cost for cm(max,min) = min DK3
        matrix[label_max, label_min] = matrix.min()
    # print(np.linalg.matrix_rank(matrix))
    if np.linalg.matrix_rank(matrix) != k_input:
        matrix = create_random_cm_matrix(n, k_input, label_min, label_max)
    else:
        return (matrix, vector_cv)


#   Create n(n-1)/2 model decision tree-----------------------------------------------------
def create_model(class_num, dataset, cost_matrix, label, features, parent):
    list_tree = []
    i = 0
    for i in range(class_num - 1):
        j = i + 1
        for j in range(j, class_num):
            dataset_i = dataset[dataset[label] == i]
            dataset_j = dataset[dataset[label] == j]
            dataset_temp = pd.DataFrame(pd.concat([dataset_i, dataset_j])).reset_index(
                drop=True
            )
            nm_ij = np.matrix(
                [
                    [cost_matrix[i, i], cost_matrix[i, j]],
                    [cost_matrix[j, i], cost_matrix[j, j]],
                ]
            )
            # print(nm_ij)
            cm_i = np.sum(nm_ij[0, l] for l in range(len(nm_ij)))
            cm_j = np.sum(nm_ij[1, m] for m in range(len(nm_ij)))
            N = len(dataset)
            N_i = int(dataset[label].value_counts()[i])
            N_j = int(dataset[label].value_counts()[j])
            # print(N_i)
            w_i = cm_i * (N / ((cm_i * N_i) + (cm_j * N_j)))
            w_j = cm_j * (N / ((cm_i * N_i) + (cm_j * N_j)))
            w = [w_i, w_j]
            tree = create_decision_tree(
                dataset_temp, dataset_temp, features, label, parent, w
            )
            list_tree.append(tree)
    return list_tree


X = dataset.iloc[:, :16]
y = dataset["NObeyesdad"]
label = "NObeyesdad"

X_train1, X_test1, y_train1, y_test1 = train_test_split(
    X, y, stratify=y, shuffle=True, test_size=0.33
)

dataset1 = X_train1
dataset1["NObeyesdad"] = list(y_train1)
dataset1 = dataset1.reset_index(drop=True)

cm_matrix, cv_ = create_random_cm_matrix(9, 7, 6, 0)

k1 = dataset1.shape[1]

value_counts1 = dataset1[label].value_counts()
full_columns_name1 = dataset1.columns
# Find target min_count values
label_min1 = list(value_counts1[value_counts1 == (value_counts1.min())].index)[0]
# Find target max_count values
label_max1 = list(value_counts1[value_counts1 == (value_counts1.max())].index)[0]
features1 = list(full_columns_name1.drop(label))
parent = None
cost_decision_tree_1 = create_model(7, dataset1, cm_matrix, label, features1, parent)

###---------------------TEST MODEL  cost_decision_tree_full-------------------------------###
def cost_test(X_test, cost_tree):
    predicts = []
    for i in range(len(X_test)):
        predict_temp = []
        for j in range(3):
            predict_temp.append(predict(pd.Series(X_test.iloc[i, :]), cost_tree[j]))
        predicts.append(max(set(predict_temp), key=predict_temp.count))
    return predicts


###-----------TEST MODEL 1  cost_decision_tree_1-------------###
X_test1 = X_test1.reset_index(drop=True)
predicts_1 = cost_test(X_test1, cost_decision_tree_1)

from sklearn.metrics import accuracy_score

accuracy_score(list(predicts_1), list(y_test1))
