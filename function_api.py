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

    def get_data_createmodel(class_name, object_id, addition_header=None):
        try:
            header = API.get_header()
            http = API.http
            url = API.url + "classes/" + str(class_name) + "/" + str(object_id)
        except AttributeError:
            print(
                "[error] can't find header in API (get_data_createmodel function in API class)")
            pass
        try:
            r = http.request_encode_url('GET', url, headers=header)
            rJson = DATA.convert_bytes_to_json(r.data)
            if('error' in list(rJson.keys())):
                print("[error] ", rJson['code'], ", data:",
                      rJson['error'], "--check class_name, objectId (get_data_createmodel function in API class)")
                return False
            else:
                return (rJson)
        except:
            print(
                "[Error get data] check object id (get_data_createmodel function in API class)")
            pass

    def get_data_user(class_name, userId, addition_header=None):
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
                "userUpload": userId
            })
            })
            param_encoded = urlencode(param)
        except:
            print("[error]")
            pass
        try:
            r = http.request('GET', url % param_encoded, headers=header)
            data = DATA.convert_bytes_to_json(r.data)
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

    def get_model_user(class_name, userId, addition_header=None):
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
                "userCreate": userId
            })
            })
            param_encoded = urlencode(param)
        except:
            print("[error]")
            pass
        try:
            r = http.request('GET', url % param_encoded, headers=header)
            data = DATA.convert_bytes_to_json(r.data)
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

    def userLogin(user_info, addition_header=None):
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

    def upload_model_file(uId, data_name, url_file_model, addition_header=None):
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
                "userCreate": {
                    "__type": "Pointer",
                    "className": "_User",
                    "objectId": uId,
                },
                "dataModel": {
                    "__type": "Pointer",
                    "className": "Data",
                    "objectId": data_name,
                },
                "modelFile": {
                    "name": dataResultLogin['name'],
                    "url": dataResultLogin['url'],
                    "__type": "File"
                }
            }
            url_upload_DB = API.url + "classes/" + "Model"
            header_upload_DB = API.get_header()
            data_decode = json.dumps(data)
            r = http.request('POST', url_upload_DB, body=data_decode,
                             headers=header_upload_DB)
            print(r)
            return(r.data)
        # except:
        #     print("[Error]---")
        #     pass

    def upload_modeldetail(model_id, athm, col_feature, col_label, addition_header=None):
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
            "modelId": {
                "__type": "Pointer",
                "className": "Model",
                "objectId": model_id,
            },
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
            url = API.url + "classes/" + str(class_name) + "?%s"
        except AttributeError:
            print(
                "[error] can't find header in API (get_data_user function in API class)")
            pass
        try:
            param = ({"where": json.dumps({
                "modelId": modelId
            })
            })
            param_encoded = urlencode(param)
        except:
            print("[error]")
            pass
        try:
            r = http.request('GET', url % param_encoded, headers=header)
            data = DATA.convert_bytes_to_json(r.data)
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
    pass
