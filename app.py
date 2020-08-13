# server/app.py
from flask import template_rendered, render_template, request, jsonify, current_app, send_from_directory, send_file
from flask import Flask
from flask_cors import cross_origin
from flask_cors import CORS
from data import DATA
from werkzeug.utils import secure_filename
import os
import joblib
from main_algorithm import *
from urllib.request import urlopen
import pickle
import uuid
import httplib2
import urllib3
import json
import csv
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
from linear_regression_tool import linear_regression_algorithm


UPLOAD_FOLDER = './temp'

app = Flask(__name__, static_folder="../front/dist/front", static_url_path="")
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST', 'get'])
def home():
    return ("hello")


@app.route('/upfile', methods=['POST'])
# @cross_origin()
def upfile():
    try:
        #   Get file
        file_upload = None
        # file = request.files.getlist('fileUploaded')[0]
        file_upload = request.files.get('fileUploaded')
        # print(file)
        # uId = request.form.getlist('userId')[0]
        uId = request.form.getlist('userId')
        #   Get file_name
        filename = secure_filename(file_upload.filename)
        filename_json = filename.split(".")[0] + ".json"
    except AttributeError:
        print("[error] can't find file_upload (upfile function app.py)")
        pass
    try:
        #   Create random id
        random_id = str(uuid.uuid4())[:8]
        #   Random file_name
        filename_upload_random = str(
            random_id) + "_" + "upload" + "_" + filename
        filename_json_random = str(random_id) + "_" + \
            "json" + "_" + filename_json
        #   get file_path
        file_path_upload = os.path.join(
            app.config['UPLOAD_FOLDER'], filename_upload_random)
        #   save file
        file_upload.save(file_path_upload)
        file_tail = filename.split(".")[1]
    except UnboundLocalError:
        print("[error] local variable 'filename' referenced before assignment (upfile function app.py)")
        pass
    try:
        data, col, n, m = DATA.read(file_tail, file_path_upload)
        data_str = DATA.convert_str(file_path_upload)
        data_str = str(data_str)
        data_post = {
            "jsonData": data_str,
            "dataName": filename_json_random,
            "userUpload": {
                "__type": "Pointer",
                "className": "_User",
                "objectId": uId
            }
        }
        class_name = "Data"
        data = API.post(class_name, data_post)
        return (data)
    except UnboundLocalError:
        print("[error] ")
        return ("fail, can't upload dataset")


@app.route('/getColumnsFrom', methods=['GET'])
@cross_origin()
def getColumnsFrom():
    try:
        objectId = request.args.get('objectId')
        className = "Data"
        r = API.get_data_createmodel(className, objectId)
        dataJson = json.loads(r['jsonData'])
        dataFrame = pd.DataFrame(dataJson)
        dataAfterCheck = DATA.check_columns_name(dataFrame)
        indexColumns = dataAfterCheck.columns
        listIndex = list(indexColumns)
        arrayIndexJson = json.dumps(listIndex)
        return (arrayIndexJson)
    except:
        print("[Error]")


@app.route('/getData', methods=['GET'])
@cross_origin()
def getData():
    try:
        userId = request.args.get('userId')
        className = 'Data'
        r = API.get_data_user(className, userId)
        return (r)
    except:
        print("[Error]")


@app.route('/getDataModels', methods=['GET'])
@cross_origin()
def getDataModels():
    try:
        userId = request.args.get('userId')
        className = 'Model'
        r = API.get_model_user(className, userId)
        return (r)
    except:
        print("[Error]")


@app.route('/getAlgorithm', methods=['GET'])
# @cross_origin()
def getAlgorithm():
    try:
        className = request.args.get('className')
        r = API.get_class(className)
        return (r)
    except:
        print("[Error]")


@app.route('/getParams', methods=['GET'])
# @cross_origin()
def getParams():
    try:
        className = request.args.get('className')
        r = API.get_class(className)
        return (r)
    except:
        print("[Error]")


@app.route('/deleteData', methods=['POST'])
@cross_origin()
def deleteData():
    try:
        object_id = request.args.getlist('oId')[0]
        class_id = "Data"
        data = API.delete_object(class_id, object_id)
        return (data)
    except:
        print("[Error]")


@app.route('/deleteDataModel', methods=['POST'])
@cross_origin()
def deleteDataModel():
    try:
        object_id = request.args.getlist('oId')[0]
        className = request.args.getlist('class')[0]
        class_id = className
        data = API.delete_object(class_id, object_id)
        return (data)
    except:
        print("[Error]")


@app.route('/Register', methods=['POST', 'GET'])
# @cross_origin()
def Register():
    try:
        userName = request.args.get('userName')
        password = request.args.get('password')
        email = request.args.get('email')
        data_info = {
            "username": userName,
            "password": password,
            "email": email
        }
        signing_info = API.signing_up(data_info)
        # object_id = signing_info['objectId']
        # time = signing_info['CreatedAt']
        # session_token = signing_info['sessionToken']
        return (signing_info)
    except:
        print("[Error]")


@app.route('/Linking_Users', methods=['POST', 'GET'])
# @cross_origin()
def LinkingUsers():
    try:
        login_info_auth = {
            "username": "36195438",
            "password": "khuong"
        }
        login_user_info = API.userLogin(login_info_auth)
        login_user_info.sessiontoken
        return (str(login_user_info))
    except:
        print("[Error]")


@app.route('/createModel', methods=['POST'])
# @cross_origin()
def createModel():
    # Get opjectId, collabel, feature, algorithm and parameters
    object_id = request.args.get('objectId')
    class_name = request.args.get('className')
    col_label = int(request.args.get('label'))
    col_feature_str = (request.args.get('feature')).split(',')
    col_feature = []
    for col in col_feature_str:
        col_feature.append(int(col))
    athm = request.args.get('algorithm')
    params = json.loads(request.args.get('params'))
    # get data
    r = API.get_data_createmodel(class_name, object_id)
    dataJson = json.loads(r['jsonData'])
    dataFrame = pd.DataFrame(dataJson)
    dataFrame = DATA.check_columns_name(dataFrame)
    # get data train, test
    X_train, X_test, y_train, y_test = DATA.get_data_train(
        dataFrame, col_feature, col_label, 0.3)
    model, evalution = get_athm(athm, params, X_train, X_test, y_train, y_test)
    #   Create random id for file name
    folder_model = "./uploadModel"
    randomId = str(uuid.uuid4())[:8]
    file_name_model = randomId + "_" + \
        str(athm) + "_" + str(object_id) + str(".pkl")
    pkl_filename = folder_model + "/" + file_name_model
    joblib.dump(model, str(file_name_model))
    custom_header = {}
    custom_header['X-Parse-Application-Id'] = API.X_Parse_Application_Id
    custom_header['X-Parse-REST-API-Key'] = API.X_Parse_REST_API_Key
    custom_header['Content-Type'] = "application/x-binary"
    r_upload = API.upload_model_file(
        "JclGidZqhN", object_id, file_name_model, custom_header)
    r_json = DATA.convert_bytes_to_json(r_upload)
    model_id = r_json['objectId']
    r_model_detail = API.upload_modeldetail(
        model_id, athm, str(col_feature), str(col_label))
    return (r_upload)


@app.route('/useModel', methods=['GET'])
# @cross_origin()
def useModel():
    try:
        modelId = request.args.get('modelId')
        dataId = request.args.get('dataId')
        modelUrl = request.args.get('modelUrl')
        r_data = API.get_data_createmodel("Data", dataId)
        dataJson = json.loads(r_data['jsonData'])
        dataFrame = pd.DataFrame(dataJson)
        dataFrame = DATA.check_columns_name(dataFrame)
        xtr, xt, ytr, yt = DATA.get_data_train(dataFrame, [0, 1, 2, 3], 4, 0.3)
        Nu_SVC_classifier = joblib.load(urlopen(modelUrl))
        KQ = Nu_SVC_classifier.predict(xt)
        return(KQ)
    except:
        print("[Error]")


@app.route('/detailModel', methods=['GET'])
# @cross_origin()
def detailModel():
    try:
        modelId = request.args.get('modelId')
        r = API.get_model_detail("ModelDetail", modelId)
        data = r['results']
        return(data)
    except:
        print("[Error]")


if __name__ == '__main__':
    app.run()
