from svm_tool import svm_algorithm
from randomforest_tool import randomforest_algorithm
from naive_bayes_tool import naive_bayes_algorithm
from decisiontree_tool import decision_tree_algorithm
from linear_regression_tool import linear_regression_algorithm


def get_athm(athm, params, X_train, X_test, y_train, y_test):
    # try:
    if (athm == "LinearRegression"):
        try:
            clf = linear_regression_algorithm.getParams(params)
            model, evalution = linear_regression_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test)
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    elif(athm == "RandomForest"):
        try:
            clf = randomforest_algorithm.getParams(params)
            model, evalution = randomforest_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test)
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    elif(athm == "NaiveBayes"):
        try:
            clf = naive_bayes_algorithm.getParams(params)
            model, evalution = naive_bayes_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test)
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    elif athm == "SupportVectorMachine":
        try:
            clf = svm_algorithm.getParams(params)
            model, evalution = svm_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test)
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    else:
        try:
            clf = decision_tree_algorithm.getParams(params)
            model, evalution = decision_tree_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test)
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    try:
        return (model, evalution)
    except UnboundLocalError:
        print("[error] clf is not define")
        pass

    # except:
    #     print("[error]--")
