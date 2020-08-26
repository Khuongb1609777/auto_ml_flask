from sklearn.naive_bayes import GaussianNB
from algorithm_parent import algorithm
from error import ERROR


class naive_bayes_algorithm(algorithm):
    params = {
        'priors': None,
        'var_smoothing': 1e-09,
    }

    def getParams(custom_params):
        if (custom_params):
            try:
                custom_params = dict(custom_params)
                custom_params['varSmoothing'] = float(
                    custom_params['varSmoothing'])
            except TypeError:
                print(
                    "[errorParams] check type of parameter (naive_bayes_algorithm getPatams function)")
                data = ERROR.error_params['error_params_naiveBayes']
                return data
            except ValueError:
                print(
                    "[errorParams] check type of parameter (naive_bayes_algorithm getPatams function)")
                data = ERROR.error_params['error_params_naiveBayes']
                return data
            except KeyError:
                print(
                    "[errorParams] check type of parameter (naive_bayes_algorithm getPatams function)")
                data = ERROR.error_params['error_params_naiveBayes']
                return data
            try:
                clf = GaussianNB(
                    priors=None, var_smoothing=custom_params['varSmoothing'])
                return clf
            except:
                print(
                    "[errorParams] check type of parameter (naive_bayes_algorithm getPatams function)")
                data = ERROR.error_params['error_params_naiveBayes']
                return data
        else:
            try:
                clf = GaussianNB(
                    priors=None, var_smoothing=naive_bayes_algorithm.params['var_smoothing'])
                return clf
            except:
                print(
                    "[errorParams] check type of parameter (naive_bayes_algorithm getPatams function)")
                data = ERROR.error_params['error_params_naiveBayes']
                return data
    pass
