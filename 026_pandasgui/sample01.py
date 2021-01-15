import pandas as pd
from pandasgui import show

df = pd.read_csv('iris.csv')
gui = show(df)
