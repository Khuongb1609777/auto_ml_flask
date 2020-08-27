# server/app.py
import httplib2
import urllib3
import json
from data import DATA
from urllib.parse import urlencode
import pandas as pd
import joblib
import os


class API:
    url = 'http://localhost:1337/parse/'  # url default
    http = urllib3.PoolManager()
    X_Parse_Application_Id = "myAppId"
    X_Parse_REST_API_Key = "api_key"
    C_Type = "application/json"
    # token = "r:1322d9f4f89476c3634672dc6108a34c"

    #   Create API get_header for user custom, Parse_id, API_key and Content type is default
    def get_header(addition_header=None):
        try:
            header = {}
            header['X-Parse-Application-Id'] = API.X_Parse_Application_Id
            header['X-Parse-REST-API-Key'] = API.X_Parse_REST_API_Key
            header['Content-Type'] = API.C_Type
        except AttributeError:
            print(
                "[error] can't find header in API (get_header function in API class)")
            pass
        # except ValueError:
        #     print("[Error]")
           # header['X-Parse-Session-Token']= API.token
        if (addition_header != None):
            try:
                header.update(addition_header)
            except ValueError:
                print(
                    "[error] can't update header, check header custom (get_header function in API class)")
                pass
        return header

    def get_object_data(class_name, object, addition_header=None):
        data = ""
        try:
            header = API.get_header(addition_header)
            http = API.http
            url = API.url + "classes/" + str(class_name) + "/" + str(object)
        except AttributeError:
            print(
                "[error] can't find header in API (get_object_data function in API class)")
            pass
        try:
            r = http.request('GET', url, headers=header)
            data = DATA.convert_dataframe(r.data)
        except:
            print("[error] can't find data (get_object_data in function API class)")
            pass
        return data
        # except:

    #   Create API get, get all object in class_name
    def get_class(class_name, addition_header=None):
        try:
            header = API.get_header(addition_header)
            http = API.http
            url = API.url + "classes/" + str(class_name)
        except AttributeError:
            print(
                "[error] can't find header in API (get_class function in API class)")
            pass
        try:
            r = http.request('GET', url, headers=header)
            checkRequest = DATA.convert_bytes_to_json(r.data)
            if ('error' in list(checkRequest.keys())):
                print(
                    "[error] Request fail :(( check your request (get_class function in API class)")
                return False
            else:
                return (r.data)
        except:
            print(
                "[Error get_class] can't find r.data, check request (get_class function in API class)")
            pass

    def get_data_create_model(class_name, object_id, addition_header=None):
        try:
            header = API.get_header()
            http = API.http
            url = API.url + "classes/" + str(class_name) + "/" + str(object_id)
        except AttributeError as ex:
            print("AttributeError ", ex)
            print(
                "[error] can't find header in API (get_data_createmodel function in API class)")
            pass
        try:
            r = http.request_encode_url('GET', url, headers=header)
            arr = str(r.data, 'utf-8')
            r_json = json.loads(arr)
            if('error' in list(r_json.keys())):
                print("[error] ", r_json['code'], ", data:",
                      r_json['error'], "--check class_name, objectId (get_data_createmodel function in API class)")
                return False
            else:
                return (r_json)
        except:
            print(
                "[Error get data] check object id (get_data_createmodel function in API class)")
            pass

    def get_data_user(class_name, userId, addition_header=None):
        try:
            header = API.get_header()
            http = API.http
            url = API.url + "classes/" + str("Data") + "?%s"
        except AttributeError:
            print(
                "[error] can't find header in API (get_data_user function in API class)")
            pass
        try:
            param = ({"where": json.dumps({
                "userUpload": str(userId)
            }), 'order': "-createdAt"})
            param_encoded = urlencode(param)
        except:
            print("[error]")
            pass
        try:
            r = http.request('GET', url % param_encoded, headers=header)
            return(r)
        except:
            print(
                "[Error] bad request, check user id, class name (get_data_user function in API class)")
            pass

    def get_model_user(class_name, user_id, addition_header=None):
        try:
            header = API.get_header()
            http = API.http
            url = API.url + "classes/" + str(class_name) + "?%s"
        except AttributeError:
            print(
                "[error] can't find header in API (get_data_user function in API class)")
            pass
        try:
            param = ({"where": json.dumps({
                "createdBy": user_id
            }), 'order': "-createdAt", 'include': '*'})
            param_encoded = urlencode(param)
        except:
            print("[error]")
            pass
        try:
            r = http.request('GET', url % param_encoded, headers=header)
            arr = str(r.data, 'utf-8')
            data = json.loads(arr)
            print(data)
            # print(r.data)
            # data = DATA.convert_bytes_to_json(r.data)
            if data['results'] == []:
                print(
                    "[error] request fail, check user id, class name (get_data_user function in API class) ")
                return False
            else:
                return (data)
        except:
            print(
                "[Error] bad request, check user id, class name (get_data_user function in API class)")
            pass

    #   Create API post, post data.

    def post(class_name, data, addition_header=None):
        try:
            header = API.get_header(addition_header)
            data_encoded = json.dumps(data)
            http = API.http
            url = API.url + "classes/" + str(class_name)
        except AttributeError:
            print(
                "[error] can't find header in API (post function in API class)")
            pass
        try:
            r = http.request('POST', url, body=data_encoded, headers=header)
            checkRequest = DATA.convert_bytes_to_json(r.data)
            if('error' in list(checkRequest.keys())):
                print("[error] ", checkRequest['code'], ", data:",
                      checkRequest['error'], "(post function in API class)")
            else:
                return (r.data)
        except:
            print(
                "[Error] bad request, check user id, class name (post function in API class)")
            pass

    #   Create API delete object
    def delete_object(class_name, object_id, addition_header=None):
        try:
            header = API.get_header(addition_header)
            http = API.http
            url = API.url + "classes/" + str(class_name) + "/" + str(object_id)
        except:
            print(
                "[error] can't find header in API (delete_object function in API class)")
            pass
        try:
            r = http.request('DELETE', url, headers=header)
            checkRequest = DATA.convert_bytes_to_json(r.data)
            if('error' in list(checkRequest.keys())):
                print("[error] ", checkRequest['code'], ", data:",
                      checkRequest['error'], "(delete_object function in API class)")
            else:
                return (r.data)
        except:
            print(
                "[Error] bad request, check user id, class name (delete_object function in API class)")
            pass

            #   Create user

    def signing_up(user_info, addition_header=None):
        try:
            header = API.get_header(addition_header)
            http = API.http
            url = API.url + "users"
            role_control = {
                "ACL": {
                    "role:user": {
                        "read": True,
                        "write": True
                    }
                },
            }
        except:
            print(
                "[error] can't find header in API (delete_object function in API class)")
            pass
        try:
            user_info = dict(user_info)
            user_info.update(role_control)
            user_info_decoded = json.dumps(user_info)
            r = http.request(
                'POST', url, body=user_info_decoded, headers=header)
            checkRequest = DATA.convert_bytes_to_json(r.data)
            if('error' in list(checkRequest.keys())):
                print("[error] ", checkRequest['code'], ", data:",
                      checkRequest['error'], "(delete_object function in API class)")
            else:
                data_signing_up_result = DATA.convert_bytes_to_json(r.data)
                return (data_signing_up_result)
        except:
            print(
                "[Error] bad request, check user id, class name (delete_object function in API class)")
            pass

    #   Create API login

    def user_login(user_info, addition_header=None):
        try:
            header = API.get_header(addition_header)
            http = API.http
            url = API.url + "login?%s"
        except:
            print(
                "[error] can't find header in API (delete_object function in API class)")
            pass
        try:
            user_info_decode = urlencode(user_info)
            r = http.request('GET', url % user_info_decode, headers=header)
            checkRequest = DATA.convert_bytes_to_json(r.data)
            if('error' in list(checkRequest.keys())):
                print("[error] ", checkRequest['code'], ", data:",
                      checkRequest['error'], "(delete_object function in API class)")
            else:
                dataResultLogin = DATA.convert_bytes_to_json(r.data)
                return (dataResultLogin)
        except:
            print(
                "[Error] bad request, check user id, class name (delete_object function in API class)")
            pass

    def get_object_id_athm(class_name, algorithmName, addition_header=None):
        try:
            header = API.get_header()
            http = API.http
            url = API.url + "classes/" + str("class_name") + "?%s"
        except AttributeError:
            print(
                "[error] can't find header in API (get_data_user function in API class)")
            pass
        try:
            param = ({"where": json.dumps({
                "algorithmName": str(algorithmName)
            }), 'order': "-createdAt"})
            param_encoded = urlencode(param)
        except:
            print("[error]")
            pass
        try:
            r = http.request('GET', url % param_encoded, headers=header)
            return(r)
        except:
            print(
                "[Error] bad request, check user id, class name (get_data_user function in API class)")
            pass

    def upload_model_file(url_file_model, user_id, model_name, data_id, algorithm_id, params, col_label, col_label_name, col_feature, col_feature_name, description, addition_header=None):
        try:
            with open(url_file_model, 'rb') as fp:
                binary_data = fp.read()
            os.remove(url_file_model)
            http = API.http
            header = API.get_header(addition_header)
            url = API.url + "files/" + str(url_file_model)
        except:
            print(
                "[error] can't find header in API (upload_model_file function in API class)")
            pass
        # try:
            # r = http.request('POST', url, body=open(
            #     url_file_model, encoding="utf8", errors='ignore').read().encode('UTF-8'), headers=header)
        r = http.request('POST', url, body=binary_data, headers=header)
        checkRequest = DATA.convert_bytes_to_json(r.data)
        if('error' in list(checkRequest.keys())):
            print("[error] ", checkRequest['code'], ", data:",
                  checkRequest['error'], "(upload_model_file function in API class)")
        else:
            dataResultLogin = DATA.convert_bytes_to_json(r.data)
            # return (dataResultLogin)
            data = {
                "modelFile": {
                    "name": dataResultLogin['name'],
                    "url": dataResultLogin['url'],
                    "__type": "File"
                },
                "createdBy": {
                    "__type": "Pointer",
                    "className": "_User",
                    "objectId": user_id,
                },
                "modelName": model_name,
                "dataModel": {
                    "__type": "Pointer",
                    "className": "Data",
                    "objectId": data_id,
                },
                "algorithm": {
                    "__type": "Pointer",
                    "className": "Algorithm",
                    "objectId": algorithm_id,
                },
                "params": params,
                "colLabel": str(col_label),
                "colLabelName": str(col_label_name),
                "colFeature": str(col_feature),
                "colFeatureName": str(col_feature_name),
                "description": str(description),
            }
            url_upload_DB = API.url + "classes/" + "Model"
            header_upload_DB = API.get_header()
            data_decode = json.dumps(data)
            r = http.request('POST', url_upload_DB, body=data_decode,
                             headers=header_upload_DB)
            # print(r)
            return(r.data)
        # except:
        #     print("[Error]---")
        #     pass

    def upload_model_detail(model_id, athm, dataName, modelName, description, col_feature, col_label, col_feature_name, col_label_name, addition_header=None):
        try:
            http = API.http
            header = API.get_header(addition_header)
            url = API.url + "classes/ModelDetail"
        except:
            print(
                "[error] can't find header in API (upload_model_file function in API class)")
            pass
        data = {
            "colLabel": col_label,
            "colFeature": col_feature,
            "algorithm": athm,
            "modelName": modelName,
            "modelId": {
                "__type": "Pointer",
                "className": "Model",
                "objectId": model_id,
            },
            "description": description,
            "dataName": dataName,
            "colFeatureName": col_feature_name,
            "colLabelName": col_label_name
        }
        model_detail = json.dumps(data)
        r = http.request('POST', url, body=model_detail, headers=header)
        checkRequest = DATA.convert_bytes_to_json(r.data)
        if('error' in list(checkRequest.keys())):
            print("[error] ", checkRequest['code'], ", data:",
                  checkRequest['error'], "(upload_model_file function in API class)")
        else:
            dataResultLogin = DATA.convert_bytes_to_json(r.data)
            return (dataResultLogin)

    def get_model_detail(class_name, modelId, addition_header=None):
        try:
            header = API.get_header()
            http = API.http
            url = API.url + "classes/ModelDetail?%s"
        except AttributeError:
            print(
                "[error] can't find header in API (get_data_user function in API class)")
            pass
        try:
            param = ({"where": json.dumps({
                "modelId": modelId
            }), 'order': "-createdAt"})
            param_encoded = urlencode(param)
        except:
            print("[error]")
            pass
        try:
            r = http.request('GET', url % param_encoded, headers=header)
            arr = str(r.data, 'utf-8')
            data = json.loads(arr)
            if data['results'] == []:
                print(
                    "[error] request fail, check user id, class name (get_model_detail function in API class) ")
                return False
            else:
                return (data)
        except:
            print(
                "[Error] bad request, check user id, class name (get_model_detail function in API class)")
            pass

    def get_model(class_name, modelId, addition_header=None):
        try:
            header = API.get_header(addition_header)
            http = API.http
            url = API.url + "classes/" + str(class_name) + "/" + str(modelId)
        except AttributeError:
            print(
                "[error] can't find header in API (get_object_data function in API class)")
            pass
        try:
            r = http.request('GET', url, headers=header)
            arr = str(r.data, 'utf-8')
            data = json.loads(arr)
            return (data)
        except:
            print("[error] can't find data (get_model in function API class)")
            return ("[error] can't find data (get_model in function API class)")
            pass
    pass
