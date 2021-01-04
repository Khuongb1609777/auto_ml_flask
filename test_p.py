from os import path
from data import DATA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
from function_api import API

dataset = pd.read_csv("./data_api/data_prep_21.csv")
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

dataset["nobesity"] = class_values

for i in range(len(dataset)):
    data_post = {
        "name": dataset["name"][i],
        "gender": int(dataset["gender"][i]),
        "yearOfBirth": int(dataset["year_of_birth"][i]),
        "job": int(dataset["job"][i]),
        "height": float(dataset["height"][i]),
        "weight": int(dataset["weight"][i]),
        "mealOfTheDay": int(dataset["meal_of_the_day"][i]),
        "breakfastOfTheWeek": int(dataset["breakfast_of_the_week"][i]),
        "dinnerOfTheWeek": int(dataset["dinner_of_the_week"][i]),
        "fastFoodOfTheWeek": int(dataset["fast_food_of_the_week"][i]),
        "vegetableInMeal": int(dataset["vegetable_in_meal"][i]),
        "sourceOfFood": int(dataset["source_of_food"][i]),
        "waterOfTheDay": int(dataset["water_of_the_day"][i]),
        "proteinOfMeal": int(dataset["protein_of_meal"][i]),
        "timeDoExcerciseForWeek": int(dataset["time_do_exercise"][i]),
        "sportTimeForWeek": int(dataset["time_of_sport"][i]),
        "alcohol": int(dataset["alcohol"][i]),
        "sodaWater": int(dataset["soda_water"][i]),
        "nicotine": int(dataset["nicotine"][i]),
        "timeSleep": int(dataset["sleep_time"][i]),
        "chronicDiseases": int(dataset["chronic_diseases"][i]),
        "chronicDiseasesMedicine": int(dataset["chronic_diseases_medicine"][i]),
        "chronicDiseasesRelative": int(dataset["chronic_diseases_relatives"][i]),
        "requireOfJob": int(dataset["require_of_job"][i]),
        "income": float(dataset["income"][i]),
        "transport": int(dataset["transport"][i]),
        "park": int(dataset["park"][i]),
        "timeUseTechEquip": int(dataset["time_use_tech_equip"][i]),
        "sedative": int(dataset["sedative"][i]),
        "depression": int(dataset["depression"][i]),
        "age": int(dataset["age"][i]),
        "obesity": int(dataset["nobesity"][i]),
    }
    class_name = "DatasetPreprocessing"
    data = API.post(class_name, data_post)