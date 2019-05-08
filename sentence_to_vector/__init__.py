import csv
import numpy as np
from os.path import dirname, join


class Bunch(dict):
    def __init__(self, **kwargs):
        super(Bunch, self).__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)


def load_data(module_path, data_file_name):

    with open(join(module_path, data_file_name)) as csv_file:
        data_file = csv.reader(csv_file)
        n_samples = 29022
        n_features = 3

        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[:-1], dtype=np.float64)
            target[i] = np.asarray(ir[-1], dtype=np.int)

    return data, target


def load_iris():
    module_path = dirname(__file__)
    data, target = load_data(module_path, 'datasets.csv')

    return Bunch(data=data, target=target,
                 # target_names=target_names,
                 # DESCR=fdescr,
                 feature_names=['sepal length (cm)', 'sepal width (cm)',
                                'petal length (cm)', 'petal width (cm)'])

