import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def data_preparation(data):
    features = data.drop(columns=['target'])
    target = data['target']

    return features, target


def tts(features, target):
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, train_size=0.66, random_state=42)
    return X_train, X_test, y_train, y_test
