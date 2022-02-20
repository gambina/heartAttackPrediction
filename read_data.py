import numpy as np
import pandas as pd


def load_data():
    dataset = pd.read_csv("heart.csv")
    return dataset
