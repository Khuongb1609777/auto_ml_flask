import pandas as pd
from sklearn import preprocessing

dataset = pd.read_excel("./data_api/data3012.xlsx")
del dataset["Địa chỉ email"]
# dataset = dataset.iloc[210:,:]
atribute_names = [
    "time_line",
    "name",
    "gender",
    "year_of_birth",
    "job",
    "height",
    "weight",
    "meal_of_the_day",
    "breakfast_of_the_week",
    "dinner_of_the_week",
    "fast_food_of_the_week",
    "vegetable_in_meal",
    "source_of_food",
    "water_of_the_day",
    "protein_of_meal",
    "time_do_exercise",
    "time_of_sport",
    "alcohol",
    "soda_water",
    "nicotine",
    "sleep_time",
    "chronic_diseases",
    "chronic_diseases_medicine",
    "chronic_diseases_relatives",
    "require_of_job",
    "income",
    "transport",
    "park",
    "time_use_tech_equip",
    "sedative",
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
#   Xử lý dữ liệu năm sinh
for i in range(len(dataset)):
    for j in range(1, 9):
        if (str(dataset["year_of_birth"][i]).count(str("200" + str(j))) >= 1) or (
            str(dataset["year_of_birth"][i]).count(str("2k" + str(j))) >= 1
        ):
            # Chuyển đổi các dữ liệu có ngày sinh và viết tắt
            # dataset.iloc[i, 3] = int(2000+j)
            dataset["year_of_birth"][i] = int(2000 + j)
    if isinstance(dataset["year_of_birth"][i], int) == False:
        # Xóa các bản ghi chứa dữ liệu string (không chứa năm sinh)
        dataset = dataset.drop(i)

dataset = dataset.reset_index(drop=True)


#   Tạo cột tuổi (2020 - năm sinh)
dataset["age"] = 2020 - dataset["year_of_birth"]

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
#   Chuẩn hóa tên gọi các ngành nghề - công việc
for i in range(len(dataset)):
    if (dataset["job"][i] == "IT") or (dataset["job"][i] == "Lập trình viên"):
        dataset["job"][i] = "Developer"


dataset = dataset.reset_index(drop=True)

#   Chuẩn hóa dữ liệu thời gian sử dụng thiết bị công nghệ
for i in range(len(dataset)):
    for j in range(0, 24):
        if str(dataset["time_use_tech_equip"][i]).count(str(j)) >= 1:
            dataset["time_use_tech_equip"][i] = j
    if isinstance(dataset["time_use_tech_equip"][i], int) == False:
        dataset = dataset.drop(i)

dataset = dataset.reset_index(drop=True)


#   Chuẩn hóa dữ liệu phương tiện di chuyển
for i in range(len(dataset)):
    if (
        (str(dataset["transport"][i]).count(str("điện")) >= 1)
        or (str(dataset["transport"][i]).count(str("dien")) >= 1)
        or (str(dataset["transport"][i]).count(str("Điện")) >= 1)
        or (str(dataset["transport"][i]).count(str("Xe đạp điện ")) >= 1)
    ):
        dataset["transport"][i] = "Xe đạp điện"
    if str(dataset["transport"][i]).count(str("Tùy chọn 7")) >= 1:
        dataset["transport"][i] = "Xe đạp"
    if (str(dataset["transport"][i]).count(str("Phụ huynh đưa rước")) >= 1) or (
        str(dataset["transport"][i]).count(str("Được đưa đi học")) >= 1
    ):
        dataset["transport"][i] = "Xe máy"
    if isinstance(dataset["transport"][i], str) == False:
        dataset = dataset.drop(i)


dataset = dataset.reset_index(drop=True)

null_income = [
    "chưa có",
    0,
    "Ko có ",
    "Không có",
    "Không có ",
    "0 có",
    "Ko có",
    "0 đồng",
    "0đ",
    "Không",
    "Chưa có thu nhập",
    "Cha mẹ nuôi",
    "Ko có chủ yếu là ba mẹ",
    "Nô nô ",
    "Chủ yếu từ ba mẹ ",
    "Tuỳ vào kinh tế phụ huynh",
    "0k",
    "Hiện còn đang đi học",
    "Còn đi học",
    "xxx hihi",
    "hehe",
    "Học sinh",
    "Dưới 1 triệu",
]

income_TR = [
    1000000,
    1500000,
    2000000,
    3000000,
    4000000,
    5000000,
    6000000,
    7000000,
    8000000,
    9000000,
    10000000,
]
income_TN = [
    100000,
    200000,
    300000,
    400000,
    500000,
    600000,
    700000,
    800000,
    900000,
    1000000,
]
income_CN = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
income_N = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
income_T = [100, 200, 300, 400, 500, 600, 700, 800, 900]


for i in range(len(dataset)):
    if dataset["income"][i] in list(null_income):
        dataset["income"][i] = 0
    if str(dataset["income"][i]).count(" triệu") >= 1:
        dataset["income"][i] = dataset["income"][i].replace(" triệu", "")
    if str(dataset["income"][i]).count("triệu  ") >= 1:
        dataset["income"][i] = dataset["income"][i].replace("triệu  ", "")
    if str(dataset["income"][i]).count("tr") >= 1:
        dataset["income"][i] = dataset["income"][i].replace("tr", "")
    if str(dataset["income"][i]).count(",") >= 1:
        dataset["income"][i] = dataset["income"][i].replace(",", ".")
    if dataset["income"][i] in list(income_TR):
        dataset["income"][i] = int(dataset["income"][i]) / 1000000
    if dataset["income"][i] in list(income_TN):
        dataset["income"][i] = int(dataset["income"][i]) / 100000
    if dataset["income"][i] in list(income_CN):
        dataset["income"][i] = int(dataset["income"][i]) / 10000
    if dataset["income"][i] in list(income_N):
        dataset["income"][i] = int(dataset["income"][i]) / 1000
    if dataset["income"][i] in list(income_T):
        dataset["income"][i] = int(dataset["income"][i]) / 100


dataset["income"] = dataset["income"].fillna(0)

for i in range(len(dataset)):
    if (
        isinstance(dataset["income"][i], int) == False
        and isinstance(dataset["income"][i], float) == False
    ):
        try:
            dataset["income"][i] = float(dataset["income"][i])
        except:
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


# export_csv = dataset.to_excel(
#     r"C:\Users\KHUONG\Desktop\LUẬN VĂN TỐT NGHIỆP\project\data\khao_sat2.xlsx",
#     sheet_name="sheet1",
#     index=False,
# )

export_csv = dataset.to_csv(
    r"C:\Users\KHUONG\Desktop\AUTO-ML\auto_ml_flask\data_api\data_pre_3012.csv",
    index=None,
    header=True,
)


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

# #   Xử lý dữ liệu job (công việc)
# job_values = dataset["job"].drop_duplicates()
# dataset = transform_encoder(dataset, "job", job_values)


# #   Xử lý dữ liệu số bữa ăn sáng trong tuần
# breakfast_of_the_week_values = [
#     "Không ăn",
#     "Từ 1 - 3 bữa/tuần",
#     "Từ 3 - 6 bữa/tuần",
#     "Mỗi ngày",
# ]

# breakfast_of_the_week_values_level = [0, 1, 2, 3]

# dataset = transform_encoder_level(
#     dataset,
#     "breakfast_of_the_week",
#     breakfast_of_the_week_values,
#     breakfast_of_the_week_values_level,
# )


# #   Xử lý dữ liệu ăn tối trong tuần
# dinner_of_the_week_values = [
#     "Không ăn",
#     "Từ 1 - 3 bữa/tuần",
#     "Từ 3 - 6 bữa/tuần",
#     "Mỗi ngày",
# ]
# dinner_of_the_week_values_level = [0, 1, 2, 3]
dataset = transform_encoder_level(
    dataset,
    "dinner_of_the_week",
    dinner_of_the_week_values,
    dinner_of_the_week_values_level,
)


# #   Xử lý dữ liệu số lần ăn thức ăn nhanh trong tuần
# fast_food_of_the_week_values = [
#     "Không ăn",
#     "Từ 1 - 3 bữa/tuần",
#     "Từ 3 - 6 bữa/tuần",
#     "Mỗi ngày",
# ]
# fast_food_of_the_week_values_level = [0, 1, 2, 3]
# dataset = transform_encoder_level(
#     dataset,
#     "fast_food_of_the_week",
#     fast_food_of_the_week_values,
#     fast_food_of_the_week_values_level,
# )


# #   xử lý dữ liệu lượng rau quả trong bữa ăn
# vegetable_in_meal_values = ["Ít hơn 50 gram", "Từ 50 - 100 gram", "Trên 100 gram"]
# vegetable_in_meal_values_level = [0, 1, 2]
# dataset = transform_encoder_level(
#     dataset,
#     "vegetable_in_meal",
#     vegetable_in_meal_values,
#     vegetable_in_meal_values_level,
# )


# #   Xử lý dữ liệu nguồn gốc thưc phẩm
# source_of_food_values = ["Chợ", "Nguồn thực phẩm nuôi/trồng tại nhà", "Siêu thị"]
# dataset = transform_encoder(dataset, "source_of_food", source_of_food_values)


# #   Xử lý dữ liệu lượng nước uống mỗi ngày
# water_of_day_values = ["Ít hơn 1 lít", "Từ 1 - 2 lít", "Từ 2 - 3 lít", "Trên 3 lít"]
# water_of_day_values_level = [0, 1, 2, 3]
# dataset = transform_encoder_level(
#     dataset,
#     "water_of_the_day",
#     water_of_day_values,
#     water_of_day_values_level,
# )

# #   Xử lý dữ liệu lượng thực phẩm chứa nhiều protein/ngày
# protein_of_meal_values = ["Ít hơn 50 gram", "Từ 50 - 100 gram", "Trên 100 gram"]
# protein_of_meal_values_level = [0, 1, 2]
# dataset = transform_encoder_level(
#     dataset,
#     "protein_of_meal",
#     protein_of_meal_values,
#     protein_of_meal_values_level,
# )


# #   Xử lý dữ liệu  time_do_exercise
# time_do_exercise_values = ["Gần như không", "Dưới 1 giờ", "Từ 1 - 3 giờ", "Trên 3 giờ"]
# time_do_exercise_values_level = [0, 1, 2, 3]
# dataset = transform_encoder_level(
#     dataset,
#     "time_do_exercise",
#     time_do_exercise_values,
#     time_do_exercise_values_level,
# )


# #   Xử lý dữ liệu sport time
# time_of_sport_values = ["Gần như không", "Dưới 2 giờ", "Từ 2 - 4 giờ", "Trên 4 giờ"]
# time_of_sport_values_level = [0, 1, 2, 3]
# dataset = transform_encoder_level(
#     dataset,
#     "time_of_sport",
#     time_of_sport_values,
#     time_of_sport_values_level,
# )


# #   Xử lý dữ liệu alcohol
# alcohol_values = ["Không", "Ít", "Trung bình", "Nhiều", "Thường xuyên"]
# alcohol_values_level = [0, 1, 2, 3, 4]
# dataset = transform_encoder_level(
#     dataset,
#     "alcohol",
#     alcohol_values,
#     alcohol_values_level,
# )

# ###################################################################################################################################

# #   Xử lý dữ liệu soda water
# soda_water_values = [
#     "Không",
#     "Ít",
#     "Trung bình",
#     "Nhiều",
#     "Thường xuyên",
# ]
# soda_water_values_level = [0, 1, 2, 3, 4]
# dataset = transform_encoder_level(
#     dataset,
#     "soda_water",
#     soda_water_values,
#     soda_water_values_level,
# )

# #   Xử lý dữ liệu nicotine
# nicotine_values = ["Không", "Có"]
# dataset = transform_encoder(dataset, "nicotine", nicotine_values)


# #   Xử lý dữ liệu chronic_diseases (bệnh mãn tính)
# chronic_diseases_values = ["Không", "Có"]
# dataset = transform_encoder(dataset, "chronic_diseases", chronic_diseases_values)


# #   Xử lý dữ liệu chronic_diseases_relatives (có người thân mắc bệnh mãn tính)
# chronic_diseases_relatives_values = ["Không", "Có"]
# dataset = transform_encoder(
#     dataset, "chronic_diseases_relatives", chronic_diseases_relatives_values
# )


# #   Xử lý dữ liệu chronic_diseases_medicine (dùng thuốc trị bệnh mãn tính)
# chronic_diseases_medicine_values = ["Không", "Có"]
# dataset = transform_encoder(
#     dataset, "chronic_diseases_medicine", chronic_diseases_medicine_values
# )


# #   Xử lý dữ liệu transport
# transport_values = dataset["transport"].drop_duplicates()
# dataset = transform_encoder(dataset, "transport", transport_values)


# #   Xử lý dữ liệu park
# park_values = ["Không", "Có"]
# dataset = transform_encoder(dataset, "park", park_values)


# #   Xử lý dữ liệu sedative
# sedative_values = ["Không", "Có"]
# dataset = transform_encoder(dataset, "sedative", sedative_values)

# #   Xử lý dữ liệu depression
# depression_values = ["Không", "Có"]
# dataset = transform_encoder(dataset, "depression", depression_values)

# dataset = dataset.reset_index(drop=True)
# #   Xử lý dữ liệu thời gian ngủ

# # atribute_names_p = [
# #     "time_line_p",
# #     "name_P",
# #     "gender_p",
# #     "year_of_birth_p",
# #     "job_p",
# #     "height_p",
# #     "weight_p",
# #     "meal_of_the_day_p",
# #     "breakfast_of_the_week_p",
# #     "dinner_of_the_week_p",
# #     "fast_food_of_the_week_p",
# #     "vegetable_in_meal_p",
# #     "source_of_food_P",
# #     "water_of_the_day_p",
# #     "protein_of_meal_p",
# #     "time_do_exercise_p",
# #     "time_of_sport_P",
# #     "alcohol_p",
# #     "soda_water_p",
# #     "nicotine_p",
# #     "sleep_time_P",
# #     "chronic_diseases_P",
# #     "chronic_diseases_medicine_p",
# #     "chronic_diseases_relatives_P",
# #     "require_of_job_p",
# #     "income_P",
# #     "transport_P",
# #     "park_P",
# #     "time_use_tech_equip_p",
# #     "sedative_p",
# #     "depression_P",
# # ]

# export_csv = dataset.to_csv(
#     r"C:\Users\KHUONG\Desktop\LUẬN VĂN TỐT NGHIỆP\project\data\data_prep_level_1.csv",
#     index=None,
#     header=True,
# )
