from sklearn import tree
from algorithm_parent import algorithm
class DECISION_TREE_ATHM(algorithm):
    clf = tree.DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2)
    pass





