import json
import numpy as np
import os
import pickle
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression

import pickle
from sklearn.externals import joblib

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=66)



clf = joblib.load(os.path.join(os.getcwd(), 'model_alpha_0.1.pkl'))
y_hat = clf.predict(X_test)
print(y_hat)