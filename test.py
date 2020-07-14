from data import DATA
from svm_tool import SVM_ATHM
from decision_tree_tool import DECISION_TREE_ATHM
from naive_bayes_tool import NAIVE_BAYES_ATHM
from linear_regression_tool import LINEAR_REGRESSION_ATHM
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

#   Get form Angular
algorithm = "regression"
# algorithm = "decision_tree"
# algorithm = "svm"
# algorithm = "bayes"
# clf = LinearRegression()

file_tail = "csv"
# file_path = "data_test/iris.csv"    #DATA_TEST for classify
file_path = "data_test/abalone.csv" #DATA_TEST for regression
# col_feature = [0,1,2,3]   # col_feature for classify (iris)
col_feature = [1,2,3,4,5,6,7] # col_feature for regression (abalone)
# col_label = 4   # col_label for classify (iris)
col_label = 8   # col_label for regression (abalone)
size = 0.3
#------------------------------------------------------------------------------------

data,columns,n,m = DATA.read(file_tail,file_path)
X_train, X_test, y_train, y_test = DATA.get_data_train(data,col_feature,col_label,size)
model,evalution = LINEAR_REGRESSION_ATHM.models(algorithm,LINEAR_REGRESSION_ATHM.clf,X_train,X_test,y_train,y_test)

model.predict(X_test)