from sklearn.ensemble import RandomForestClassifier
from algorithm_parent import algorithm
class RANDOM_FORREST_ATHM(algorithm):
    clf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=None, min_samples_split=2)
    pass