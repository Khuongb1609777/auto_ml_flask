import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import csv
import json


class DATA:
    def read(file_tail, file_path, separator):
        if file_tail == 'csv':
            try:
                data_reader = pd.read_csv(
                    file_path, delimiter=separator, header=None)
            except(FileNotFoundError):
                print("file_path or file_tail false")
        elif file_tail == 'excel':
            try:
                data_reader = pd.read_excel(file_path, header=None)
            except(FileNotFoundError):
                print("file_path or file_tail false")
        #   Check columns atribute
        try:
            list_name = list(data_reader.iloc[0, :])
            list_label = list(
                data_reader.iloc[1:, len(list_name)-1].drop_duplicates())
        except UnboundLocalError:
            print("variable data_reader not exist")
        except IndexError:
            print("index error")
        try:
            if list_name[len(list_name)-1] not in list_label:
                data_reader = data_reader.drop(0)
                data_reader.columns = list_name
            else:
                list_name_col = []
                for i in range(len(list_name)):
                    name = 'columns _ ' + str(i)
                    list_name_col.append(name)
                data_reader.columns = list_name_col
            m = data_reader.shape[0]
            n = data_reader.shape[1]
            columns = data_reader.columns  # AttributeErrorUnboundLocalError
        except IndexError:
            print("index error")
        except UnboundLocalError:
            print("variable data_reader not exist")
        except AttributeError:
            print("data_reader is not data_reader frame")
        return (data_reader, columns, n, m)

    def check_columns_name(data_frame):
        try:
            data_frame = pd.DataFrame(data_frame)
        except ValueError:
            print("[error] Can't parse data input to dataframe")
            pass
        try:
            list_name = list(data_frame.iloc[0, :])
            list_label = list(
                data_frame.iloc[1:, len(list_name)-1].drop_duplicates())
        except AttributeError:
            print("[error] Data input is not dataframe, has no attribute 'iloc'")
            pass
        try:
            if list_name[len(list_name)-1] not in list_label:
                data_frame = data_frame.drop(0)
                data_frame.columns = list_name
                data_frame = data_frame.reset_index(drop=True)
            else:
                list_name_col = []
                for i in range(len(list_name)):
                    name = 'columns _ ' + str(i)
                    list_name_col.append(name)
                data_frame.columns = list_name_col
                data_frame = data_frame.reset_index(drop=True)
        except UnboundLocalError:
            print(
                "[error] Can't find list_name (check input) ")
        return (data_frame)

    def get_data_train(data, col_feature, col_label, choose_size):
        try:
            data = pd.DataFrame(data)
        except ValueError:
            print("[error] Can't parse data input to dataframe")
            pass
        try:
            X = data.iloc[:, col_feature]
            Y = data.iloc[:, col_label]
        except AttributeError:
            print("[error] Data input is not dataframe, has no attribute 'iloc'")
            pass
        except IndexError:
            print(
                "[error] check input (label and feature) single positional indexer is out-of-bounds")
            pass
        try:
            X_train = ""
            X_test = ""
            y_train = ""
            y_test = ""
            X_train, X_test, y_train, y_test = train_test_split(
                X, Y, test_size=choose_size, random_state=40, shuffle=True)
        except UnboundLocalError:
            print("[error] can't get train, test data, check type of data input")
            pass
        except ValueError:
            print("[error] can't get train, test data, check type of data input")
            pass
        if (X_train, X_test, y_train, y_test):
            return (X_train, X_test, y_train, y_test)
        else:
            return False

    def convert_str(file):
        results = []
        result_str = ""
        try:
            with open(file) as csvfile:
                # change contents to floats
                reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
                for row in reader:  # each row is a list
                    results.append(row)
                result_str = json.dumps(results)
        except FileNotFoundError:
            print("[error] can't find", file, "check file path")
            pass
        if result_str:
            return (result_str)
        else:
            return False

    def convert_dataframe(data):
        try:
            r_json = (data).decode('utf8').replace("'", '"')
            data = json.loads(r_json)
            data_json = json.loads(data['jsonData'])
        except KeyError:
            print("[error] can't request, check class name, objectId")
            pass
        except AttributeError:
            print(
                "[error] check input type (input of convert_dataframe function must be type(bytes)")
            pass
        try:
            data_arr = np.array(data_json)
            data_frame = pd.DataFrame(data_arr)
            return (data_frame)
        except UnboundLocalError:
            print("[error] can't find data_json (convert_dataframe function)")
            pass
        except AttributeError:
            print(
                "[error] check input type (input of convert_dataframe function must be type(bytes)")
            pass
    #     return (file_path_json)

    #   Create convert function for return form API parser
    def convert_bytes_to_json(data_bytes):
        try:
            data_str = (data_bytes).decode('utf8').replace("'", '"')
            data_json = json.loads(data_str)
            return data_json
        except AttributeError:
            print("[error] check input type")
            pass

    pass
