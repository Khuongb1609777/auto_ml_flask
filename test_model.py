import numpy as np
from numpy.core.fromnumeric import argmax
from numpy.core.numeric import full
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from numpy.linalg import matrix_rank
import math

from sklearn.utils import shuffle

dataset = pd.read_csv("./data_api/data_pre_3012.csv")
dataset["BMI"] = dataset["weight"] / (dataset["height"] * dataset["height"])

class_values = []
for i in range(len(dataset)):
    if (dataset["BMI"][i]) < 18.5:
        class_values.append(0)
    elif (dataset["BMI"][i]) >= 18.5 and (dataset["BMI"][i]) < 23:
        class_values.append(1)
    elif (dataset["BMI"][i] >= 23) and (dataset["BMI"][i]) < 25:
        class_values.append(2)
    elif (dataset["BMI"][i]) >= 25 and (dataset["BMI"][i]) < 30:
        class_values.append(3)
    elif (dataset["BMI"][i] >= 30) and (dataset["BMI"][i]) < 40:
        class_values.append(4)
    else:
        class_values.append(5)

dataset["obesity"] = class_values


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
            / np.sum([((w[v] * class_counts[v])) for v in range(len(class_counts))])
        )
    )
    return entropy_value


#   Create function information gain---------------------------------------
def calculate_information_gain(dataset, feature, label, w):
    # Calculate the dataset entropy
dataset_entropy = calculate_entropy(dataset_temp[label], w)
values, feat_counts = np.unique(dataset_temp['dinner_of_the_week'], return_counts=True)
# Calculate the weighted feature entropy
# Call the calculate_entropy function
weighted_feature_entropy = np.sum(
    [
        (feat_counts[i] / np.sum(feat_counts))
        * calculate_entropy_node(
            dataset_temp.where(dataset_temp['dinner_of_the_week'] ==  values[1]).dropna()[label], w
        )
        for i in range(len(values))
    ]
)
    feature_info_gain = dataset_entropy - weighted_feature_entropy
    return feature_info_gain


# create decision tree ---------------------------------------------------------
def create_decision_tree(dataset, df, features, label, parent, w):
data_t = np.unique(dataset_temp[label], return_counts=True)
unique_data = np.unique(dataset_temp[label])
parent = unique_data[np.argmax(data_t[1])]
item_values = [
    calculate_information_gain(dataset_temp, feature, label, w)
    for feature in features1
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
        decision_tree = decision_tree[nodes][value]
        prediction = 0
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
for i in range(5 - 1):
    j = i + 1
    for j in range(j, 5):
        dataset_i = dataset1[dataset1[label] == i]
        dataset_j = dataset1[dataset1[label] == j]
        dataset_temp = pd.DataFrame(pd.concat([dataset_i, dataset_j]))
        nm_ij = np.matrix(
            [
                [cm_matrix[i, i], cm_matrix[i, j]],
                [cm_matrix[j, i], cm_matrix[j, j]],
            ]
        )
cm_i = np.sum(nm_ij[0, l] for l in range(len(nm_ij)))
cm_j = np.sum(nm_ij[1, m] for m in range(len(nm_ij)))
N = len(dataset1)
N_i = len(dataset_temp.where(dataset_temp[label] == i).dropna())
N_j = len(dataset_temp.where(dataset_temp[label] == j).dropna())
w_i = cm_i * (N / ((cm_i * N_i) + (cm_j * N_j)))
w_j = cm_j * (N / ((cm_i * N_i) + (cm_j * N_j)))
w = [w_i, w_j]
tree = create_decision_tree(
    dataset_temp, dataset_temp, features1, label, parent, w
)
        list_tree.append(tree)
    return list_tree


#   Chuẩn bị dữ liệu chạy mô hình kịch bản 1 sử dụng các thuộc tính về bữa ăn - nước uống (về dinh dưỡng) ----------------------------------------------
features_script1 = [
    "meal_of_the_day",
    "breakfast_of_the_day",
    "dinner_of_the_week",
    "fast_food_of_the_week",
    "vegetable_in_meal",
    "source_of_food",
    "water_of_the_day",
    "protein_of_meal",
    "alcohol",
    "soda_water",
]
features_script1_index = [7, 8, 9, 10, 11, 12, 13, 14, 17, 18]


#   Chuẩn bị dữ liệu chạy mô hình kịch bản 2 sử dụng các thuộc tính về hoạt động thể chất-----------------------------------
features_script2 = [
    "time_do_exercise",
    "time_of_sport",
    "require_of_job",
    "transport",
    "park",
]
features_script2_index = [15, 16, 24, 26, 27]


#   Chuẩn bị dữ liệu chạy mô hình kịch bản 3 sử dụng các thuộc tính về thói quen sinh hoạt - tình trạng sức khỏe -----------------------------------
features_script3 = [
    "nicotine",
    "sleep_time",
    "chronic_diseases",
    "chronic_diseases_medicine",
    "chronic_diseases_relatives",
    "time_use_tech_equip",
    "sedative",
    "depression",
]
features_script3_index = [19, 20, 21, 22, 23, 28, 29, 30]


#   Chuẩn bị dữ liệu chạy mô hình kịch bản 4 sử dụng các thuộc tính kết hợp -----------------------------------
features_full = features_script1 + features_script2 + features_script3
features_full_index = (
    features_script1_index + features_script2_index + features_script3_index
)

label = "nobesity"
label_index = 33

X_script1 = dataset.iloc[:, features_script1_index]
X_script2 = dataset.iloc[:, features_script2_index]
X_script3 = dataset.iloc[:, features_script3_index]
X_script_full = dataset.iloc[:, features_full_index]

y = dataset[label]

import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split

X_train1, X_test1, y_train1, y_test1 = train_test_split(
    X_script1, y, stratify=y, shuffle=True, test_size=0.33
)
X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X_script2, y, stratify=y, shuffle=True, test_size=0.33
)
X_train3, X_test3, y_train3, y_test3 = train_test_split(
    X_script3, y, stratify=y, shuffle=True, test_size=0.33
)
X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(
    X_script_full, y, stratify=y, shuffle=True, test_size=0.33
)


####-----------------------------MODEL 1 DATASET1 --------------------------------#####

dataset1 = X_train1
dataset1["nobesity"] = list(y_train1)
dataset1 = dataset1.reset_index(drop = True)

k1 = dataset1.shape[1]
value_counts1 = dataset1[label].value_counts()
full_columns_name1 = dataset1.columns
# Find target min_count values
label_min1 = list(value_counts1[value_counts1 == (value_counts1.min())].index)[0]
# Find target max_count values
label_max1 = list(value_counts1[value_counts1 == (value_counts1.max())].index)[0]
cm_matrix, cv_ = create_random_cm_matrix(9, len(value_counts1), label_min1, label_max1)
features1 = list(full_columns_name1.drop(label))
parent = None
dts = create_model(5, dataset1, cm_matrix, label, features1, parent)


####-----------------------------MODEL 2 --------------------------------#####


dataset2 = X_train2
dataset2["nobesity"] = list(y_train2)


####-----------------------------MODEL 3 --------------------------------#####


dataset3 = X_train3
dataset3["nobesity"] = list(y_train3)


####-----------------------------MODEL FULL --------------------------------#####


dataset_full = X_train_full
dataset_full["nobesity"] = list(y_train_full)


k = dataset.shape[1]
value_counts = dataset["tk"].value_counts()
full_columns_name = dataset.columns
# Find target min_count values
label_min = list(value_counts[value_counts == (value_counts.min())].index)[0]
# Find target max_count values
label_max = list(value_counts[value_counts == (value_counts.max())].index)[0]
cm_matrix, cv_ = create_random_cm_matrix(9, 5, label_min, label_max)
label = "tk"
features = list(full_columns_name.drop("tk"))
parent = None


dts = create_model(class_num, dataset, cm_matrix, label, features, parent)


import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

X = dataset.drop(["CLASS"])
y = dataset["CLASS"]
sss = StratifiedShuffleSplit(n_splits=5, test_size=0.5, random_state=0)
sss.get_n_splits(X, y)


# a = predict(X_test.iloc[0,:],dt)