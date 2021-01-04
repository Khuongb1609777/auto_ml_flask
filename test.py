from os import path
from data import DATA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
from function_api import API

dataset = pd.read_csv("./data_api/data_end.csv")
dataset_p = pd.read_csv("./data_api/data_prep_21.csv")
dataset_p["BMI"] = dataset["weight"] / (dataset["height"] * dataset["height"])

class_values = []
for i in range(len(dataset_p)):
    if (dataset_p["BMI"][i]) < 18.5:
        class_values.append(0)
    elif (dataset_p["BMI"][i]) >= 18.5 and (dataset_p["BMI"][i]) < 23:
        class_values.append(1)
    elif (dataset_p["BMI"][i] >= 23) and (dataset_p["BMI"][i]) < 25:
        class_values.append(2)
    elif (dataset_p["BMI"][i]) >= 25 and (dataset_p["BMI"][i]) < 30:
        class_values.append(3)
    elif (dataset_p["BMI"][i] >= 30) and (dataset_p["BMI"][i]) < 40:
        class_values.append(4)
    else:
        class_values.append(5)

dataset_p["obesity"] = class_values

for i in range(len(dataset)):
    data_post = {
        "name": str(dataset["name"][i]),
        "gender": str(dataset["gender"][i]),
        "gender_p": int(dataset_p["gender"][i]),
        "yearOfBirth": int(dataset["year_of_birth"][i]),
        "job": str(dataset["job"][i]),
        "job_p": int(dataset_p["job"][i]),
        "height": float(dataset["height"][i]),
        "height_p": float(dataset_p["height"][i]),
        "weight": int(dataset["weight"][i]),
        "weight_p": int(dataset_p["weight"][i]),
        "mealOfTheDay": int(dataset["meal_of_the_day"][i]),
        "mealOfTheDay_p": int(dataset_p["meal_of_the_day"][i]),
        "breakfastOfTheWeek": str(dataset["breakfast_of_the_week"][i]),
        "breakfastOfTheWeek_p": int(dataset_p["breakfast_of_the_week"][i]),
        "dinnerOfTheWeek": str(dataset["dinner_of_the_week"][i]),
        "dinnerOfTheWeek_p": int(dataset_p["dinner_of_the_week"][i]),
        "fastFoodOfTheWeek": str(dataset["fast_food_of_the_week"][i]),
        "fastFoodOfTheWeek_p": int(dataset_p["fast_food_of_the_week"][i]),
        "vegetableInMeal": str(dataset["vegetable_in_meal"][i]),
        "vegetableInMeal_p": int(dataset_p["vegetable_in_meal"][i]),
        "sourceOfFood": str(dataset["source_of_food"][i]),
        "sourceOfFood_p": int(dataset_p["source_of_food"][i]),
        "waterOfTheDay": str(dataset["water_of_the_day"][i]),
        "waterOfTheDay_p": int(dataset_p["water_of_the_day"][i]),
        "proteinOfMeal": str(dataset["protein_of_meal"][i]),
        "proteinOfMeal_p": int(dataset_p["protein_of_meal"][i]),
        "timeDoExcerciseForWeek": str(dataset["time_do_exercise"][i]),
        "timeDoExcerciseForWeek_p": int(dataset_p["time_do_exercise"][i]),
        "sportTimeForWeek": str(dataset["time_of_sport"][i]),
        "sportTimeForWeek_p": int(dataset_p["time_of_sport"][i]),
        "alcohol": str(dataset["alcohol"][i]),
        "alcohol_p": int(dataset_p["alcohol"][i]),
        "sodaWater": str(dataset["soda_water"][i]),
        "sodaWater_p": int(dataset_p["soda_water"][i]),
        "nicotine": str(dataset["nicotine"][i]),
        "nicotine_p": int(dataset_p["nicotine"][i]),
        "timeSleep": str(dataset["sleep_time"][i]),
        "timeSleep_p": int(dataset_p["sleep_time"][i]),
        "chronicDiseases": dataset["chronic_diseases"][i],
        "chronicDiseases_p": int(dataset_p["chronic_diseases"][i]),
        "chronicDiseasesMedicine": dataset["chronic_diseases_medicine"][i],
        "chronicDiseasesMedicine_p": int(dataset_p["chronic_diseases_medicine"][i]),
        "chronicDiseasesRelative": dataset["chronic_diseases_relatives"][i],
        "chronicDiseasesRelative_p": int(dataset_p["chronic_diseases_relatives"][i]),
        "requireOfJob": str(dataset["require_of_job"][i]),
        "income": str(dataset["income"][i]),
        "income_p": int(dataset_p["income"][i]),
        "transport": dataset["transport"][i],
        "transport_p": int(dataset_p["transport"][i]),
        "park": dataset["park"][i],
        "park_p": int(dataset_p["park"][i]),
        "timeUseTechEquip": str(dataset["time_use_tech_equip"][i]),
        "timeUseTechEquip_p": int(dataset_p["time_use_tech_equip"][i]),
        "sedative": dataset["sedative"][i],
        "sedative_p": int(dataset_p["sedative"][i]),
        "depression": dataset["depression"][i],
        "depression_p": int(dataset_p["depression"][i]),
        "age": str(dataset["age"][i]),
        "age_p": int(dataset_p["age"][i]),
        "BMI": float(dataset_p["BMI"][i]),
        "obesity": int(dataset_p["obesity"][i]),
    }
    class_name = "DatasetMerge"
    data = API.post(class_name, data_post)