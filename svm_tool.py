from sklearn.svm import SVC
from algorithm_parent import algorithm
import json
from error import ERROR


class svm_algorithm(algorithm):
    params = {
        'c': 10,
        'gamma': 0.5,
        'degree': 3
    }

    def getParams(custom_params=None):
        # try:
        if(custom_params):
            try:
                custom_params = dict(custom_params)
                custom_params['C'] = int(custom_params['C'])
                custom_params['gamma'] = float(custom_params['gamma'])
                custom_params['degree'] = int(custom_params['degree'])
            except TypeError:
                print("[errorParams] check type of parameter, params_c is int, params_gamma is float and degree is int (svm_tool getPatams function)")
                data = ERROR.error_params['error_params_SVM']
                return data
            except ValueError:
                print("[errorParams] check type of parameter, params_c is int, params_gamma is float and degree is int (svm_tool getPatams function)")
                data = ERROR.error_params['error_params_SVM']
                return data
            except KeyError:
                print("[errorParams] check type of parameter, params_c is int, params_gamma is float and degree is int (svm_tool getPatams function)")
                data = ERROR.error_params['error_params_SVM']
                return data
            try:
                clf = SVC(C=custom_params['C'], kernel='rbf',
                          degree=custom_params['degree'], gamma=custom_params['gamma'])
                return clf
            except:
                print("[errorParams] check type of parameter, params_c is int, params_gamma is float and degree is int (svm_tool getPatams function)")
                data = ERROR.error_params['error_params_SVM']
                return data
        else:
            try:
                clf = SVC(C=svm_algorithm.params['c'], kernel='rbf',
                          degree=svm_algorithm.params['degree'], gamma=svm_algorithm.params['gamma'])
                return clf
            except:
                print("[errorParams] check type of parameter, params_c is int, params_gamma is float and degree is int (svm_tool getPatams function)")
                data = ERROR.error_params['error_params_SVM']
                return data
    pass
