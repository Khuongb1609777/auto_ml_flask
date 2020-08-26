from sklearn import metrics
from sklearn.metrics import mean_squared_error
from function_api import API
from error import ERROR


class algorithm:

    # algorithm_dict = {
    #     "LinearRegression": linear_regression_algorithm.getParams(),
    #     "RandomForest": "randomforest_algorithm",
    #     "NaiveBayes": "naive_bayes_algorithm",
    #     "SupportVectorMachine": "svm_algorithm",
    #     "DecisionTree": "decision_tree_algorithm",
    # }

    def models(athm, clf, X_train, X_test, y_train, y_test):
        if(type(clf) is dict):
            model = ""
            error = clf['errorParams']
            evalution = "evalution = 0.0 [error] create model"
            return(model, evalution, error)
        else:
            try:
                # print(athm)
                model = clf.fit(X_train, y_train)
            except ValueError:
                print(
                    "[error] label for linear regression must be continuous data and label for classify must be uncontinuous data")
                model = ""
                error = ERROR.error_type['error_feature_label']['errorType']
                evalution = "evalution = 0.0 [error] create model"
                return(model, evalution, error)
            except TypeError:
                print("[error] can't create model")
                model = ""
                error = ERROR.error_type['error_feature_label']['errorType']
                evalution = "evalution = 0.0 [error] create model"
                return(model, evalution, error)
            except AttributeError:
                print("error", clf)
                model = ""
                error = ERROR.error_type['error_feature_label']['errorType']
                evalution = "evalution = 0.0 [error] create model"
                return(model, evalution, error)
            try:
                evalution = 0.0
                error = ""
                y_pred = model.predict(X_test)
                if athm == "LinearRegression":
                    evalution = mean_squared_error(y_test, y_pred)
                else:
                    evalution = 100 * metrics.accuracy_score(y_test, y_pred)
                return model, evalution, error
            except ValueError:
                print(
                    "[Error] can't calculate evalution (algorithm_parent functions model")
                model = ""
                error = ERROR.error_type['error_feature_label']['errorType']
                evalution = "evalution = 0.0 [error] create model"
                return(model, evalution, error)
            except TypeError:
                print("[Error] model is not exist")
                model = ""
                error = ERROR.error_type['error_feature_label']['errorType']
                evalution = "evalution = 0.0 [error] create model"
                return(model, evalution, error)
            except AttributeError:
                print(AttributeError)
                model = ""
                error = ERROR.error_type['error_feature_label']['errorType']
                evalution = "evalution = 0.0 [error] create model"
                return(model, evalution, error)
    pass
