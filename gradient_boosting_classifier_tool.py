from sklearn.ensemble import GradientBoostingClassifier
from algorithm_parent import algorithm
from error import ERROR


class gradient_boosting_classifier_algorithm(algorithm):
    params = {
        'learning_rate': 0.1,
        'n_estimators': 100,
        'subsample': 1.0,
    }

    def getParams(customParams=None):
        if customParams:
            try:
                customParams = dict(customParams)
                customParams['learning_rate'] = float(
                    customParams['learningRate'])
                customParams['n_estimators'] = int(customParams['nEstimators'])
                customParams['subsample'] = float(customParams['subsample'])
            except TypeError:
                print(
                    "[errorParams] check type of parameter (error_params_GradientBoostingClassifier getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingClassifier']
                return data
            except ValueError:
                print(
                    "[errorParams] check type of parameter (error_params_GradientBoostingClassifier getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingClassifier']
                return data
            except KeyError:
                print(
                    "[errorParams] check type of parameter (error_params_GradientBoostingClassifier getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingClassifier']
                return data
            try:
                clf = GradientBoostingClassifier(
                    learning_rate=customParams['learning_rate'], n_estimators=customParams['n_estimators'], subsample=customParams['subsample'])
                return clf
            except:
                print(
                    "[errorParams] check type of parameter (error_params_GradientBoostingClassifier getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingClassifier']
                return data
        else:
            try:
                clf = GradientBoostingClassifier(learning_rate=gradient_boosting_classifier_algorithm.params['learning_rate'], n_estimators=gradient_boosting_classifier_algorithm.params[
                                                 'n_estimators'], subsample=gradient_boosting_classifier_algorithm.params['subsample'])
                return clf
            except:
                print(
                    "[error] check type of parameter (decision_tree_algorithm getPatams function)")
                data = ERROR.error_params['error_params_GradientBoostingClassifier']
                return data
    pass
