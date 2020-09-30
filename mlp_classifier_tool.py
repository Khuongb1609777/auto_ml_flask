from algorithm_parent import algorithm
from error import ERROR
from sklearn.neural_network import MLPClassifier


class MLP_classifier_algorithm(algorithm):
    params = {
        'hidden_layer_sizes': 100,
        'activation': 'relu',
        'solver': 'adam',
        'alpha': 0.0001,
        'batch_size': 20,
        'learning_rate': 'constant',
        'learning_rate_init': 0.001,
        'power_t': 0.5,
        'max_iter': 200
    }

    def getParams(customParams=None):
        if customParams:
            try:
                customParams = dict(customParams)
                customParams['hiddenLayerSizes'] = int(
                    customParams['hiddenLayerSizes'])
                customParams['solver'] = str(customParams['solver'])
                customParams['alpha'] = float(customParams['alpha'])
                print(customParams)
                customParams['batchSize'] = int(customParams['batchSize'])
                customParams['learningRate'] = str(
                    customParams['learningRate'])
                customParams['learningRateInit'] = float(
                    customParams['learningRateInit'])
                customParams['powerT'] = float(customParams['powerT'])
                customParams['maxIter'] = int(customParams['maxIter'])
                # print(customParams)
            except TypeError:
                print(
                    "[errorParams] check type of parameter (error_params_MLP getPatams function)")
                data = ERROR.error_params['error_params_MLP']
                return data
            except ValueError:
                print(
                    "[errorParams] check type of parameter (error_params_MLP getPatams function)")
                data = ERROR.error_params['error_params_MLP']
                return data
            except KeyError:
                print(
                    "[errorParams] check type of parameter (error_params_MLP getPatams function)")
                data = ERROR.error_params['error_params_MLP']
                return data
            try:
                clf = MLPClassifier(hidden_layer_sizes=customParams['hiddenLayerSizes'], solver=customParams['solver'], alpha=customParams['alpha'],
                                    batch_size=customParams['batchSize'], learning_rate=customParams[
                                        'learningRate'], learning_rate_init=customParams['learningRateInit'],
                                    power_t=customParams['powerT'], max_iter=customParams['maxIter'])
                return clf
            except:
                print(
                    "[errorParams] check type of parameter (error_params_MLP getPatams function)")
                data = ERROR.error_params['error_params_MLP']
                return data
        else:
            try:
                clf = MLPClassifier(hidden_layer_sizes=MLP_classifier_algorithm.params['hidden_layer_sizes'], solver=MLP_classifier_algorithm.params['solver'], alpha=MLP_classifier_algorithm.params['alpha'],
                                    batch_size=MLP_classifier_algorithm.params['batch_size'], learning_rate=MLP_classifier_algorithm.params[
                                        'learning_rate'], learning_rate_init=MLP_classifier_algorithm.params['learning_rate_init'],
                                    power_t=MLP_classifier_algorithm.params['power_t'], max_iter=MLP_classifier_algorithm.params['max_iter'])
                return clf
            except:
                print(
                    "[error] check type of parameter (decision_tree_algorithm getPatams function)")
                data = ERROR.error_params['error_params_MLP']
                return data
    pass
