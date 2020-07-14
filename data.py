import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
class DATA:
    def read(file_tail, file_path):
        if file_tail == 'csv':
            data = pd.read_csv(file_path,header = None)
        elif file_tail == 'xlsx':
            data = pd.read_excel(file_path,header = None)
        #   Check columns atribute
        list_name = list(data.iloc[0,:])
        list_label  =  list(data.iloc[1:,len(list_name)-1].drop_duplicates())
        if list_name[len(list_name)-1] not in list_label:
            data = data.drop(0)
            data.columns = list_name
        else:
            list_name_col = []
            for i in range(len(list_name)):
                name = 'columns _ '+ str(i)
                list_name_col.append(name)
            data.columns = list_name_col
        m = data.shape[0]
        n = data.shape[1]
        return (data, data.columns, n, m)
    def get_data_train(data, col_feature, col_label, choose_size):
        X = data.iloc[:, col_feature]
        Y = data.iloc[:, col_label]
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = choose_size, random_state=40)
        return X_train, X_test, y_train, y_test
    pass