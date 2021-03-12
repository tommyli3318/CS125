import numpy as np
from sklearn import tree
from joblib import load

clf = load('DT_CLF.joblib')

YESTERDAY = 480

sats = []

for TODAY in range(0, 600, 30):

    IDEAL = np.array([[YESTERDAY, TODAY]])

    sats.append( (TODAY, clf.predict(IDEAL) ))

print(sorted(sats, reverse=True))