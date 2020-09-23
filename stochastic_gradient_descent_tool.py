from sklearn.linear_model import SGDClassifier
from algorithm_parent import algorithm
from error import ERROR


class SGD_classifier_algorithm(algorithm):
    params = {
        'loss': 'hinge',
        'penalty': 'l2',
        'alpha': 0.0001,
        'l1_ratio': 0.15,
        'max_iter': 1000,
        'verbose': 0,
        'epsilon': 0.1
    }

    def getParams(customParams=None):
        if customParams:
            try:
                customParams = dict(customParams)
                print(customParams)
                customParams['loss'] = str(customParams['loss'])
                customParams['penalty'] = str(customParams['penalty'])
                customParams['alpha'] = float(customParams['alpha'])
                customParams['max_iter'] = int(customParams['max_iter'])
                print("test", customParams)
                customParams['verbose'] = int(customParams['verbose'])
                customParams['epsilon'] = float(customParams['epsilon'])

            except TypeError:
                print(
                    "[errorParams] check type of parameter (error_params_SGD getPatams function)")
                data = ERROR.error_params['error_params_SGD']
                return data
            except ValueError:
                print(
                    "[errorParams] check type of parameter (error_params_SGD getPatams function)")
                data = ERROR.error_params['error_params_SGD']
                return data
            except KeyError:
                print(
                    "[errorParams] check type of parameter (error_params_SGD getPatams function)")
                data = ERROR.error_params['error_params_SGD']
                return data
            try:
                clf = SGDClassifier(loss=customParams['loss'], penalty=customParams['penalty'], alpha=customParams['alpha'],
                                    max_iter=customParams['max_iter'], verbose=customParams['verbose'], epsilon=customParams['epsilon'])
                # clf = RidgeClassifier(
                #     alpha=1.0, max_inter=customParams['max_inter'])
                return clf
            except:
                print(
                    "[errorParams] check type of parameter (error_params_SGD getPatams function)")
                data = ERROR.error_params['error_params_SGD']
                return data
        else:
            try:
                clf = SGDClassifier(loss=SGD_classifier_algorithm.params['loss'], penalty=SGD_classifier_algorithm.params['penalty'],
                                    alpha=SGD_classifier_algorithm.params[
                                        'alpha'], max_iter=SGD_classifier_algorithm.params['max_iter'],
                                    verbose=SGD_classifier_algorithm.params['verbose'], epsilon=SGD_classifier_algorithm.params['epsilon'])
                return clf
            except:
                print(
                    "[error] check type of parameter (error_params_SGD getPatams function)")
                data = ERROR.error_params['error_params_SGD']
                return data
    pass
