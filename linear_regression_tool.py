from sklearn.linear_model import LinearRegression
from algorithm_parent import algorithm


class linear_regression_algorithm(algorithm):
    params = {
        'fitIntercept': True,
        'normalize': False,
    }

    def getParams(custom_params=None):
        # try:
        if (custom_params):
            try:
                custom_params = dict(custom_params)
            except ValueError:
                print(
                    "[error] input is not dict, can't parse dict linearegression tool (get params function)")
                return False
            try:
                params_true = ["true", "True", "treu", "Treu", "TRUE",
                               "tRUE", "tRue", "trUe", "truE", "TRue", "TrUe", "TruE", "tRUe", "tRuE", "trUE", "TRUe", "tRUE", "TrUE", "TRuE"]
                for p in custom_params.keys():
                    if (custom_params[p] in list(params_true)):
                        custom_params[p] = True
                    else:
                        custom_params[p] = False
            except KeyError:
                print("[error] can not convert type of params")
            try:
                clf = LinearRegression(
                    fit_intercept=custom_params['fitIntercept'], normalize=custom_params['normalize'])
                return clf
            except UnboundLocalError:
                print(
                    "[error] input for function LinearGression is false, check params linear (regression tool)")
            except KeyError:
                print(
                    "[error] input for function LinearGression is false, check params linear (regression tool)")
        else:
            try:
                clf = LinearRegression(
                    fit_intercept=linear_regression_algorithm.params['fitIntercept'], normalize=linear_regression_algorithm.params['normalize'])
                return clf
            except UnboundLocalError:
                print(
                    "[error] input for function LinearGression is false, check params linear (regression tool)")

        # except:
        #     print("[Error] check input for getParams function linear_regression")
        #     pass
    pass
