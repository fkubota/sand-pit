from sklearn.datasets import load_iris
import pandas as pd
from ipdb import set_trace as st

iris = load_iris()
data = iris.data
target = iris.target
feat_names = iris.feature_names

df = pd.DataFrame(data, columns=feat_names)
df['target'] = target

df.to_csv('iris.csv', index=False)
