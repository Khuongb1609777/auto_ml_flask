from sklearn.ensemble import RandomForestClassifier
from algorithm_parent import algorithm


class randomforest_algorithm(algorithm):
    params = {
        'nEstimators': 100,
        'criterion': 'gini',
        'maxDepth': None,
        'minSamples': 2
    }

    def getParams(custom_params=None):
        # try:
        if custom_params:
            try:
                custom_params = dict(custom_params)
                custom_params['nEstimators'] = int(
                    custom_params['nEstimators'])
                custom_params['maxDepth'] = int(custom_params['maxDepth'])
                custom_params['minSamples'] = int(custom_params['minSamples'])
                custom_params['criterion'] = str(custom_params['criterion'])
            except TypeError:
                print(
                    "[error] check type of parameter (randomforest_algorithm getPatams function)")
                return False
            except ValueError:
                print(
                    "[error] check type of parameter (randomforest_algorithm getPatams function)")
                return False
            except KeyError:
                print(
                    "[error] check type of parameter (randomforest_algorithm getPatams function)")
                return False
            try:
                clf = RandomForestClassifier(
                    n_estimators=custom_params['nEstimators'], criterion=custom_params['criterion'], max_depth=custom_params['maxDepth'])
                return clf
            except:
                print(
                    "[error] check type of parameter (randomforest_algorithm getPatams function)")
                return False
        else:
            try:
                clf = RandomForestClassifier(
                    n_estimators=randomforest_algorithm.params['nEstimators'], criterion=randomforest_algorithm.params['criterion'], max_depth=randomforest_algorithm.params['maxDepth'])
                return clf
            except:
                print(
                    "[error] check type of parameter (randomforest_algorithm getPatams function)")
                return False
        # except:
        #     print("[Error] check input for getParams function random Forest")
    pass
