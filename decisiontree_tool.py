from sklearn.tree import DecisionTreeClassifier
from algorithm_parent import algorithm
from error import ERROR


class decision_tree_algorithm(algorithm):
    params = {
        'criterion': 'gini',
        'splitter': 'best',
        'max_depth': None,
        'min_samples_split': 2
    }

    def getParams(customParams=None):
        if customParams:
            try:
                customParams = dict(customParams)
                customParams['criterion'] = str(customParams['criterion'])
                # print("cri", customParams['criterion'])
                customParams['splitter'] = str(customParams['splitter'])
                # print("splitter", customParams['splitter'])
                customParams['maxDepth'] = int(customParams['maxDepth'])
                # print("maxDepth", customParams['maxDepth'])
                customParams['minSamples'] = int(
                    customParams['minSamplesSplit'])
                # print("minSamples", customParams['minSamples'])
            except TypeError:
                print(
                    "[errorParams] check type of parameter (decision_tree_algorithm getPatams function)")
                data = ERROR.error_params['error_params_decisionTree']
                return data
            except ValueError:
                print(
                    "[errorParams] check type of parameter (decision_tree_algorithm getPatams function)")
                data = ERROR.error_params['error_params_decisionTree']
                return data
            except KeyError:
                print(
                    "[errorParams] check type of parameter (decision_tree_algorithm getPatams function)")
                data = ERROR.error_params['error_params_decisionTree']
                return data
            try:
                clf = DecisionTreeClassifier(
                    criterion=customParams['criterion'], splitter=customParams['splitter'], max_depth=customParams['maxDepth'], min_samples_split=customParams['minSamples'])
                return clf
            except:
                print(
                    "[errorParams] check type of parameter (decision_tree_algorithm getPatams function)")
                data = ERROR.error_params['error_params_decisionTree']
                return data
        else:
            try:
                clf = DecisionTreeClassifier(
                    criterion=decision_tree_algorithm.params['criterion'], splitter=decision_tree_algorithm.params['splitter'], max_depth=decision_tree_algorithm.params['max_depth'], min_samples_split=decision_tree_algorithm.params['min_samples_split'])
                return clf
            except:
                print(
                    "[error] check type of parameter (decision_tree_algorithm getPatams function)")
                data = ERROR.error_params['error_params_decisionTree']
                return data
    pass
