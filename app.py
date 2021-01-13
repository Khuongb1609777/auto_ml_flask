# server/app.py
from logging import exception
from flask import (
    template_rendered,
    render_template,
    request,
    jsonify,
    current_app,
    send_from_directory,
    send_file,
    safe_join,
)
from flask import Flask
from flask_cors import cross_origin
from flask_cors import CORS
from data import DATA
from werkzeug.utils import secure_filename
from urllib.request import urlretrieve
import os
import joblib

# from main_algorithm import *
from urllib.request import urlopen
import pickle
import uuid
import httplib2
import urllib3
import json
import csv
import ast
import sys
from urllib.parse import urlencode
from itertools import chain
import pandas as pd
import numpy as np
from parse import *
from function_api import API
from algorithm_parent import algorithm
from svm_tool import svm_algorithm
from randomforest_tool import randomforest_algorithm
from naive_bayes_tool import naive_bayes_algorithm
from decisiontree_tool import decision_tree_algorithm
from main_algorithm import *


UPLOAD_FOLDER = "./upload_temp"
DOWNLOAD_FOLDER = "./download_temp"
DATA_API_FOLDER = "./data_api"

app = Flask(__name__, static_folder="../front/dist/front", static_url_path="")
CORS(app)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
app.config["DATA_API_FOLDER"] = DATA_API_FOLDER


@app.route("/", methods=["POST", "get"])
def home():
    return "Server python [5000]"


@app.route("/upload-dataset", methods=["POST"])
# @cross_origin()
def upload_dataset():
    try:
        dataset = pd.read_csv("./data_api/data_preprocessing_2.csv")
        print(dataset)
        for i in range(len(dataset)):
            data_post = {
                "name": dataset["name"][i],
                "gender": str(dataset["gender"][i]),
                "yearOfBirth": int(dataset["year_of_birth"][i]),
                "job": dataset["job"][i],
                "height": float(dataset["height"][i]),
                "weight": int(dataset["weight"][i]),
                "mealOfTheDay": int(dataset["meal_of_the_day"][i]),
                "breakfastOfTheWeek": dataset["breakfast_of_the_week"][i],
                "dinnerOfTheWeek": dataset["dinner_of_the_week"][i],
                "fastFoodOfTheWeek": dataset["fast_food_of_the_week"][i],
                "vegetableInMeal": dataset["vegetable_in_meal"][i],
                "sourceOfFood": dataset["source_of_food"][i],
                "waterOfTheDay": dataset["water_of_the_day"][i],
                "proteinOfMeal": dataset["protein_of_meal"][i],
                "timeDoExcerciseForWeel": dataset["time_do_exercise"][i],
                "sportTimeForWeek": dataset["time_of_sport"][i],
                "alcohol": dataset["alcohol"][i],
                "sodaWater": dataset["soda_water"][i],
                "nicotine": dataset["nicotine"][i],
                "timeSleep": str(dataset["sleep_time"][i]),
                "chronicDiseases": dataset["chronic_diseases"][i],
                "chronicDiseasesMedicine": dataset["chronic_diseases_medicine"][i],
                "chronicDiseasesRelative": dataset["chronic_diseases_relatives"][i],
                "requireOfJob": str(dataset["require_of_job"][i]),
                "income": str(dataset["income"][i]),
                "transport": dataset["transport"][i],
                "park": dataset["park"][i],
                "timeUseTechEquip": str(dataset["time_use_tech_equip"][i]),
                "sedative": dataset["sedative"][i],
                "depression": dataset["depression"][i],
                "age": str(dataset["age"][i]),
            }
            class_name = "Dataset"
            data = API.post(class_name, data_post)
        return data
    except UnboundLocalError:
        print("[error] ")
        return "fail, can't upload dataset"


# @app.route("/add_record", methods=["POST"])
# # @cross_origin()
# def add_record():
#     try:
#         print("a")
#     except Exception as e:
#         print(e)


@app.route("/get-datasets", methods=["GET"])
@cross_origin()
def get_datasets():
    try:
        class_name = request.args.get("className")
        # class_name = "Dataset"
        r = API.get_class(class_name)
        return r.data
    except:
        print("[Error] (getDataModels function app.py)")
        return "[Error] BAD REQUEST can't get datamodel"


@app.route("/get-data-charts", methods=["GET"])
@cross_origin()
def get_data_charts():
    try:
        class_name = request.args.get("className")
        r = API.get_class(class_name)
        arr = str(r.data, "utf-8")
        r_json = json.loads(arr)
        data = r_json["results"]
        df = pd.DataFrame(data)
        data_mealOfTheDay = DATA.get_data_chart(df, "mealOfTheDay")
        data_breakfastOfTheWeek = DATA.get_data_chart(df, "breakfastOfTheWeek")
        data_dinnerOfTheWeek = DATA.get_data_chart(df, "dinnerOfTheWeek")
        data_fastfoodOfTheWeek = DATA.get_data_chart(df, "fastFoodOfTheWeek")
        data_vegetableInMeal = DATA.get_data_chart(df, "vegetableInMeal")
        data_proteinOfMeal = DATA.get_data_chart(df, "proteinOfMeal")
        data_waterOfTheDay = DATA.get_data_chart(df, "waterOfTheDay")
        data_timeDoExcerciseForWeek = DATA.get_data_chart(df, "timeDoExcerciseForWeek")
        data_sportTimeForWeek = DATA.get_data_chart(df, "sportTimeForWeek")
        data_alcohol = DATA.get_data_chart(df, "alcohol")
        data_nicotine = DATA.get_data_chart(df, "nicotine")
        data_requireOfJob = DATA.get_data_chart(df, "requireOfJob")
        data_park = DATA.get_data_chart(df, "park")
        data_depression = DATA.get_data_chart(df, "depression")
        data_result = {
            "chart_meal_of_theday": data_mealOfTheDay,
            "chart_breakfast_of_theweek": data_breakfastOfTheWeek,
            "chart_dinner_of_theweek": data_dinnerOfTheWeek,
            "chart_fastfood_of_theweek": data_fastfoodOfTheWeek,
            "chart_vegetable_in_meal": data_vegetableInMeal,
            "chart_protein_of_meal": data_proteinOfMeal,
            "chart_water_of_the_day": data_waterOfTheDay,
            "chart_time_doexcercise_for_week": data_timeDoExcerciseForWeek,
            "chart_sporttime_for_week": data_sportTimeForWeek,
            "chart_alcohol": data_alcohol,
            "chart_nicotine": data_nicotine,
            "chart_requireOfJob": data_requireOfJob,
            "chart_park": data_park,
            "chart_depression": data_depression,
        }
        # data_result = json.dumps(data_result)
        return data_result
    except:
        print("[Error] (getDataModels function app.py)")
        return "[Error] BAD REQUEST can't get datamodel"


@app.route("/get-data-charts-obesity", methods=["GET"])
@cross_origin()
def get_data_charts_obesity():
    try:
        class_name = request.args.get("className")
        # class_name = "Dataset"
        r = API.get_class(class_name)
        arr = str(r.data, "utf-8")
        r_json = json.loads(arr)
        data = r_json["results"]
        df = pd.DataFrame(data)
        columns = list(df.columns)[4:]
        columns.remove("weight")
        for i in range(len(df)):
            for column in list(columns):
                try:
                    df[column][i] = int(round(df[column][i]))
                except:
                    df[column][i] = str(df[column][i])
        data_FAVC = DATA.get_data_chart(df, "FAVC")
        data_gender = DATA.get_data_chart(df, "gender")
        data_NCP = DATA.get_data_chart(df, "NCP")
        data_FHWO = DATA.get_data_chart(df, "FHWO")
        data_CAEC = DATA.get_data_chart(df, "CAEC")
        data_CH2O = DATA.get_data_chart(df, "CH2O")
        data_SMOKE = DATA.get_data_chart(df, "SMOKE")
        data_FCVC = DATA.get_data_chart(df, "FCVC")
        data_SCC = DATA.get_data_chart(df, "SCC")
        data_FAF = DATA.get_data_chart(df, "FAF")
        data_TUE = DATA.get_data_chart(df, "TUE")
        data_CALC = DATA.get_data_chart(df, "CALC")
        data_MTRANS = DATA.get_data_chart(df, "MTRANS")
        data_NObeyesdad = DATA.get_data_chart(df, "NObeyesdad")
        df1 = df.sort_values(by=["weight"], ascending=True).reset_index(drop=True)
        weight_values = {
            "duoi_40": [],
            "duoi_50": [],
            "duoi_60": [],
            "duoi_70": [],
            "duoi_80": [],
            "duoi_90": [],
            "duoi_100": [],
            "tren_100": [],
        }
        for i in range(len(df1)):
            if float(df1["weight"][i]) < 40:
                weight_values["duoi_40"].append(float(df1["height"][i]))
            elif (float(df1["weight"][i]) >= 40) and (float(df1["weight"][i]) < 50):
                weight_values["duoi_50"].append(float(df1["height"][i]))
            elif (float(df1["weight"][i]) >= 50) and (float(df1["weight"][i]) < 60):
                weight_values["duoi_60"].append(float(df1["height"][i]))
            elif (float(df1["weight"][i]) >= 60) and (float(df1["weight"][i]) < 70):
                weight_values["duoi_70"].append(float(df1["height"][i]))
            elif (float(df1["weight"][i]) >= 70) and (float(df1["weight"][i]) < 80):
                weight_values["duoi_80"].append(float(df1["height"][i]))
            elif (float(df1["weight"][i]) >= 80) and (float(df1["weight"][i]) < 90):
                weight_values["duoi_90"].append(float(df1["height"][i]))
            elif (float(df1["weight"][i]) >= 90) and (float(df1["weight"][i]) < 100):
                weight_values["duoi_100"].append(float(df1["height"][i]))
            elif float(df1["weight"][i]) >= 100:
                weight_values["tren_100"].append(float(df1["height"][i]))
        data_height_weight = [
            {
                "name": "Ít hơn 40 kg",
                "value": DATA.trung_binh(weight_values["duoi_40"]),
            },
            {
                "name": "Từ 40 - 50 kg",
                "value": DATA.trung_binh(weight_values["duoi_50"]),
            },
            {
                "name": "Từ 50 - 60 kg",
                "value": DATA.trung_binh(weight_values["duoi_60"]),
            },
            {
                "name": "Từ 60 - 70 kg",
                "value": DATA.trung_binh(weight_values["duoi_70"]),
            },
            {
                "name": "Từ 70 - 80 kg",
                "value": DATA.trung_binh(weight_values["duoi_80"]),
            },
            {
                "name": "Từ 80 - 90 kg",
                "value": DATA.trung_binh(weight_values["duoi_90"]),
            },
            {
                "name": "Từ 90 - 100 kg",
                "value": DATA.trung_binh(weight_values["duoi_100"]),
            },
            {
                "name": "Trên 100 kg",
                "value": DATA.trung_binh(weight_values["tren_100"]),
            },
        ]
        data_age = [
            {"name": "Dưới 20 tuổi", "value": 0},
            {"name": "Từ 20 - dưới 30 tuổi", "value": 0},
            {"name": "Từ 30 - dưới 40 tuổi", "value": 0},
            {"name": "Từ 40 - dưới 50 tuổi", "value": 0},
            {"name": "Từ 50 - dưới 60 tuổi", "value": 0},
            {"name": "Từ 60 trở lên", "value": 0},
        ]
        data_result = {
            "chart_gender": data_gender,
            "chart_FAVC": data_FAVC,
            "chart_NCP": data_NCP,
            "chart_FHWO": data_FHWO,
            "chart_CAEC": data_CAEC,
            "chart_CH2O": data_CH2O,
            "chart_SMOKE": data_SMOKE,
            "chart_FCVC": data_FCVC,
            "chart_SCC": data_SCC,
            "chart_FAF": data_FAF,
            "chart_TUE": data_TUE,
            "chart_CALC": data_CALC,
            "chart_MTRANS": data_MTRANS,
            "chart_age": data_age,
            "chart_obesity": data_NObeyesdad,
        }
        # data_result = json.dumps(data_result)
        return data_result
    except:
        print("[Error] (getDataModels function app.py)")
        return "[Error] BAD REQUEST can't get datamodel"


# -##############################################################################################


@app.route("/upload-file-url", methods=["POST"])
# @cross_origin()
def upload_file_url():
    try:
        #   Get file
        url = request.args.get("urlData")
        data_name = request.args.get("dataName")
        separator = request.args.get("separator")
        if data_name == "":
            data_name = "dataset_not_name"
        user_id = request.args.get("userId")
    except AttributeError:
        print("[error] can't find file_upload (upfile function app.py)")
        pass
    try:
        #   Create random id
        random_id = str(uuid.uuid4())[:8]
        #   Random file_name
        filename_upload_random = str(random_id) + "_" + "upload.csv"
        #   get file_path
        if os.path.exists(app.config["UPLOAD_FOLDER"]):
            file_path_upload = os.path.join(
                app.config["UPLOAD_FOLDER"], filename_upload_random
            )
        else:
            os.makedirs(app.config["UPLOAD_FOLDER"])
            file_path_upload = os.path.join(
                app.config["UPLOAD_FOLDER"], filename_upload_random
            )
        #   save file
        # Save file locally
        a = urlretrieve(url, file_path_upload)
        # Read file into a DataFrame and print its head
    except UnboundLocalError:
        print(
            "[error] local variable 'filename' referenced before assignment (upfile function app.py)"
        )
        pass
    except ValueError:
        data_return_err = {"error": "unknown url"}
        return data_return_err
    try:
        data, col, n, m = DATA.read("csv", file_path_upload, separator)
        file_name_csv = data_name + ".csv"
        file_path_save_csv = os.path.join(app.config["UPLOAD_FOLDER"], file_name_csv)
        export_csv = data.to_csv(file_path_save_csv, index=None, header=True)
        data_str = DATA.convert_str(file_path_save_csv)
        data_str = str(data_str)
        data_post = {
            "jsonData": data_str,
            "dataName": data_name,
            "userUpload": {
                "__type": "Pointer",
                "className": "_User",
                "objectId": user_id,
            },
            "delimiter": separator,
            "uploadFrom": "url",
        }
        class_name = "Data"
        data = API.post(class_name, data_post)
        print(data)
        return data
    except UnboundLocalError:
        print("[error] ")
        return "fail, can't upload dataset"


@app.route("/get-columns-form", methods=["GET"])
@cross_origin()
def get_columns_form():
    try:
        class_name = request.args.get("className")
        if class_name == "DatasetSurveyBalance":
            r = API.get_class(class_name)
            arr = str(r.data, "utf-8")
            r_json = json.loads(arr)
            data_create_model = pd.DataFrame(r_json["results"])
            index_columns = data_create_model.columns[3:]
            list_index = list(index_columns)
            array_index_json = json.dumps(list_index)
            return array_index_json
        elif class_name == "DatasetObesity":
            r = API.get_class(class_name)
            arr = str(r.data, "utf-8")
            r_json = json.loads(arr)
            data_create_model = pd.DataFrame(r_json["results"])
            index_columns = data_create_model.columns[3:]
            list_index = list(index_columns)
            array_index_json = json.dumps(list_index)
            return array_index_json

    except:
        print("[Error] (getColumnsFrom function app.py)")
        return "[Error] BAD REQUEST can't det columns form"


@app.route("/get-data", methods=["GET"])
@cross_origin()
def get_data():
    try:
        userId = request.args.get("userId")
        className = "Data"
        r = API.get_data_user("Data", userId)
        data = r.data
        return r.data
    except:
        print("[Error] (getData function app.py)")
        return "[Error] BAD REQUEST can't get data"


@app.route("/get-data-models", methods=["GET"])
@cross_origin()
def get_data_models():
    try:
        user_id = request.args.get("userId")
        class_name = "Model"
        r = API.get_model_user(class_name)
        return r
    except:
        print("[Error] (getDataModels function app.py)")
        return "[Error] BAD REQUEST can't get datamodel"


@app.route("/check-data-delete", methods=["GET"])
# @cross_origin()
def check_data_delete():
    try:
        className = request.args.get("className")
        object_id_delete = request.args.get("dataId")
        r = API.check_data(className, object_id_delete)
        return r
    except:
        print("[Error] (getAlgorithm function app.py)")
        return "[Error] BAD REQUEST can't get algorithm"


@app.route("/get-algorithm", methods=["GET"])
# @cross_origin()
def get_algorithm():
    try:
        class_name = request.args.get("className")
        r = API.get_class(class_name)
        return r.data
    except:
        print("[Error] (getAlgorithm function app.py)")
        return "[Error] BAD REQUEST can't get algorithm"


@app.route("/get-params", methods=["GET"])
# @cross_origin()
def get_params():
    try:
        className = request.args.get("className")
        r = API.get_class(className)
        return r
    except:
        print("[Error] (getParams function app.py)")
        return "[Error] BAD REQUEST can't get params"


@app.route("/delete-data", methods=["POST"])
@cross_origin()
def delete_data():
    try:
        object_id = request.args.get("oId")
        class_id = "Data"
        data = API.delete_data(class_id, object_id)
        return data
    except:
        print("[Error] (delete function app.py)")
        return "[Error] BAD REQUEST can't delete dataset"


@app.route("/delete-data-model", methods=["POST"])
@cross_origin()
def delete_data_model():
    try:
        object_id = request.args.getlist("oId")[0]
        className = request.args.getlist("class")[0]
        class_id = className
        data = API.delete_object(class_id, object_id)
        return data
    except:
        print("[Error] (deleteDataModel function app.py)")
        return "[Error] BAD REQUEST can't delete model"


@app.route("/register", methods=["POST", "GET"])
# @cross_origin()
def register():
    try:
        userName = request.args.get("userName")
        password = request.args.get("password")
        email = request.args.get("email")
        data_info = {"username": userName, "password": password, "email": email}
        signing_info = API.signing_up(data_info)
        # object_id = signing_info['objectId']
        # time = signing_info['CreatedAt']
        # session_token = signing_info['sessionToken']
        return signing_info
    except:
        print("[Error] (Register function app.py)")
        return "[Error] BAD REQUEST can't Register"


@app.route("/linking-users", methods=["POST", "GET"])
# @cross_origin()
def linking_users():
    try:
        login_info_auth = {"username": "36195438", "password": "khuong"}
        login_user_info = API.user_login(login_info_auth)
        login_user_info.sessiontoken
        return str(login_user_info)
    except:
        print("[Error] (Linking_Users function app.py)")
        return "[Error] BAD REQUEST can't Linking_Users"


@app.route("/create-model", methods=["POST"])
# @cross_origin()
def create_model():
    try:
        # Get opjectId, collabel, feature, algorithm and parameters
        data_name = request.args.get("dataName")
        class_name = request.args.get("className")
        model_name = request.args.get("modelname")
        col_label = int(request.args.get("label"))
        col_feature_str = (request.args.get("feature")).split(",")
        col_feature = []
        for col in col_feature_str:
            col_feature.append(int(col))
        athm = request.args.get("algorithm")
        athm_id = request.args.get("algorithmId")
        params = json.loads(request.args.get("params"))
        # print(params)
        if params == {}:
            params = None
            test_size = 0.3
        else:
            test_size = float(params["testSize"])
            if test_size >= 1.0 or test_size <= 0.0:
                data = {"error": "0.0 < test size < 1.0"}
                return data
        # get data
        r = API.get_class(class_name)
        arr = str(r.data, "utf-8")
        r_json = json.loads(arr)
        data = r_json["results"]
        dataFrame = pd.DataFrame(data)
        if class_name == "DatasetSurveyBalance":
            dataFrame = dataFrame.iloc[:, 3:]
        elif class_name == "DatasetObesity":
            dataFrame = dataFrame.iloc[:, 3:]
        if "yearOfBirth" in list(dataFrame.columns):
            del dataFrame["yearOfBirth"]
        # dataFrame = dataFrame.dropna(axis="1",how = "any")
        col_feature_name = np.array((dataFrame.iloc[:, col_feature]).columns)
        col_feature_name_str = col_feature_name[0]
        col_feature_name = list(col_feature_name)
        col_feature_name.pop(0)
        col_feature_name = np.array(col_feature_name)
        for col in col_feature_name:
            col_feature_name_str = col_feature_name_str + "," + col
        col_label_name = str(
            np.array(pd.DataFrame(np.matrix(dataFrame.columns)).iloc[0, col_label])
        )
        # get data train, test
        X_train, X_test, y_train, y_test = DATA.get_data_train(
            dataFrame, col_feature, col_label, test_size
        )
        model, evalution, error, params = get_athm(
            athm, X_train, X_test, y_train, y_test, params
        )
        if error != "":
            data = {"error": error}
            return data
        else:
            #   Create random id for file name
            folder_model = "./upload_model"
            randomId = str(uuid.uuid4())[:8]
            file_name_model = (
                randomId + "_" + str(athm) + "_" + str(class_name) + str(".pkl")
            )
            pkl_filename = folder_model + "/" + file_name_model
            joblib.dump(model, str(file_name_model))
            custom_header = {}
            custom_header["X-Parse-Application-Id"] = API.X_Parse_Application_Id
            custom_header["X-Parse-REST-API-Key"] = API.X_Parse_REST_API_Key
            custom_header["Content-Type"] = "application/x-binary"
            desription = description = (
                "Model "
                + " use "
                + str(athm)
                + " algorithm "
                + ". "
                + "Dataset for model is "
                + str(data_name)
                + ", columns label is "
                + str(col_label_name)
                + " and columns feature is "
                + str(col_feature_name)
            )
            r_upload = API.upload_model_file(
                file_name_model,
                model_name,
                data_name,
                athm_id,
                params,
                col_label,
                col_label_name,
                col_feature,
                col_feature_name_str,
                description,
                evalution,
            )
            return r_upload
    except:
        print("[error] (createModel function app.py)")
        data = {"error": "can't create model"}
        return data


@app.route("/download-dataset", methods=["GET"])
# @cross_origin()
def download_dataset():
    try:
        # Get opjectId, collabel, feature, algorithm and parameters
        data_id = request.args.get("dataId")
        class_name = request.args.get("className")
        r = API.get_data_create_model(class_name, data_id)
        file_name = str(uuid.uuid4())[:8] + "_data.csv"
        data_json = json.loads(r["jsonData"])
        dataFrame = pd.DataFrame(data_json)
        dataFrame = DATA.check_columns_name(dataFrame)
        if os.path.exists(app.config["DOWNLOAD_FOLDER"]):
            file_path_download = os.path.join(app.config["DOWNLOAD_FOLDER"], file_name)
        else:
            os.makedirs(app.config["DOWNLOAD_FOLDER"])
            file_path_download = os.path.join(app.config["DOWNLOAD_FOLDER"], file_name)
        # file_path = "./temp/" + file_name
        # file_path_download = "./temp/" + file_name
        export_csv = dataFrame.to_csv(file_path_download, index=None, header=True)
        return send_file(
            file_path_download,
            mimetype="test/csv",
            attachment_filename="data.csv",
            as_attachment=True,
        )
    except Exception as ex:
        print("[error] (createModel function app.py)")
        data = {"error": "can't  download data"}
        print(ex)
        return data


@app.route("/model-publish-api", methods=["GET", "POST"])
# @cross_origin()
def create_api_model():
    # try:
    if request.headers["CONTENT_TYPE"] == "application/json":
        try:
            data_request = request.json
            modelId = data_request["modelId"]
            if modelId == None:
                return "[error] modelId not found check (keys) modelId and values "
            else:
                data_test_json = data_request["data"]
                data_test_dataFrame = pd.DataFrame(data_test_json)
                r = API.get_model("Model", modelId)
                modelUrl = r["modelFile"]["url"]
                Nu_SVC_classifier = joblib.load(urlopen(modelUrl))
                KQ = np.array(Nu_SVC_classifier.predict(data_test_dataFrame))
                dataReturn = {
                    "result": [],
                }
                for rs in KQ:
                    dataReturn["result"].append(str(rs))
                return dataReturn
        except:
            print("[error] check key (inputColumns) and value")
            return (
                "[error] check key (inputColumns) and value (check type inputColumns)"
            )
            pass
    else:
        modelId = request.form.get("modelId")
        if modelId == None:
            return "[error] modelId not found check (keys) modelId and values "
        else:
            file_test = request.files.getlist("data")[0]
            file_name = secure_filename(file_test.filename)
            if file_name == "":
                return "[error] Can't find data, check keys 'data' and values"
            else:
                try:
                    filename_random = str(uuid.uuid4())[:8] + "_" + file_name
                    if os.path.exists(app.config["DATA_API_FOLDER"]):
                        file_path_test = os.path.join(
                            app.config["DATA_API_FOLDER"], filename_random
                        )
                    else:
                        os.makedirs(app.config["DATA_API_FOLDER"])
                        file_path_test = os.path.join(
                            app.config["DATA_API_FOLDER"], filename_random
                        )
                    file_test.save(file_path_test)
                    df_test, columns, n, m = DATA.read("csv", file_path_test, ",")
                except Exception as e:
                    print(e)
                    return "[error] can't save data, request fail"
                    pass
                try:
                    col_feature_test_string = request.form.getlist("inputColumns")[0]
                    col_feature_test_list = ast.literal_eval(col_feature_test_string)
                    col_feature_test_array = np.array(col_feature_test_list)
                    r = API.get_model("Model", modelId)
                    modelUrl = r["modelFile"]["url"]
                    Nu_SVC_classifier = joblib.load(urlopen(modelUrl))
                except:
                    print("[error] request fail")
                    notification = (
                        "[error] request fail check key 'modelId', model "
                        + str(modelId)
                        + " not found"
                    )
                    return notification
                    pass
                try:
                    data_test = df_test.iloc[:, col_feature_test_array]
                    KQ = np.array(Nu_SVC_classifier.predict(data_test))
                    dataReturn = {
                        "result": [],
                    }
                    for rs in KQ:
                        dataReturn["result"].append(str(rs))
                    os.remove(file_path_test)
                    return dataReturn
                except IndexError:
                    print("[error] check key (inputColumns) and value")
                    return "[error] check key (inputColumns) and value check (number inputColumns)"
                    pass
                except ValueError:
                    print("[error] check key (inputColumns) and value")
                    return "[error] check key (inputColumns) and value (check type inputColumns)"
                    pass


@app.route("/load-model", methods=["GET"])
# @cross_origin()
def load_model():
    try:
        model_id = request.args.get("modelId")
        new_record = request.args.get("record")
        new_record = new_record.split(",")
        df_new_record = pd.DataFrame([new_record])
        if model_id == None:
            return "[error] modelId not found check (keys) modelId and values"
        else:
            r = API.get_model("Model", model_id)
            modelUrl = r["modelFile"]["url"]
            Nu_SVC_classifier = joblib.load(urlopen(modelUrl))
            data_transform = {
                "0": "Thiếu cân (Insufficient weight)",
                "1": "Bình thường (Normal weight)",
                "2": "Thừa cân loại 1 (Overweight level 1)",
                "3": "Thừa cân loại 2 (Overweight level 2)",
                "4": "Béo phì loại 1 (Obesity type I)",
                "5": "Béo phì loại 2 (Obesity type II)",
                "6": "Béo phì loại 3 (Obesity type III)",
            }
            KQ = np.array(Nu_SVC_classifier.predict(df_new_record))
            dataReturn = {
                "dataPredict": [],
            }
            for rs in KQ:
                dataReturn["dataPredict"].append(data_transform[str(rs)])
            return dataReturn
    except:
        print("[error] check key (inputColumns) and value")
        return "[error] check key (inputColumns) and value (check type inputColumns)"
        pass


@app.route("/add-record-obesity", methods=["POST"])
# @cross_origin()
def add_record_obesity():
    try:
        new_record = request.args.get("record")
        new_record = new_record.split(",")
        class_name = request.args.get("className")
        class_name_raw = request.args.get("classNameRaw")
        data_tf_obesity = {
            "0": "Insufficient_Weight",
            "1": "Normal_Weight",
            "2": "Overweight_Level_I",
            "3": "Overweight_Level_II",
            "4": "Obesity_Type_I",
            "5": "Obesity_Type_II",
            "6": "Obesity_Type_III",
        }
        data_tf_gender = {"0": "Female", "1": "Male"}
        data_tf_FHWO = {"0": "no", "1": "yes"}
        data_tf_FAVC = {"0": "no", "1": "yes"}
        data_tf_CAEC = {"0": "no", "1": "Sometimes", "2": "Frequently", "3": "Always"}
        data_tf_CALC = {"0": "no", "1": "Sometimes", "2": "Frequently", "3": "Always"}
        data_tf_SMOKE = {"0": "no", "1": "yes"}
        data_tf_SCC = {"0": "no", "1": "yes"}
        data_tf_MTRANS = {
            "0": "Public_Transportation",
            "1": "Automobile",
            "2": "Walking",
            "3": "Motorbike",
            "4": "Bike",
        }
        df_new_record = pd.DataFrame([new_record])
        df_new_record.columns = [
            "GENDER",
            "HEIGHT",
            "FAVC",
            "AGE",
            "NCP",
            "FHWO",
            "CAEC",
            "CH2O",
            "SMOKE",
            "FCVC",
            "SCC",
            "FAF",
            "TUE",
            "CALC",
            "MTRANS",
            "WEIGHT",
            "CLASS_OB",
        ]
        for i in range(len(df_new_record)):
            data_post_raw = {
                "gender": str(data_tf_gender[str(df_new_record["GENDER"][i])]),
                "age": float(df_new_record["AGE"][i]),
                "height": float(df_new_record["HEIGHT"][i]),
                "weight": float(df_new_record["WEIGHT"][i]),
                "FHWO": str(data_tf_FHWO[str(df_new_record["FHWO"][i])]),
                "FAVC": str(data_tf_FAVC[str(df_new_record["FAVC"][i])]),
                "FCVC": float(df_new_record["FCVC"][i]),
                "NCP": float(df_new_record["NCP"][i]),
                "CAEC": str(data_tf_CAEC[str(df_new_record["CAEC"][i])]),
                "SMOKE": str(data_tf_SMOKE[str(df_new_record["SMOKE"][i])]),
                "CH2O": float(df_new_record["CH2O"][i]),
                "SCC": str(data_tf_SCC[str(df_new_record["SCC"][i])]),
                "FAF": float(df_new_record["FAF"][i]),
                "TUE": float(df_new_record["TUE"][i]),
                "CALC": str(data_tf_CALC[str(df_new_record["CALC"][i])]),
                "MTRANS": str(data_tf_MTRANS[str(df_new_record["MTRANS"][i])]),
                "NObeyesdad": str(data_tf_obesity[str(df_new_record["CLASS_OB"][i])]),
            }
            data_post = {
                "gender": float(df_new_record["GENDER"][i]),
                "age": float(df_new_record["AGE"][i]),
                "height": float(df_new_record["HEIGHT"][i]),
                "weight": float(df_new_record["WEIGHT"][i]),
                "FHWO": float(df_new_record["FHWO"][i]),
                "FAVC": float(df_new_record["FAVC"][i]),
                "FCVC": float(df_new_record["FCVC"][i]),
                "NCP": float(df_new_record["NCP"][i]),
                "CAEC": float(df_new_record["CAEC"][i]),
                "SMOKE": float(df_new_record["SMOKE"][i]),
                "CH2O": float(df_new_record["CH2O"][i]),
                "SCC": float(df_new_record["SCC"][i]),
                "FAF": float(df_new_record["FAF"][i]),
                "TUE": float(df_new_record["TUE"][i]),
                "CALC": float(df_new_record["CALC"][i]),
                "MTRANS": float(df_new_record["MTRANS"][i]),
                "NObeyesdad": float(df_new_record["CLASS_OB"][i]),
            }
            data_raw = API.post(class_name_raw, data_post_raw)
            data = API.post(class_name, data_post)
            return str(postok)
    except:
        print("[error] check key (inputColumns) and value")
        return "[error] check key (inputColumns) and value (check type inputColumns)"
        pass


@app.route("/get-model-detail", methods=["GET"])
# @cross_origin()
def get_model_detail():
    try:
        modelId = request.args.get("modelId")
        r = API.get_model_detail("ModelDetail", modelId)
        if r == False:
            data = {
                "error": "[error] request fail, model " + str(modelId) + " not found"
            }
            return data
        else:
            data = r["results"][0]
            return data
    except:
        print("[Error] (useModel function app.py)")
        return "[Error] BAD REQUEST can't get model detail"


if __name__ == "__main__":
    app.run()
