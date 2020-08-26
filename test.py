# # import httplib
# import pickle
# import os
# import uuid
# import json
# import httplib2
# import urllib3
# import joblib
# import csv
# from function_api import API
# import json
# from urllib.parse import urlencode
# from data import DATA
# from svm_tool import svm_algorithm
# from randomforest_tool import randomforest_algorithm
# from naive_bayes_tool import naive_bayes_algorithm
# from decisiontree_tool import decision_tree_algorithm
# from linear_regression_tool import linear_regression_algorithm
# from ath_au import *
# df, col, n, m = DATA.read('csv', './temp/iris.csv')


# params = {
#     'n_estimators': 100,
#     'criterion': 'gini',
#     'max_depth': None,
#     'min_samples_split': 2
# }

# algorithm_dict = {
#     "LinearRegression": linear_regression_algorithm.getParams(),
#     "RandomForest": "randomforest_algorithm",
#     "NaiveBayes": "naive_bayes_algorithm",
#     "SupportVectorMachine": "svm_algorithm",
#     "DecisionTree": "decision_tree_algorithm",
# }

# df, col, n, m = DATA.read('csv', './temp/iris.csv')
# xtr, xt, ytr, yt = DATA.get_data_train(df, [0, 1, 2, 3], 4, 0.3)

# clf = get_athm("LinearRegression", params)
# model, evalution = randomforest_algorithm.models("svm", clf, xtr, xt, ytr, yt)


# import httplib


# import httplib


from error import ERROR
from urllib.request import urlopen
import re
import requests as req
import urllib3
from bs4 import BeautifulSoup
import pickle
import os
import uuid
import json
import httplib2
import urllib3
import joblib
import csv
from function_api import API
import json
from urllib.parse import urlencode
from data import DATA
from svm_tool import svm_algorithm
from randomforest_tool import randomforest_algorithm
from naive_bayes_tool import naive_bayes_algorithm
from decisiontree_tool import decision_tree_algorithm
from linear_regression_tool import linear_regression_algorithm
from main_algorithm import *

# params_ln = {
#     'fitIntercept': True,
#     'normalize': True,

# }
# # df, col, n, m = DATA.read('csv', './temp/iris.csv')
# df, col, n, m = DATA.read('csv', './temp/abalone.csv')
# xtr, xt, ytr, yt = DATA.get_data_train(df, [0,1, 2, 3, 4, 5, 6, 7], 8, 0.3)

# clf = get_athm("LinearRegression", params_ln)

# model, evalution = linear_regression_algorithm.models(
#     "regression", clf, xtr, xt, ytr, yt)

#   -----------------------------------------------------------------

# test svm

# params_svm = {
#     "C": 10,
#     "degree": 3,
#     "gamma": 1.2
# }

# df, col, n, m = DATA.read('csv', './temp/iris.csv')
# xtr, xt, ytr, yt = DATA.get_data_train(df, [0, 1, 2, 3], 4, 0.3)

# clf = get_athm("SupportVectorMachine", params_svm)

# model, evalution = svm_algorithm.models(
#     "SupportVectorMachine", clf, xtr, xt, ytr, yt)

#   --------------------------------------------------------------


# test tree

# params_tree = {
#     "criterion": "gini",
#     "maxDepth": "3",
#     "minSamplesSplit": "2",
#     "splitter": "best"
# }

# df, col, n, m = DATA.read('csv', './temp/iris.csv')
# xtr, xt, ytr, yt = DATA.get_data_train(df, [0, 1, 2, 3], 4, 0.3)

# model, evalution = get_athm("DecisionTree", params_tree, xtr, xt, ytr, yt)

# -----------------------------------------------------------------


#   test naive bayes

# params_bayes = {
#     "varSmoothing": "SADa"
# }

# df, col, n, m = DATA.read('csv', './temp/iris.csv')
# xtr, xt, ytr, yt = DATA.get_data_train(df, [0, 1, 2, 3], 4, 0.3)

# model, evalution = get_athm("NaiveBayes", params_bayes, xtr, xt, ytr, yt)

# ---------------------------------------------------------
#   test random forest

# params_forest = {
#     "criterion": "gini",
#     "maxDepth": "3",
#     "minSamples": "2",
#     "nEstimators": "100"
# }

# df, col, n, m = DATA.read('csv', './temp/iris.csv')
# xtr, xt, ytr, yt = DATA.get_data_train(df, [0, 1, 2, 3], 4, 0.3)

# model, evalution = get_athm("RandomForest", params_forest, xtr, xt, ytr, yt)


# header = API.get_header()
# http = API.http
# url = API.url + "classes/" + str("Model") + "?%s"
# param = ({"where": json.dumps({
#     "userUpload": "JclGidZqhN"
# })
# })
# param_encoded = urlencode(param)
# r = http.request('GET', url % param_encoded, headers=header)
# data = DATA.convert_bytes_to_json(r.data)


# http = urllib3.PoolManager()

# df, col, n, m = DATA.read('csv', './temp/iris.csv')
# xtr, xt, ytr, yt = DATA.get_data_train(df, [0, 1, 2, 3], 4, 0.3)

# url = 'http://localhost:1337/parse/files/myAppId/9be587fb3e5cb1e8506ad134a57dd652_02eaf0eb_NaiveBayes_SeS0zIQwZi.pkl'
# response = http.request('GET', url)

# Nu_SVC_classifier = pickle.load(urllib3.PoolManager().urlopen("GET",
#                                                               "http://localhost:1337/parse/files/myAppId/9be587fb3e5cb1e8506ad134a57dd652_02eaf0eb_NaiveBayes_SeS0zIQwZi.pkl"))


# params_forest = {
#     "criterion": "gini",
#     "maxDepth": "3",
#     "minSamples": "2",
#     "nEstimators": "100"
# }
# df, col, n, m = DATA.read('csv', './temp/iris.csv')
# xtr, xt, ytr, yt = DATA.get_data_train(df, [0, 1, 2, 3], 4, 0.3)
# model, evalution = get_athm("RandomForest", params_forest, xtr, xt, ytr, yt)


# pkl_filename = "test_file_3.pkl"
# with open(pkl_filename, 'wb') as file:
#     pickle.dump(model, file)

# data = joblib.load("./kt_test_model.pkl", 'r+')


# with open("./kt_test_model.pkl", 'rb') as p_f:
#     data = pickle.load(p_f)

# with open('./kt_test_model.pkl', 'rb') as fp:
#     binary_data = fp.read()

# header = {
#     'X-Parse-Application-Id': 'myAppId',
#     'X-Parse-REST-API-Key': 'api_key',
#     'Content-Type': 'text/plain'
# }

# http = API.http
# url = "http://localhost:1337/parse/files/test3.pkl"

# r = http.request('POST', url, body=binary_data, headers=header)

# with open("403f5f5968552ed5ffb9f8adacca0912_595d81f3_NaiveBayes_mgFseoltfa.pkl") as p_f:
#     data = pickle.load(p_f)

# data = joblib.load("http://localhost:1337/parse/files/myAppId/403f5f5968552ed5ffb9f8adacca0912_595d81f3_NaiveBayes_mgFseoltfa.pkl", 'r+')

# import os
# os.remove("ChangedFile.csv")


# df, col, n, m = DATA.read('csv', './temp/iris.csv')
# xtr, xt, ytr, yt = DATA.get_data_train(df, [0, 1, 2, 3], 4, 0.3)

# Nu_SVC_classifier = joblib.load(urlopen(
#     "http://localhost:1337/parse/files/myAppId/32c7410331f84d0196fd8ac62f1c0b0b_73e59acd_NaiveBayes_7PzjG47Gql.pkl"))

# header = API.get_header()
# http = API.http
# class_name = "ModelDetail"
# modelId = "ZQzxJXqYvV"
# url = API.url + "classes/ModelDetail?%s"
# param = ({"where": json.dumps({
#     "modelId": modelId,
# })
# })
# # url = API.url + "classes/ModelDetail/Y87e6ZSRGV"
# param_encoded = urlencode(param)
# r = http.request('GET', url % param_encoded, headers=header)


# header = API.get_header()
# http = API.http
# url = API.url + "classes/" + str("Data") + "?%s"
# param = ({"where": json.dumps({
#     "userUpload": "JclGidZqhN"
# })
# })
# param_encoded = urlencode(param)
# r = http.request('GET', url % param_encoded, headers=header)
# data = DATA.convert_bytes_to_json(r.data)
# if data['results'] == []:
#     print(
#         "[error] request fail, check user id, class name (get_data_user function in API class) ")
#     return False
# else:
#     return (data)


# header = API.get_header()
# http = API.http
# url = API.url + "classes/" + str("Data") + "?%s"
# param = ({"where": json.dumps({
#     "userUpload": "JclGidZqhN"
# })
# })
# param_encoded = urlencode(param)
# r = http.request('GET', url % param_encoded, headers=header)

df, columns, n, m = DATA.read("csv", "./file_test/abalone.csv")

xtr, xts, ytr, yts = DATA.get_data_train(df, [0, 2, 3, 4], 8, 0.3)

model, eva = get_athm("LinearRegression", xtr, xts, ytr, yts)

clf = linear_regression_algorithm.getParams()

clf = {
    "errorParams": "fasdfasdf"
}

if(clf['errorParams']):
    print("error")


clf = {
    "asdfasdf": "sadfasdfadf"
}
