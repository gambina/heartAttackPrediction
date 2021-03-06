import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def prediction(clf, data):
    result = clf.predict(data)
    return result
