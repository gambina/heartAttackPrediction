from os import name
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from read_data import load_data
from prepare_data import data_preparation, tts
from model_train import training
from model_predict import prediction
from prepare_score_data import fetching_data, select_random_point
import pickle
from pickle_handler import save_model, load_model


def run():
    os.chdir('/app')
    data = load_data()
    features, target = data_preparation(data)
    X_train, X_test, y_train, y_test = tts(features, target)
    clf = training(X_train, y_train)

    modelname = save_model(clf)

    # In loop for 4 times
    i = 0
    while i < 4:
        scoring_data = fetching_data()
        latest_data = select_random_point(scoring_data)
        print(latest_data)

        loaded_model = load_model(modelname)
        result = loaded_model.predict(latest_data)

        #result = prediction(clf, latest_data)
        i = i+1
        print("Predicted result: ", result)


if __name__ == '__main__':
    pd.options.mode.chained_assignment = None
    run()
