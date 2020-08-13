from sklearn import metrics
from sklearn.metrics import mean_squared_error
from function_api import API


class algorithm:

    # algorithm_dict = {
    #     "LinearRegression": linear_regression_algorithm.getParams(),
    #     "RandomForest": "randomforest_algorithm",
    #     "NaiveBayes": "naive_bayes_algorithm",
    #     "SupportVectorMachine": "svm_algorithm",
    #     "DecisionTree": "decision_tree_algorithm",
    # }

    def models(athm, clf, X_train, X_test, y_train, y_test):
        try:
            # print(athm)
            model = clf.fit(X_train, y_train)
        except ValueError:
            print("[error] label for linear regression must be continuous data and label for classify must be uncontinuous data")
            return False
        except TypeError:
            print("[error] can't create model")
            return False
        except AttributeError:
            print("[error] clf is not define")
            return False
        try:
            evalution = 0.0
            y_pred = model.predict(X_test)
            if athm == "LinearRegression":
                evalution = mean_squared_error(y_test, y_pred)
            else:
                evalution = 100 * metrics.accuracy_score(y_test, y_pred)
            return model, evalution
        except ValueError:
            print(
                "[Error] can't calculate evalution (algorithm_parent functions model")
            return False
        except TypeError:
            print("[Error] model is not exist")
            return False
    pass
