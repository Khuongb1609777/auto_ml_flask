from sklearn import metrics
from sklearn.metrics import mean_squared_error
class algorithm:
    def models(athm,clf,X_train, X_test, y_train, y_test):
        clf = clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        if athm == "regression":
            evalution = mean_squared_error(y_test,y_pred)
        else:
            evalution = 100 * metrics.accuracy_score(y_test,y_pred)
        return clf,evalution
    pass


