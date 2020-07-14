from sklearn.svm import SVC
from algorithm_parent import algorithm
class SVM_ATHM(algorithm):
    clf = SVC(C = 1.0, gamma = 0.5, degree= 3 )
    pass






