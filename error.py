class ERROR:
    error_params = {
        'error_params_linearRegression': {'errorParams': "Function parameters LinearGression, Please check your parameters again, with Linear Regression, 'fitIntercept' and 'normalize' is 'True or False'"},
        'error_params_decisionTree': {'errorParams': "Function parameters Decision Tree, Please check your parameters again, with Decision Tree, 'criterion' is 'gini or entropy', 'splitter' is 'best or random', 'maxdepth and minsample' is 'int'"},
        'error_params_naiveBayes': {"errorParams": "Function parameters Naive Bayes, Please check your parameters again, with Naive Bayes, varSmoothing is 'float' ex: 0.00001"},
        'error_params_randomForest': {"errorParams": "Function parameters Random Forest, Please check your parameters again, with Random Forest, 'nEstimator' is 'int ex:100', 'criterion' is 'gini or entropy', 'maxdepth and minSample is int ex: 3 "},
        'error_params_SVM': {"errorParams": "Function parameters SVM (Support Vector Machine), Please check your parameters again, with SVM (Support Vector Machine), 'param C' is 'number ex: 1 or 0.001, 10, 100...', 'gamma' is '0 < float < 1.0 ex: 0.3', 'degree' is 'int ex: 3' "},
        'error_params_GradientBoostingClassifier': {"errorParams": "Function parameters GradientBoosting, Please check your parameters again, with GradientBoosting, 'param 'learning_rate' is 'float', 'nEStimator' is 'int ex: 100', 'subsample' is float  "},
        'error_params_GradientBoostingRegression': {"errorParams": "Function parameters GradientBoosting, Please check your parameters again, with GradientBoosting, 'param loss' is 'ls, lad, huber or quantile', 'learning_rate' is 'float', 'nEStimator' is 'int ex: 100', 'subsample' is float, 'criterion' is 'friedman_mse, mse, mae',  "},
        'error_params_Logistic_regression': {"errorParams": "Function parameters logistic regression, please check your parameters again, with logistic regression, params 'pebalty' is 'l1, l2 or elasticnet', tol, C and interceptScaling is floar number (ex: 0.001)"},
        'error_params_ridge_classifier': {"errorParams": "Function parameters ridge classifier, please check your parameters again, with ridge classifier, params alpha is float (ex: 0.001), max_inter is int (ex:3)"},
        'error_params_SGD': {"errorParams": "Function parameters SGD classifier, please check your parameters again"},
    }
    error_type = {
        'error_feature_label': {"errorType": "Your data set type is incorrect (feature and label), you have to check it again "}
    }

    pass
