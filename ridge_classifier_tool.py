from sklearn.linear_model import RidgeClassifier
from algorithm_parent import algorithm
from error import ERROR


class ridge_classifier_algorithm(algorithm):
    params = {
        'alpha': 1.0,
        'max_inter': 3.0,
    }

    def getParams(customParams=None):
        if customParams:
            try:
                customParams = dict(customParams)
                customParams['alpha'] = float(customParams['alpha'])
                customParams['max_inter'] = float(customParams['maxInter'])
            except TypeError:
                print(
                    "[errorParams] check type of parameter (error_params_ridge_classifier getPatams function)")
                data = ERROR.error_params['error_params_ridge_classifier']
                return data
            except ValueError:
                print(
                    "[errorParams] check type of parameter (error_params_ridge_classifier getPatams function)")
                data = ERROR.error_params['error_params_ridge_classifier']
                return data
            except KeyError:
                print(
                    "[errorParams] check type of parameter (error_params_ridge_classifier getPatams function)")
                data = ERROR.error_params['error_params_ridge_classifier']
                return data
            try:
                clf = RidgeClassifier(
                    alpha=ridge_classifier_algorithm.params['alpha'], max_iter=ridge_classifier_algorithm.params['max_inter'])
                # clf = RidgeClassifier(
                #     alpha=1.0, max_inter=customParams['max_inter'])
                return clf
            except:
                print(
                    "[errorParams] check type of parameter (error_params_ridge_classifier getPatams function)")
                data = ERROR.error_params['error_params_ridge_classifier']
                return data
        else:
            try:
                clf = RidgeClassifier(
                    alpha=ridge_classifier_algorithm.params['alpha'], max_iter=ridge_classifier_algorithm.params['max_inter'])
                return clf
            except:
                print(
                    "[error] check type of parameter (error_params_ridge_classifier getPatams function)")
                data = ERROR.error_params['error_params_ridge_classifier']
                return data
    pass
