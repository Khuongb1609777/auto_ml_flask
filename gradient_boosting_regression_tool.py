from sklearn.ensemble import GradientBoostingRegressor
from algorithm_parent import algorithm
from error import ERROR


class gradient_boosting_regression_algorithm(algorithm):
    params = {
        'loss': "ls",
        'learning_rate': 0.1,
        'n_estimators': 100,
        'subsample': 1.0,
        'criterion': 'friedman_mse'
    }

    def getParams(customParams=None):
        if customParams:
            try:
                customParams = dict(customParams)
                customParams['loss'] = str(customParams['loss'])
                customParams['learning_rate'] = float(
                    customParams['learningRate'])
                customParams['n_estimators'] = int(customParams['nEstimators'])
                customParams['subsample'] = float(customParams['subsample'])
                customParams['criterion'] = str(customParams['criterion'])
            except TypeError:
                print(
                    "[errorParams] check type of parameter (error_params_GradientBoostingRegression getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingRegression']
                return data
            except ValueError:
                print(
                    "[errorParams] check type of parameter (error_params_GradientBoostingRegression getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingRegression']
                return data
            except KeyError:
                print(
                    "[errorParams] check type of parameter (error_params_GradientBoostingRegression getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingRegression']
                return data
            try:
                clf = GradientBoostingRegressor(loss=customParams['loss'],
                                                learning_rate=customParams['learning_rate'], n_estimators=customParams['n_estimators'], subsample=customParams['subsample'], criterion=customParams['criterion'])
                return clf
            except:
                print(
                    "[errorParams] check type of parameter (error_params_GradientBoostingRegression getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingRegression']
                return data
        else:
            try:
                clf = GradientBoostingRegressor(loss=gradient_boosting_regression_algorithm.params['loss'], learning_rate=gradient_boosting_regression_algorithm.params['learning_rate'], n_estimators=gradient_boosting_regression_algorithm.params[
                    'n_estimators'], subsample=gradient_boosting_regression_algorithm.params['subsample'], criterion=gradient_boosting_regression_algorithm.params['criterion'])
                return clf
            except:
                print(
                    "[error] check type of parameter (error_params_GradientBoostingRegression getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingRegression']
                return data
    pass
