import pickle
import os
from datetime import datetime


def dummy():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '/artifacts')
    print(filename)


def save_model(clf):
    dirname = os.path.dirname(__file__)
    # filename = os.path.join(dirname, '/artifacts')
    filename = dirname+'/artifacts'+"/clf_model_" + \
        datetime.now().strftime('%Y-%m-%d_%H:%M:%S')+".pkl"
    pickle.dump(clf, open(filename, 'wb'))
    return filename


def load_model(filename):
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model


if __name__ == '__main__':
    dummy()
