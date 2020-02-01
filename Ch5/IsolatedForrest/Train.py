from pyod.models.iforest import IForest
from pyod.utils.data import generate_data
from pyod.utils.data import evaluate_print
import numpy as np
import pickle


X_train = np.loadtxt('X_train.txt', dtype=float)
y_train = np.loadtxt('y_train.txt', dtype=float)
X_test = np.loadtxt('X_test.txt', dtype=float)
y_test = np.loadtxt('y_test.txt', dtype=float)
    
clf = IForest()
clf.fit(X_train)

# get the prediction labels and outlier scores of the training data
#y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
#y_train_scores = clf.decision_scores_  # raw outlier scores

# get the prediction on the test data
y_test_pred = clf.predict(X_test)  # outlier labels (0 or 1)
y_test_scores = clf.decision_function(X_test)  # outlier scores
print(y_test_pred)

# evaluate and print the results
print("\nOn Test Data:")
evaluate_print('IForest', y_test, y_test_scores)

pickle.dump( clf, open( "IForest.p", "wb" ) )