from sklearn.linear_model import LinearRegression
from algorithm_parent import algorithm
from error import ERROR


class linear_regression_algorithm(algorithm):
    params = {
        'fitIntercept': True,
        'normalize': False,
    }

    def getParams(custom_params=None):
        if (custom_params):
            try:
                custom_params = dict(custom_params)
            except ValueError:
                print(
                    "[errorParams] input is not dict, can't parse dict linearegression tool (get params function)")
                data = ERROR.error_params['error_params_linearRegression']
                return data
            try:
                params_true = ["true", "True", "treu", "Treu", "TRUE",
                               "tRUE", "tRue", "trUe", "truE", "TRue", "TrUe", "TruE", "tRUe", "tRuE", "trUE", "TRUe", "tRUE", "TrUE", "TRuE"]
                params_false = ["false", "False", "fAlse", "faLse", "falSe",
                                "falsE", "FAlse", "fALse", "faLSe", "falSE", "FALSE", "FALSR"]
                for p in custom_params.keys():
                    if (custom_params[p] in list(params_true)):
                        custom_params[p] = True
                    elif (custom_params[p] in list(params_false)):
                        custom_params[p] = False
                    else:
                        data = {
                            "errorParams": "error, function parameters LinearGression, Please check your parameters again, with Linear Gression, 'fitIntercept' and 'normalize' is 'True or False'"
                        }
                        return data
            except KeyError:
                data = ERROR.error_params['error_params_linearRegression']
                return data
            try:
                clf = LinearRegression(
                    fit_intercept=custom_params['fitIntercept'], normalize=custom_params['normalize'])
                return clf
            except UnboundLocalError:
                print(
                    "[errorParams] error, function parameters LinearGression , please check params linear (regression tool)")
                data = ERROR.error_params['error_params_linearRegression']
                return data
            except KeyError:
                print(
                    "[errorParams] error, function parameters LinearGression , please check params linear (regression tool)")
                data = ERROR.error_params['error_params_linearRegression']
                return data
        else:
            try:
                clf = LinearRegression(
                    fit_intercept=linear_regression_algorithm.params['fitIntercept'], normalize=linear_regression_algorithm.params['normalize'])
                return clf
            except UnboundLocalError:
                print(
                    "[errorParams] error, function parameters LinearGression , please check params linear (regression tool)")
                data = ERROR.error_params['error_params_linearRegression']
                return data
    pass
