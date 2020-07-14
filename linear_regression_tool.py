from sklearn.linear_model import LinearRegression
from algorithm_parent import algorithm
class LINEAR_REGRESSION_ATHM(algorithm):
    clf = LinearRegression(fit_intercept = True, normalize = False)
    pass