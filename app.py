# server/app.py
from flask import template_rendered, render_template, request, jsonify, current_app, send_from_directory, send_file, safe_join
from flask import Flask
from flask_cors import cross_origin
from flask_cors import CORS
from data import DATA
from werkzeug.utils import secure_filename
from urllib.request import urlretrieve
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
from linear_regression_tool import linear_regression_algorithm


UPLOAD_FOLDER = './upload_temp'
DOWNLOAD_FOLDER = './download_temp'
DATA_API_FOLDER = './data_api'

app = Flask(__name__, static_folder="../front/dist/front", static_url_path="")
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['DATA_API_FOLDER'] = DATA_API_FOLDER


@app.route('/', methods=['POST', 'get'])
def home():
    return ("Server python [5000]")


@app.route('/upload-file', methods=['POST'])
# @cross_origin()
def upload_file():
    try:
        #   Get file
        file_upload = None
        file_upload = request.files.getlist('fileUploaded')[0]
        data_name = request.form.get('dataName')
        separator = request.form.get('separator')
        file_tail = request.form.get('fileTail')
        # file_upload = request.files.get('fileUploaded')
        # print(file)
        uId = request.form.getlist('userId')[0]
        # uId = request.form.getlist('userId')
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
        if(os.path.exists(app.config['UPLOAD_FOLDER'])):
            file_path_upload = os.path.join(
                app.config['UPLOAD_FOLDER'], filename_upload_random)
        else:
            os.makedirs(app.config['UPLOAD_FOLDER'])
            file_path_upload = os.path.join(
                app.config['UPLOAD_FOLDER'], filename_upload_random)
        #   save file
        file_upload.save(file_path_upload)
        if(data_name == ""):
            data_name_upload = filename
        else:
            data_name_upload = data_name
    except UnboundLocalError:
        print("[error] local variable 'filename' referenced before assignment (upfile function app.py)")
        pass
    try:
        data, col, n, m = DATA.read("csv", file_path_upload, separator)
        data_str = DATA.convert_str(file_path_upload)
        data_str = str(data_str)
        print(data_str)
        data_post = {
            "jsonData": data_str,
            "dataName": data_name_upload,
            "userUpload": {
                "__type": "Pointer",
                "className": "_User",
                "objectId": uId
            },
            "delimiter": separator,
            "uploadFrom": "folder"
        }
        class_name = "Data"
        data = API.post(class_name, data_post)
        return (data)
    except UnboundLocalError:
        print("[error] ")
        return ("fail, can't upload dataset")


@app.route('/upload-file-url', methods=['POST'])
# @cross_origin()
def upload_file_url():
    try:
        #   Get file
        url = request.args.get('urlData')
        data_name = request.args.get('dataName')
        separator = request.args.get('separator')
        if(data_name == ""):
            data_name = "dataset_not_name"
        user_id = request.args.get('userId')
    except AttributeError:
        print("[error] can't find file_upload (upfile function app.py)")
        pass
    try:
        #   Create random id
        random_id = str(uuid.uuid4())[:8]
        #   Random file_name
        filename_upload_random = str(
            random_id) + "_" + "upload.csv"
        #   get file_path
        if(os.path.exists(app.config['UPLOAD_FOLDER'])):
            file_path_upload = os.path.join(
                app.config['UPLOAD_FOLDER'], filename_upload_random)
        else:
            os.makedirs(app.config['UPLOAD_FOLDER'])
            file_path_upload = os.path.join(
                app.config['UPLOAD_FOLDER'], filename_upload_random)
        #   save file
        # Save file locally
        a = urlretrieve(url, file_path_upload)
        # Read file into a DataFrame and print its head
    except UnboundLocalError:
        print("[error] local variable 'filename' referenced before assignment (upfile function app.py)")
        pass
    except ValueError:
        data_return_err = {
            "error": "unknown url"
        }
        return (data_return_err)
    try:
        data, col, n, m = DATA.read("csv", file_path_upload, separator)
        file_name_csv = data_name + ".csv"
        file_path_save_csv = os.path.join(
            app.config['UPLOAD_FOLDER'], file_name_csv)
        export_csv = data.to_csv(file_path_save_csv, index=None, header=True)
        data_str = DATA.convert_str(file_path_save_csv)
        data_str = str(data_str)
        data_post = {
            "jsonData": data_str,
            "dataName": data_name,
            "userUpload": {
                "__type": "Pointer",
                "className": "_User",
                "objectId": user_id
            },
            "delimiter": separator,
            "uploadFrom": "url"
        }
        class_name = "Data"
        data = API.post(class_name, data_post)
        print(data)
        return (data)
    except UnboundLocalError:
        print("[error] ")
        return ("fail, can't upload dataset")


@app.route('/get-columns-form', methods=['GET'])
@cross_origin()
def get_columns_form():
    try:
        objectId = request.args.get('objectId')
        className = "Data"
        r = API.get_data_create_model(className, objectId)
        # if(r['uploadFrom'] == "url"):
        #     data_json = json.loads(r['jsonData'])
        #     for i in range(len(data_json)):
        #         data_json[i] = data_json[i][0]
        #     data_frame = pd.DataFrame(data_json)
        #     data_after_check = DATA.check_columns_name(data_frame)
        #     index_columns = data_after_check.columns
        #     list_index = list(index_columns)
        #     array_index_json = json.dumps(list_index)
        #     return (array_index_json)
        # else:
        data_json = json.loads(r['jsonData'])
        data_frame = pd.DataFrame(data_json)
        data_after_check = DATA.check_columns_name(data_frame)
        index_columns = data_after_check.columns
        list_index = list(index_columns)
        array_index_json = json.dumps(list_index)
        return (array_index_json)
    except:
        print("[Error] (getColumnsFrom function app.py)")
        return ("[Error] BAD REQUEST can't det columns form")


@app.route('/get-data', methods=['GET'])
@cross_origin()
def get_data():
    try:
        userId = request.args.get('userId')
        className = 'Data'
        r = API.get_data_user("Data", userId)
        data = r.data
        return (r.data)
    except:
        print("[Error] (getData function app.py)")
        return ("[Error] BAD REQUEST can't get data")


@app.route('/get-data-models', methods=['GET'])
@cross_origin()
def get_data_models():
    try:
        user_id = request.args.get('userId')
        class_name = 'Model'
        r = API.get_model_user(class_name, user_id)
        return (r)
    except:
        print("[Error] (getDataModels function app.py)")
        return ("[Error] BAD REQUEST can't get datamodel")


@app.route('/check-data-delete', methods=['GET'])
# @cross_origin()
def check_data_delete():
    try:
        className = request.args.get('className')
        object_id_delete = request.args.get('dataId')
        r = API.check_data(className, object_id_delete)
        return (r)
    except:
        print("[Error] (getAlgorithm function app.py)")
        return ("[Error] BAD REQUEST can't get algorithm")


@app.route('/get-algorithm', methods=['GET'])
# @cross_origin()
def get_algorithm():
    try:
        className = request.args.get('className')
        r = API.get_class(className)
        return (r)
    except:
        print("[Error] (getAlgorithm function app.py)")
        return ("[Error] BAD REQUEST can't get algorithm")


@app.route('/get-params', methods=['GET'])
# @cross_origin()
def get_params():
    try:
        className = request.args.get('className')
        r = API.get_class(className)
        return (r)
    except:
        print("[Error] (getParams function app.py)")
        return ("[Error] BAD REQUEST can't get params")


@app.route('/delete-data', methods=['POST'])
@cross_origin()
def delete_data():
    try:
        object_id = request.args.get('oId')
        class_id = "Data"
        data = API.delete_data(class_id, object_id)
        return (data)
    except:
        print("[Error] (delete function app.py)")
        return ("[Error] BAD REQUEST can't delete dataset")


@app.route('/delete-data-model', methods=['POST'])
@cross_origin()
def delete_data_model():
    try:
        object_id = request.args.getlist('oId')[0]
        className = request.args.getlist('class')[0]
        class_id = className
        data = API.delete_object(class_id, object_id)
        return (data)
    except:
        print("[Error] (deleteDataModel function app.py)")
        return ("[Error] BAD REQUEST can't delete model")


@app.route('/register', methods=['POST', 'GET'])
# @cross_origin()
def register():
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
        print("[Error] (Register function app.py)")
        return ("[Error] BAD REQUEST can't Register")


@app.route('/linking-users', methods=['POST', 'GET'])
# @cross_origin()
def linking_users():
    try:
        login_info_auth = {
            "username": "36195438",
            "password": "khuong"
        }
        login_user_info = API.user_login(login_info_auth)
        login_user_info.sessiontoken
        return (str(login_user_info))
    except:
        print("[Error] (Linking_Users function app.py)")
        return ("[Error] BAD REQUEST can't Linking_Users")


@app.route('/create-model', methods=['POST'])
# @cross_origin()
def create_model():
    try:
        # Get opjectId, collabel, feature, algorithm and parameters
        data_id = request.args.get('dataId')
        user_id = request.args.get('userId')
        class_name = request.args.get('className')
        model_name = request.args.get('modelname')
        col_label = int(request.args.get('label'))
        col_feature_str = (request.args.get('feature')).split(',')
        col_feature = []
        for col in col_feature_str:
            col_feature.append(int(col))
        athm = request.args.get('algorithm')
        athm_id = request.args.get('algorithmId')
        params = json.loads(request.args.get('params'))
        # print(params)
        if(params == {}):
            params = None
            test_size = 0.3
        else:
            test_size = float(params['testSize'])
            if (test_size >= 1.0 or test_size <= 0.0):
                data = {'error': "0.0 < test size < 1.0"}
                return (data)
        # get data
        r = API.get_data_create_model(class_name, data_id)
        data_name = r['dataName']
        data_json = json.loads(r['jsonData'])
        dataFrame = pd.DataFrame(data_json)
        dataFrame = DATA.check_columns_name(dataFrame)
        for col in col_feature:
            dataFrame = dataFrame.drop(
                dataFrame[(dataFrame.iloc[:, col] == "")].index)
        # dataFrame = dataFrame.dropna(axis="1",how = "any")
        col_feature_name = (np.array(pd.DataFrame(
            np.matrix(dataFrame.columns)).iloc[0, col_feature]))
        col_feature_name_str = col_feature_name[0]
        col_feature_name = list(col_feature_name)
        col_feature_name.pop(0)
        col_feature_name = np.array(col_feature_name)
        for col in (col_feature_name):
            col_feature_name_str = col_feature_name_str + "," + col
        col_label_name = str(np.array(pd.DataFrame(
            np.matrix(dataFrame.columns)).iloc[0, col_label]))
        # get data train, test
        X_train, X_test, y_train, y_test = DATA.get_data_train(
            dataFrame, col_feature, col_label, test_size)
        model, evalution, error, params = get_athm(
            athm, X_train, X_test, y_train, y_test, params)
        if(error != ""):
            data = {
                'error': error
            }
            return data
        else:
            #   Create random id for file name
            folder_model = "./upload_model"
            randomId = str(uuid.uuid4())[:8]
            file_name_model = randomId + "_" + \
                str(athm) + "_" + str(data_id) + str(".pkl")
            pkl_filename = folder_model + "/" + file_name_model
            joblib.dump(model, str(file_name_model))
            custom_header = {}
            custom_header['X-Parse-Application-Id'] = API.X_Parse_Application_Id
            custom_header['X-Parse-REST-API-Key'] = API.X_Parse_REST_API_Key
            custom_header['Content-Type'] = "application/x-binary"
            desription = description = "Model " + " use " + str(athm) + " algorithm " + ". " + "Dataset for model is " + str(
                data_name) + ", columns label is " + str(col_label_name) + " and columns feature is " + str(col_feature_name)
            r_upload = API.upload_model_file(file_name_model, user_id, model_name, data_id,
                                             athm_id, params, col_label, col_label_name, col_feature, col_feature_name_str, description, evalution)
            return (r_upload)
    except:
        print("[error] (createModel function app.py)")
        data = {
            'error': "can't create model"
        }
        return (data)


@app.route('/download-dataset', methods=['GET'])
# @cross_origin()
def download_dataset():
    try:
        # Get opjectId, collabel, feature, algorithm and parameters
        data_id = request.args.get('dataId')
        class_name = request.args.get('className')
        r = API.get_data_create_model(class_name, data_id)
        file_name = str(uuid.uuid4())[:8] + "_data.csv"
        data_json = json.loads(r['jsonData'])
        dataFrame = pd.DataFrame(data_json)
        dataFrame = DATA.check_columns_name(dataFrame)
        if(os.path.exists(app.config['DOWNLOAD_FOLDER'])):
            file_path_download = os.path.join(
                app.config['DOWNLOAD_FOLDER'], file_name)
        else:
            os.makedirs(app.config['DOWNLOAD_FOLDER'])
            file_path_download = os.path.join(
                app.config['DOWNLOAD_FOLDER'], file_name)
        # file_path = "./temp/" + file_name
        # file_path_download = "./temp/" + file_name
        export_csv = dataFrame.to_csv(
            file_path_download, index=None, header=True)
        return send_file(file_path_download,
                         mimetype='test/csv',
                         attachment_filename="data.csv",
                         as_attachment=True)
    except Exception as ex:
        print("[error] (createModel function app.py)")
        data = {
            'error': "can't  download data"
        }
        print(ex)
        return (data)


@app.route('/model-publish-api', methods=['GET', 'POST'])
# @cross_origin()
def create_api_model():
    # try:
    if (request.headers['CONTENT_TYPE'] == "application/json"):
        try:
            data_request = request.json
            modelId = data_request['modelId']
            if(modelId == None):
                return("[error] modelId not found check (keys) modelId and values ")
            else:
                data_test_json = data_request['data']
                data_test_dataFrame = pd.DataFrame(data_test_json)
                r = API.get_model("Model", modelId)
                modelUrl = r['modelFile']['url']
                Nu_SVC_classifier = joblib.load(urlopen(modelUrl))
                KQ = np.array(Nu_SVC_classifier.predict(data_test_dataFrame))
                dataReturn = {
                    "result": [],
                }
                for rs in KQ:
                    dataReturn['result'].append(str(rs))
                return(dataReturn)
        except:
            print("[error] check key (inputColumns) and value")
            return("[error] check key (inputColumns) and value (check type inputColumns)")
            pass
    else:
        modelId = request.form.get('modelId')
        if(modelId == None):
            return("[error] modelId not found check (keys) modelId and values ")
        else:
            file_test = request.files.getlist('data')[0]
            file_name = secure_filename(file_test.filename)
            if(file_name == ""):
                return ("[error] Can't find data, check keys 'data' and values")
            else:
                try:
                    filename_random = str(uuid.uuid4())[:8] + "_" + file_name
                    if(os.path.exists(app.config['DATA_API_FOLDER'])):
                        file_path_test = os.path.join(
                            app.config['DATA_API_FOLDER'], filename_random)
                    else:
                        os.makedirs(app.config['DATA_API_FOLDER'])
                        file_path_test = os.path.join(
                            app.config['DATA_API_FOLDER'], filename_random)
                    file_test.save(file_path_test)
                    df_test, columns, n, m = DATA.read(
                        "csv", file_path_test, ",")
                except Exception as e:
                    print(e)
                    return("[error] can't save data, request fail")
                    pass
                try:
                    col_feature_test_string = request.form.getlist('inputColumns')[
                        0]
                    col_feature_test_list = ast.literal_eval(
                        col_feature_test_string)
                    col_feature_test_array = np.array(col_feature_test_list)
                    r = API.get_model("Model", modelId)
                    modelUrl = r['modelFile']['url']
                    Nu_SVC_classifier = joblib.load(urlopen(modelUrl))
                except:
                    print("[error] request fail")
                    notification = "[error] request fail check key 'modelId', model " + \
                        str(modelId) + " not found"
                    return(notification)
                    pass
                try:
                    data_test = df_test.iloc[:, col_feature_test_array]
                    KQ = np.array(Nu_SVC_classifier.predict(data_test))
                    dataReturn = {
                        "result": [],
                    }
                    for rs in KQ:
                        dataReturn['result'].append(str(rs))
                    os.remove(file_path_test)
                    return(dataReturn)
                except IndexError:
                    print("[error] check key (inputColumns) and value")
                    return("[error] check key (inputColumns) and value check (number inputColumns)")
                    pass
                except ValueError:
                    print("[error] check key (inputColumns) and value")
                    return("[error] check key (inputColumns) and value (check type inputColumns)")
                    pass

# @ app.route('/create-api-model-jsondata', methods=['POST'])
# # @cross_origin()
# def create_api_model_jsondata():
#     try:
#         data_request = request.json
#         modelId = data_request['modelId']
#         if(modelId == None):
#             return("[error] modelId not found check (keys) modelId and values ")
#         else:
#             data_test_json = data_request['data']
#             data_test_dataFrame = pd.DataFrame(data_test_json)
#             r = API.get_model("Model", modelId)
#             modelUrl = r['modelFile']['url']
#             Nu_SVC_classifier = joblib.load(urlopen(modelUrl))
#             KQ = np.array(Nu_SVC_classifier.predict(data_test_dataFrame))
#             dataReturn = {
#                 "dataPredict": [],
#             }
#             for rs in KQ:
#                 dataReturn['dataPredict'].append(str(rs))
#             # print(type(dataReturn))
#             return(dataReturn)
#     except:
#         print("[error] check key (inputColumns) and value")
#         return("[error] check key (inputColumns) and value (check type inputColumns)")
#         pass


@ app.route('/get-model-detail', methods=['GET'])
# @cross_origin()
def get_model_detail():
    try:
        modelId = request.args.get('modelId')
        r = API.get_model_detail("ModelDetail", modelId)
        if r == False:
            data = {
                "error": "[error] request fail, model " + str(modelId) + " not found"
            }
            return (data)
        else:
            data = r['results'][0]
            return(data)
    except:
        print("[Error] (useModel function app.py)")
        return ("[Error] BAD REQUEST can't get model detail")


if __name__ == '__main__':
    app.run()
