import pandas as pd
from sklearn import preprocessing

dataset = pd.read_excel("./data/dataset.xlsx")
# dataset = dataset.iloc[210:,:]
atribute_names = [
    "height",
    "weight",
    "meal_of_the_day",
    "breakfast_of_the_week",
    "dinner_of_the_week",
    "fast_food_of_the_week",
    "vegetable_in_meal",
    "water_of_the_day",
    "protein_of_meal",
    "time_do_exercise",
    "time_of_sport",
    "alcohol",
    "nicotine",
    "sleep_time",
    "require_of_job",
    "park",
    "time_use_tech_equip",
    "depression",
]

dataset.columns = atribute_names

# create transform function


def transform_encoder(data, feature_name, array_feature):
    label_encoder = preprocessing.LabelEncoder()
    arr_temp = label_encoder.fit_transform(data[feature_name])
    data[feature_name] = arr_temp
    return data

dataset = dataset.reset_index(drop=True)


#   Xử lý dữ liệu chiều cao loại bỏ (cm) và xử lý các giá trị 1mxx

for i in range(len(dataset)):
    for j in range(0, 100):
        if (
            (str(dataset["height"][i]).count(str("1m" + str(j))) >= 1)
            or (str(dataset["height"][i]).count(str(str(100 + j) + "cm")) >= 1)
            or (str(dataset["height"][i]).count(str(str(100 + j))) >= 1)
        ):
            dataset["height"][i] = float(1 + float("0." + str(j)))
    dataset["height"]
    if isinstance(dataset["height"][i], float) == False:
        try:
            dataset["height"][i] = float(dataset["height"][i])
        except:
            dataset = dataset.drop(i)

dataset = dataset.reset_index(drop=True)
#   Xử lý dữ liệu cân năng loại bỏ (kg)

for i in range(len(dataset)):
    for j in range(100, 150):
        if str(dataset["weight"][i]).count(str(j)) >= 1:
            dataset["weight"][i] = int(j)
    for j in range(10, 100):
        if str(dataset["weight"][i]).count(str(j)) >= 1:
            dataset["weight"][i] = int(j)
    if isinstance(dataset["weight"][i], int) == False:
        dataset = dataset.drop(i)

dataset = dataset.reset_index(drop=True)


#   Chuẩn hóa dữ liệu thời gian sử dụng thiết bị công nghệ
for i in range(len(dataset)):
    for j in range(0, 24):
        if str(dataset["time_use_tech_equip"][i]).count(str(j)) >= 1:
            dataset["time_use_tech_equip"][i] = j
    if isinstance(dataset["time_use_tech_equip"][i], int) == False:
        dataset = dataset.drop(i)

dataset = dataset.reset_index(drop=True)

for i in range(len(dataset)):
    for j in range(3, 24):
        if str(dataset["sleep_time"][i]).count(str(j)) >= 1:
            dataset["sleep_time"][i] = int(j)
    if isinstance(dataset["sleep_time"][i], int) == False:
        for k in range(1, 3):
            if str(dataset["sleep_time"][i]).count(str(k)) >= 1:
                dataset["sleep_time"][i] = int(k)




# export_csv = dataset.to_csv(
#     r"C:\Users\KHUONG\Desktop\luanvan\auto_ml_flask\data\data_end_no_encode.csv",
#     index=None,
#     header=True,
# )


# dataset1 = pd.read_csv("../data/data_pre_1.csv")


# for name in list(atribute_names):
#     print(dataset[name].value_counts())


# #   Kết thúc tiền xử lý giá triij giai đoạn 1

# #   Giai đoạn 2 chuẩn hóa dữ liệu


# #   Tạo hàm chuyển đổi dữ liệu
# def transform_encoder(dataset, feature_name, array_feature):
#     le = preprocessing.LabelEncoder()
#     le.fit(array_feature)
#     dataset[feature_name] = le.transform(dataset[feature_name])
#     return dataset


#   Ham chuyen doi du lieu co thu tu
def transform_encoder_level(dataset, feature_name, feature_values, feture_values_level):
    for i in range(len(dataset)):
        for j in range(len(feature_values)):
            if dataset[feature_name][i] == feature_values[j]:
                dataset[feature_name][i] = feture_values_level[j]
    return dataset


# # reversed feature values
# dataset = transform_encoder(dataset, "gender", ["Nữ", "Nam"])
# # le.inverse_transform(arr_after_transform)


# #   Xử lý dữ liệu số bữa ăn sáng trong tuần
breakfast_of_the_week_values = [
    "Không ăn",
    "Từ 1 - 3 bữa/tuần",
    "Từ 3 - 6 bữa/tuần",
    "Mỗi ngày",
]

breakfast_of_the_week_values_level = [0, 1, 2, 3]

dataset = transform_encoder_level(
    dataset,
    "breakfast_of_the_week",
    breakfast_of_the_week_values,
    breakfast_of_the_week_values_level,
)


#   Xử lý dữ liệu ăn tối trong tuần
dinner_of_the_week_values = [
    "Không ăn",
    "Từ 1 - 3 bữa/tuần",
    "Từ 3 - 6 bữa/tuần",
    "Mỗi ngày",
]
dinner_of_the_week_values_level = [0, 1, 2, 3]
dataset = transform_encoder_level(
    dataset,
    "dinner_of_the_week",
    dinner_of_the_week_values,
    dinner_of_the_week_values_level,
)


#   Xử lý dữ liệu số lần ăn thức ăn nhanh trong tuần
fast_food_of_the_week_values = [
    "Không ăn",
    "Từ 1 - 3 bữa/tuần",
    "Từ 3 - 6 bữa/tuần",
    "Mỗi ngày",
]
fast_food_of_the_week_values_level = [0, 1, 2, 3]
dataset = transform_encoder_level(
    dataset,
    "fast_food_of_the_week",
    fast_food_of_the_week_values,
    fast_food_of_the_week_values_level,
)


#   xử lý dữ liệu lượng rau quả trong bữa ăn
vegetable_in_meal_values = ["Ít hơn 50 gram", "Từ 50 - 100 gram", "Trên 100 gram"]
vegetable_in_meal_values_level = [0, 1, 2]
dataset = transform_encoder_level(
    dataset,
    "vegetable_in_meal",
    vegetable_in_meal_values,
    vegetable_in_meal_values_level,
)


#   Xử lý dữ liệu lượng nước uống mỗi ngày
water_of_day_values = ["Ít hơn 1 lít", "Từ 1 - 2 lít", "Từ 2 - 3 lít", "Trên 3 lít"]
water_of_day_values_level = [0, 1, 2, 3]
dataset = transform_encoder_level(
    dataset,
    "water_of_the_day",
    water_of_day_values,
    water_of_day_values_level,
)

#   Xử lý dữ liệu lượng thực phẩm chứa nhiều protein/ngày
protein_of_meal_values = ["Ít hơn 50 gram", "Từ 50 - 100 gram", "Trên 100 gram"]
protein_of_meal_values_level = [0, 1, 2]
dataset = transform_encoder_level(
    dataset,
    "protein_of_meal",
    protein_of_meal_values,
    protein_of_meal_values_level,
)


#   Xử lý dữ liệu  time_do_exercise
time_do_exercise_values = ["Gần như không", "Dưới 1 giờ", "Từ 1 - 3 giờ", "Trên 3 giờ"]
time_do_exercise_values_level = [0, 1, 2, 3]
dataset = transform_encoder_level(
    dataset,
    "time_do_exercise",
    time_do_exercise_values,
    time_do_exercise_values_level,
)


#   Xử lý dữ liệu sport time
time_of_sport_values = ["Gần như không", "Dưới 2 giờ", "Từ 2 - 4 giờ", "Trên 4 giờ"]
time_of_sport_values_level = [0, 1, 2, 3]
dataset = transform_encoder_level(
    dataset,
    "time_of_sport",
    time_of_sport_values,
    time_of_sport_values_level,
)


#   Xử lý dữ liệu alcohol
alcohol_values = ["Không", "Ít", "Trung bình", "Nhiều", "Thường xuyên"]
alcohol_values_level = [0, 1, 2, 3, 4]
dataset = transform_encoder_level(
    dataset,
    "alcohol",
    alcohol_values,
    alcohol_values_level,
)


#   Xử lý dữ liệu nicotine
nicotine_values = ["Không", "Có"]
dataset = transform_encoder_level(dataset, "nicotine", nicotine_values, [0,1])



#   Xử lý dữ liệu park
park_values = ["Không", "Có"]
dataset = transform_encoder_level(dataset, "park", park_values, [0,1])


#   Xử lý dữ liệu depression
depression_values = ["Không", "Có"]
dataset = transform_encoder_level(dataset, "depression", depression_values, [0,1])

dataset['BMI'] = dataset['weight']/(dataset['height']*dataset['height'])

dataset = dataset.reset_index(drop = True)

obesity = []

for i in range(len(dataset)):
    if dataset['BMI'][i] < 18.5:
        obesity.append(0)
    elif (dataset['BMI'][i] >= 18.5) and (dataset['BMI'][i] < 23):
        obesity.append(1)
    elif (dataset['BMI'][i] >= 23) and (dataset['BMI'][i] < 25):
        obesity.append(2)
    elif (dataset['BMI'][i] >= 25) and (dataset['BMI'][i] < 30):
        obesity.append(3)
    elif (dataset['BMI'][i] >= 30) and (dataset['BMI'][i] < 40):
        obesity.append(4)
    elif (dataset['BMI'][i] > 40):
        obesity.append(5)

dataset['obesity'] = obesity

export_csv = dataset.to_csv(
    r"C:\Users\KHUONG\Desktop\luanvan\auto_ml_flask\data\data_chart.csv",
    index=None,
    header=True,
)
