from sklearn.naive_bayes import GaussianNB
from algorithm_parent import algorithm
class NAIVE_BAYES_ATHM(algorithm):
    clf = GaussianNB( priors=None, var_smoothing=1e-09)
    pass
