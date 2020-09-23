from sklearn.linear_model import LogisticRegression
from algorithm_parent import algorithm
from error import ERROR


class logistic_regression_algorithm(algorithm):
    params = {
        'penalty': "l2",
        'tol': 0.0001,
        'C': 1.0,
        'intercept_scaling': 1.0,
    }

    def getParams(customParams=None):
        if customParams:
            try:
                customParams = dict(customParams)
                customParams['penalty'] = str(customParams['penalty'])
                customParams['tol'] = float(customParams['tol'])
                customParams['C'] = float(customParams['C'])
                customParams['intercept_scaling'] = float(
                    customParams['interceptScaling'])
            except TypeError:
                print(
                    "[errorParams] check type of parameter (error_params_Logistic_regression getPatams function)")
                data = ERROR.error_params['error_params_Logistic_regression']
                return data
            except ValueError:
                print(
                    "[errorParams] check type of parameter (error_params_Logistic_regression getPatams function)")
                data = ERROR.error_params['error_params_Logistic_regression']
                return data
            except KeyError:
                print(
                    "[errorParams] check type of parameter (error_params_Logistic_regression getPatams function)")
                data = ERROR.error_params['error_params_Logistic_regression']
                return data
            try:
                clf = LogisticRegression(penalty=customParams['penalty'], tol=customParams['tol'],
                                         C=customParams['C'], intercept_scaling=customParams['intercept_scaling'])
                return clf
            except:
                print(
                    "[errorParams] check type of parameter (error_params_Logistic_regression getPatams function)")
                data = ERROR.error_params['error_params_Logistic_regression']
                return data
        else:
            try:
                clf = LogisticRegression(penalty=logistic_regression_algorithm.params['penalty'], tol=logistic_regression_algorithm.params[
                                         'tol'], C=logistic_regression_algorithm.params['C'], intercept_scaling=logistic_regression_algorithm.params['intercept_scaling'])
                return clf
            except:
                print(
                    "[error] check type of parameter (error_params_Logistic_regression getPatams function)")
                data = ERROR.error_params['error_params_Logistic_regression']
                return data
    pass
