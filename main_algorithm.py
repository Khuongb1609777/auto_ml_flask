from svm_tool import svm_algorithm
from randomforest_tool import randomforest_algorithm
from naive_bayes_tool import naive_bayes_algorithm
from decisiontree_tool import decision_tree_algorithm
from linear_regression_tool import linear_regression_algorithm


def get_athm(athm, X_train, X_test, y_train, y_test, params=None):
    # try:
    if (athm == "LinearRegression"):
        try:
            clf = linear_regression_algorithm.getParams(params)
            model, evalution, error = linear_regression_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test)
        except TypeError:
            pass
        except UnboundLocalError:
            pass
        except ValueError:
            pass
    elif(athm == "RandomForest"):
        try:
            clf = randomforest_algorithm.getParams(params)
            model, evalution, error = randomforest_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test)
        except TypeError:
            print("co loi xay ra", clf['errorParams'])
            pass
        except UnboundLocalError:
            print("co loi xay ra", clf['errorParams'])
            pass
    elif(athm == "NaiveBayes"):
        try:
            clf = naive_bayes_algorithm.getParams(params)
            model, evalution, error = naive_bayes_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test)
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
            model, evalution, error = decision_tree_algorithm.models(
                athm, clf, X_train, X_test, y_train, y_test)
        except TypeError:
            print("[error] clf is not define")
            pass
        except UnboundLocalError:
            print("[error] clf is not define")
            pass
    try:
        return (model, evalution, error)
    except UnboundLocalError:
        print("error", clf)
        pass

    # except:
    #     print("[error]--")
