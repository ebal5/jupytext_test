import pandas as pd
from sklearn.datasets import load_iris

def load_iris_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target.astype(int)
    df['target_names'] = df['target'].apply(lambda x: iris.target_names[x])
    return df