from sklearn.naive_bayes import GaussianNB
from algorithm_parent import algorithm


class naive_bayes_algorithm(algorithm):
    params = {
        'priors': None,
        'var_smoothing': 1e-09,
    }

    def getParams(custom_params):
        # try:
        if (custom_params):
            try:
                custom_params = dict(custom_params)
                custom_params['varSmoothing'] = float(
                    custom_params['varSmoothing'])
            except TypeError:
                print(
                    "[error] check type of parameter (naive_bayes_algorithm getPatams function)")
                return False
            except ValueError:
                print(
                    "[error] check type of parameter (naive_bayes_algorithm getPatams function)")
                return False
            except KeyError:
                print(
                    "[error] check type of parameter (naive_bayes_algorithm getPatams function)")
                return False
            try:
                clf = GaussianNB(
                    priors=None, var_smoothing=custom_params['varSmoothing'])
                return clf
            except:
                print(
                    "[error] check type of parameter (naive_bayes_algorithm getPatams function)")
                return False
        else:
            try:
                clf = GaussianNB(
                    priors=None, var_smoothing=naive_bayes_algorithm.params['var_smoothing'])
                return clf
            except:
                print(
                    "[error] check type of parameter (naive_bayes_algorithm getPatams function)")
                return False
        # except:
        #     print("[Error] check input for getParams function Naive bayes")
        #     pass
    pass
