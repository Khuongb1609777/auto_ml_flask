import numpy as np
from numpy.core.fromnumeric import argmax
from numpy.core.numeric import full
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from numpy.linalg import matrix_rank
import math

from sklearn.utils import shuffle

dataset = pd.read_csv("./data_api/data_obesity_before.csv")
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
    for i in range(class_num - 1):
        j = i + 1
        for j in range(j, class_num):
            dataset_i = dataset[dataset[label] == i]
            dataset_j = dataset[dataset[label] == j]
            dataset_temp = pd.DataFrame(pd.concat([dataset_i, dataset_j]))
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
            N_i = len(dataset.where(dataset[label] == i).dropna())
            N_j = len(dataset.where(dataset[label] == j).dropna())
            w_i = cm_i * (N / ((cm_i * N_i) + (cm_j * N_j)))
            w_j = cm_j * (N / ((cm_i * N_i) + (cm_j * N_j)))
            w = [w_i, w_j]
            # print(w)
            tree = create_decision_tree(
                dataset_temp, dataset_temp, features, label, parent, w
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
X_script_full = dataset.iloc[
    :,
]

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


cm_matrix = np.matrix(
    [
        [0, 8, 3, 2, 1],
        [7, 0, 5, 1, 2],
        [8, 8, 0, 2, 3],
        [7, 9, 4, 0, 1],
        [9, 8, 3, 1, 0],
    ]
)

####-----------------------------MODEL 1 DATASET1 --------------------------------#####

dataset1 = X_train1
dataset1["nobesity"] = list(y_train1)
dataset1 = dataset1.reset_index(drop=True)

k1 = dataset1.shape[1]
value_counts1 = dataset1[label].value_counts()
full_columns_name1 = dataset1.columns
# Find target min_count values
label_min1 = list(value_counts1[value_counts1 == (value_counts1.min())].index)[0]
# Find target max_count values
label_max1 = list(value_counts1[value_counts1 == (value_counts1.max())].index)[0]
features1 = list(full_columns_name1.drop(label))
parent = None
cost_decision_tree_1 = create_model(5, dataset1, cm_matrix, label, features1, parent)


####-----------------------------MODEL 2 --------------------------------#####

dataset2 = X_train2
dataset2["nobesity"] = list(y_train2)
dataset2 = dataset2.reset_index(drop=True)

k2 = dataset2.shape[1]
value_counts2 = dataset2[label].value_counts()
full_columns_name2 = dataset2.columns
# Find target min_count values
label_min2 = list(value_counts2[value_counts2 == (value_counts2.min())].index)[0]
# Find target max_count values
label_max2 = list(value_counts2[value_counts2 == (value_counts2.max())].index)[0]
features2 = list(full_columns_name2.drop(label))
parent = None
cost_decision_tree_2 = create_model(5, dataset2, cm_matrix, label, features2, parent)


####-----------------------------MODEL 3 --------------------------------#####


dataset3 = X_train3
dataset3["nobesity"] = list(y_train3)
dataset3 = dataset3.reset_index(drop=True)

k3 = dataset3.shape[1]
value_counts3 = dataset3[label].value_counts()
full_columns_name3 = dataset3.columns
# Find target min_count values
label_min3 = list(value_counts3[value_counts3 == (value_counts3.min())].index)[0]
# Find target max_count values
label_max3 = list(value_counts3[value_counts3 == (value_counts3.max())].index)[0]
features3 = list(full_columns_name3.drop(label))
parent = None
cost_decision_tree_3 = create_model(5, dataset3, cm_matrix, label, features3, parent)


####-----------------------------MODEL FULL --------------------------------#####


dataset_full = X_train_full
dataset_full["nobesity"] = list(y_train_full)
dataset_full = dataset_full.reset_index(drop=True)

k_full = dataset_full.shape[1]
value_counts_full = dataset_full[label].value_counts()
full_columns_name_full = dataset_full.columns
# Find target min_count values
label_min_full = list(
    value_counts_full[value_counts_full == (value_counts_full.min())].index
)[0]
# Find target max_count values
label_max_full = list(
    value_counts_full[value_counts_full == (value_counts_full.max())].index
)[0]
features_full = list(full_columns_name_full.drop(label))
parent = None
cost_decision_tree_full = create_model(
    5, dataset_full, cm_matrix, label, features_full, parent
)


###---------------------TEST MODEL  cost_decision_tree_full-------------------------------###
def cost_test(X_test, cost_tree):
    predicts = []
    list_predict = []
    for i in range(len(X_test)):
        predict_temp = []
        for j in range(len(cost_tree)):
            predict_temp.append(predict(pd.Series(X_test.iloc[i, :]), cost_tree[j]))
            list_predict.append(predict_temp)
        # print(predict_temp)
        predicts.append(max(set(predict_temp), key=predict_temp.count))
    return predicts, list_predict


###-----------TEST MODEL 1  cost_decision_tree_1-------------###
X_test1 = X_test1.reset_index(drop=True)
predicts_1, list_pr = cost_test(X_test1, cost_decision_tree_1)

###-----------TEST MODEL 2  cost_decision_tree_2-------------###
X_test2 = X_test2.reset_index(drop=True)
predicts_1, list_pr = cost_test(X_test2, cost_decision_tree_2)

###-----------TEST MODEL 3  cost_decision_tree_3-------------###
X_test1 = X_test1.reset_index(drop=True)
predicts_1, list_pr = cost_test(X_test1, cost_decision_tree_1)

###-----------TEST MODEL FULL  cost_decision_tree_full-------------###
X_test_full = X_test_full.reset_index(drop=True)
predicts_full, list_pr = cost_test(X_test_full, cost_decision_tree_full)