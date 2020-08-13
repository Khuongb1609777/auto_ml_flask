from sklearn.tree import DecisionTreeClassifier
from algorithm_parent import algorithm


class decision_tree_algorithm(algorithm):
    params = {
        'criterion': 'gini',
        'splitter': 'best',
        'max_depth': None,
        'min_samples_split': 2
    }

    def getParams(customParams=None):
        # try:
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
                    "[error] check type of parameter (decision_tree_algorithm getPatams function)")
                return False
            except ValueError:
                print(
                    "[error] check type of parameter (decision_tree_algorithm getPatams function)")
                return False
            except KeyError:
                print(
                    "[error] check type of parameter (decision_tree_algorithm getPatams function)")
                return False
            try:
                clf = DecisionTreeClassifier(
                    criterion=customParams['criterion'], splitter=customParams['splitter'], max_depth=customParams['maxDepth'], min_samples_split=customParams['minSamples'])
                return clf
            except:
                print(
                    "[error] check type of parameter (decision_tree_algorithm getPatams function)")
                return False
        else:
            try:
                clf = DecisionTreeClassifier(
                    criterion=decision_tree_algorithm.params['criterion'], splitter=decision_tree_algorithm.params['splitter'], max_depth=decision_tree_algorithm.params['max_depth'], min_samples_split=decision_tree_algorithm.params['min_samples_split'])
                return clf
            except:
                print(
                    "[error] check type of parameter (decision_tree_algorithm getPatams function)")
                return False

        # except:
        #     print("[Error] check input for getParams function decision Tree")
    pass
