from imblearn.over_sampling import SMOTE
from data import DATA
import pandas as pd
from function_api import API
from sklearn.tree import DecisionTreeClassifier
from random import choice
from random import shuffle
import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


dataset = pd.read_csv("./data/data_end_encode_balance.csv")

index_class_0 = list(dataset[dataset['obesity']==0].index)
random.shuffle(index_class_0)
index_random_0 = index_class_0[30:]

index_class_1 = list(dataset[dataset['obesity']==1].index)
random.shuffle(index_class_1)
index_random_1 = index_class_1[19:]

index_class_2 = list(dataset[dataset['obesity']==2].index)
random.shuffle(index_class_2)
index_random_2 = index_class_2[26:]

index_class_3 = list(dataset[dataset['obesity']==3].index)
random.shuffle(index_class_3)
index_random_3 = index_class_3[24:]

index_class_4 = list(dataset[dataset['obesity']==4].index)
random.shuffle(index_class_4)
index_random_4 = index_class_4[10:]

columns = ['meal_of_the_day', 'breakfast_of_the_week', 'dinner_of_the_week',
       'fast_food_of_the_week', 'vegetable_in_meal', 'water_of_the_day',
       'protein_of_meal', 'time_do_exercise', 'time_of_sport', 'alcohol',
       'nicotine', 'sleep_time', 'require_of_job', 'park',
       'time_use_tech_equip', 'depression', 'obesity']

for i in list(index_random_0):
    dataset['meal_of_the_day'][i] = 2
    dataset['breakfast_of_the_week'][i] = 3
    dataset['dinner_of_the_week'][i] = 0
    dataset['fast_food_of_the_week'][i] = 0
    dataset['vegetable_in_meal'][i] = 3
    dataset['protein_of_meal'][i] = 0
    dataset['time_do_exercise'][i] = 1
    dataset['time_of_sport'][i] = 1
    dataset['alcohol'][i] = 0
    dataset['nicotine'][i] = 0
    dataset['require_of_job'][i] = 4
    dataset['park'][i] = 0
    dataset['time_use_tech_equip'][i] = random.choice([1,2])
    dataset['depression'][i] = 0



for i in list(index_random_1):
    dataset['meal_of_the_day'][i] = 2
    dataset['breakfast_of_the_week'][i] = 2
    dataset['dinner_of_the_week'][i] = 0
    dataset['fast_food_of_the_week'][i] = 0
    dataset['vegetable_in_meal'][i] = 2
    dataset['protein_of_meal'][i] = 1
    dataset['time_do_exercise'][i] = 3
    dataset['time_of_sport'][i] = 2
    dataset['alcohol'][i] = 1
    dataset['nicotine'][i] = 0
    dataset['require_of_job'][i] = 3
    dataset['park'][i] = 1
    dataset['time_use_tech_equip'][i] = random.choice([1,2])
    dataset['depression'][i] = 0



for i in list(index_random_2):
    dataset['meal_of_the_day'][i] = 3
    dataset['breakfast_of_the_week'][i] = 2
    dataset['dinner_of_the_week'][i] = 1
    dataset['fast_food_of_the_week'][i] = 1
    dataset['vegetable_in_meal'][i] = 2
    dataset['protein_of_meal'][i] = 1
    dataset['time_do_exercise'][i] = 2
    dataset['time_of_sport'][i] = 1
    dataset['alcohol'][i] = 2
    dataset['nicotine'][i] = 1
    dataset['require_of_job'][i] = 2
    dataset['park'][i] = 0
    dataset['time_use_tech_equip'][i] = random.choice([3,4])
    dataset['depression'][i] = 0




for i in list(index_random_3):
    dataset['meal_of_the_day'][i] = 3
    dataset['breakfast_of_the_week'][i] = 1
    dataset['dinner_of_the_week'][i] = 2
    dataset['fast_food_of_the_week'][i] = 2
    dataset['vegetable_in_meal'][i] = 1
    dataset['protein_of_meal'][i] = 2
    dataset['time_do_exercise'][i] = 1
    dataset['time_of_sport'][i] = 0
    dataset['alcohol'][i] = 3
    dataset['nicotine'][i] = 1
    dataset['require_of_job'][i] = 1
    dataset['park'][i] = 0
    dataset['time_use_tech_equip'][i] = random.choice([4,5])
    dataset['depression'][i] = 1

    



for i in list(index_random_4):
    dataset['meal_of_the_day'][i] = 3
    dataset['breakfast_of_the_week'][i] = 0
    dataset['dinner_of_the_week'][i] = 3
    dataset['fast_food_of_the_week'][i] = 3
    dataset['vegetable_in_meal'][i] = 1
    dataset['protein_of_meal'][i] = 2
    dataset['time_do_exercise'][i] =0 
    dataset['time_of_sport'][i] = 0
    dataset['alcohol'][i] = 4
    dataset['nicotine'][i] = 1
    dataset['require_of_job'][i] = 0
    dataset['park'][i] = 0
    dataset['time_use_tech_equip'][i] = random.choice([6,7,8])
    dataset['depression'][i] = 1


X = dataset.iloc[:,:16]
Y = dataset['obesity']
X_train, X_test, y_train, y_test = train_test_split(
                X, Y, test_size=0.333, random_state=40, shuffle=True, stratify=Y)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

acc = accuracy_score(y_pred,y_test)
print(acc)

export_csv = dataset.to_csv(
    r"C:\Users\KHUONG\Desktop\luanvan\auto_ml_flask\data\data_fit.csv",
    index=None,
    header=True,
)