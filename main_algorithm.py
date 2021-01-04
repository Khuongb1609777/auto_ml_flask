from svm_tool import svm_algorithm
from randomforest_tool import randomforest_algorithm
from naive_bayes_tool import naive_bayes_algorithm
from decisiontree_tool import decision_tree_algorithm
from linear_regression_tool import linear_regression_algorithm
from gradient_boosting_classifier_tool import gradient_boosting_classifier_algorithm
from gradient_boosting_regression_tool import gradient_boosting_regression_algorithm
from logistic_regression_tool import logistic_regression_algorithm
from ridge_classifier_tool import ridge_classifier_algorithm
from stochastic_gradient_descent_tool import SGD_classifier_algorithm
from mlp_classifier_tool import MLP_classifier_algorithm


def get_athm(athm, X_train, X_test, y_train, y_test, params=None):
    # try:
    if athm == "LinearRegression":
        try:
            clf = linear_regression_algorithm.getParams(params)
            model, evalution, error = linear_regression_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = linear_regression_algorithm.params
        except TypeError:
            pass
        except UnboundLocalError:
            pass
        except ValueError:
            pass
    elif athm == "RandomForest":
        try:
            clf = randomforest_algorithm.getParams(params)
            model, evalution, error = randomforest_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = randomforest_algorithm.params
        except TypeError:
            print("co loi xay ra", clf["errorParams"])
            pass
        except UnboundLocalError:
            print("co loi xay ra", clf["errorParams"])
            pass
    elif athm == "NaiveBayes":
        try:
            clf = naive_bayes_algorithm.getParams(params)
            model, evalution, error = naive_bayes_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = naive_bayes_algorithm.params
        except TypeError:
            print("[error] naive_bayes_algorithm")
            pass
        except UnboundLocalError:
            print("[error] naive_bayes_algorithm")
            pass
    elif athm == "SupportVectorMachine":
        try:
            clf = svm_algorithm.getParams(params)
            model, evalution, error = svm_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = svm_algorithm.params
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    # elif athm == "ArtificialNeuralNetwork":GradientBoostingClassifier
    #     try:
    #         model, evalution, error = artificial_neural_network_algorithm.model_ann(
    #             X_train, y_train, X_test, y_test, params)
    #     except Exception as e:
    #         print(e)
    elif athm == "GradientBoostingClassifier":
        try:
            clf = gradient_boosting_classifier_algorithm.getParams(params)
            model, evalution, error = gradient_boosting_classifier_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = gradient_boosting_classifier_algorithm.params
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    elif athm == "GradientBoostingRegression":
        try:
            clf = gradient_boosting_regression_algorithm.getParams(params)
            model, evalution, error = gradient_boosting_regression_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = gradient_boosting_regression_algorithm.params
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    elif athm == "LogisticRegression":
        try:
            clf = logistic_regression_algorithm.getParams(params)
            model, evalution, error = logistic_regression_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = logistic_regression_algorithm.params
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    elif athm == "RidgeClassifier":
        try:
            clf = ridge_classifier_algorithm.getParams(params)
            model, evalution, error = ridge_classifier_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = ridge_classifier_algorithm.params
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    elif athm == "SGD_Classifier":
        try:
            clf = SGD_classifier_algorithm.getParams(params)
            model, evalution, error = SGD_classifier_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = SGD_classifier_algorithm.params
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    elif athm == "MLP_Classifier":
        try:
            clf = MLP_classifier_algorithm.getParams(params)
            model, evalution, error = MLP_classifier_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
            if params == None:
                params = MLP_classifier_algorithm.params
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    else:
        try:
            if params == None:
                params = decision_tree_algorithm.params
            clf = decision_tree_algorithm.getParams(params)
            model, evalution, error = decision_tree_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test
            )
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    try:
        return (model, evalution, error, params)
    except UnboundLocalError:
        print("error", clf)
        pass

    # except:
    #     print("[error]--")
