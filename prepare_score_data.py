import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def fetching_data():
    scoring_data = pd.DataFrame(columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
                                         'exang', 'oldpeak', 'slope', 'ca', 'thal'])

    scoring_data['thal'] = pd.DataFrame(
        np.random.randint(0, 4, size=(100, 1)), columns=['thal'])
    scoring_data['ca'] = pd.DataFrame(
        np.random.randint(0, 5, size=(100, 1)), columns=['ca'])
    scoring_data['slope'] = pd.DataFrame(
        np.random.randint(0, 3, size=(100, 1)), columns=['slope'])
    scoring_data['oldpeak'] = pd.DataFrame(
        np.random.randint(0, 7, size=(100, 1)), columns=['oldpeak'])
    scoring_data['exang'] = pd.DataFrame(
        np.random.randint(0, 2, size=(100, 1)))
    scoring_data['thalach'] = pd.DataFrame(
        np.random.randint(70, 204, size=(100, 1)))
    scoring_data['restecg'] = pd.DataFrame(
        np.random.randint(0, 3, size=(100, 1)))
    scoring_data['fbs'] = pd.DataFrame(np.random.randint(0, 2, size=(100, 1)))
    scoring_data['chol'] = pd.DataFrame(
        np.random.randint(51, 565, size=(100, 1)))
    scoring_data['trestbps'] = pd.DataFrame(
        np.random.randint(94, 201, size=(100, 1)))
    scoring_data['cp'] = pd.DataFrame(np.random.randint(0, 4, size=(100, 1)))
    scoring_data['sex'] = pd.DataFrame(np.random.randint(0, 2, size=(100, 1)))
    scoring_data['age'] = pd.DataFrame(
        np.random.randint(29, 78, size=(100, 1)))

    return scoring_data


def select_random_point(scoring_data):
    rownum = np.random.randint(1, 101)
    latest_data = scoring_data[rownum:rownum+1]
    return latest_data
