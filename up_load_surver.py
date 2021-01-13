from os import path
from data import DATA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
from function_api import API

dataset = pd.read_csv("./data/data_end_encode_balance.csv")
# dataset = pd.read_csv("./data/data_end_no_encode.csv")
# dataset_p["BMI"] = dataset["weight"] / (dataset["height"] * dataset["height"])

for i in range(len(dataset)):
    data_post = {
        "mealOfTheDay": int(dataset["meal_of_the_day"][i]),
        "breakfastOfTheWeek": str(dataset["breakfast_of_the_week"][i]),
        "dinnerOfTheWeek": str(dataset["dinner_of_the_week"][i]),
        "fastFoodOfTheWeek": str(dataset["fast_food_of_the_week"][i]),
        "vegetableInMeal": str(dataset["vegetable_in_meal"][i]),
        "waterOfTheDay": str(dataset["water_of_the_day"][i]),
        "proteinOfMeal": str(dataset["protein_of_meal"][i]),
        "timeDoExcerciseForWeek": str(dataset["time_do_exercise"][i]),
        "sportTimeForWeek": str(dataset["time_of_sport"][i]),
        "alcohol": str(dataset["alcohol"][i]),
        "nicotine": str(dataset["nicotine"][i]),
        "timeSleep": str(dataset["sleep_time"][i]),
        "requireOfJob": str(dataset["require_of_job"][i]),
        "park": str(dataset["park"][i]),
        "timeUseTechEquip": str(dataset["time_use_tech_equip"][i]),
        "depression": str(dataset["depression"][i]),
        "obesity": int(dataset["obesity"][i]),
    }
    class_name = "DatasetSurveyBalance"
    data = API.post(class_name, data_post)
