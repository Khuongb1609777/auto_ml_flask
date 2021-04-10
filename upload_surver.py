from os import path
from data import DATA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
from function_api import API

dataset = pd.read_csv("./data/data_fit.csv")
# dataset = pd.read_csv("./data/data_end_no_encode.csv")
# dataset_p["BMI"] = dataset["weight"] / (dataset["height"] * dataset["height"])

for i in range(len(dataset)):
    data_post = {
        "mealOfTheDay": int(dataset["meal_of_the_day"][i]),
        "breakfastOfTheWeek": float(dataset["breakfast_of_the_week"][i]),
        "dinnerOfTheWeek": float(dataset["dinner_of_the_week"][i]),
        "fastFoodOfTheWeek": float(dataset["fast_food_of_the_week"][i]),
        "vegetableInMeal": float(dataset["vegetable_in_meal"][i]),
        "waterOfTheDay": float(dataset["water_of_the_day"][i]),
        "proteinOfMeal": float(dataset["protein_of_meal"][i]),
        "timeDoExcerciseForWeek": float(dataset["time_do_exercise"][i]),
        "sportTimeForWeek": float(dataset["time_of_sport"][i]),
        "alcohol": float(dataset["alcohol"][i]),
        "nicotine": float(dataset["nicotine"][i]),
        "timeSleep": float(dataset["sleep_time"][i]),
        "requireOfJob": float(dataset["require_of_job"][i]),
        "park": float(dataset["park"][i]),
        "timeUseTechEquip": float(dataset["time_use_tech_equip"][i]),
        "depression": float(dataset["depression"][i]),
        "obesity": int(dataset["obesity"][i]),
    }
    class_name = "DatasetSurveyBalance"
    data = API.post(class_name, data_post)
