import numpy as np
import pandas as pd

df = pd.read_csv('data/earthquakes.csv')

#print(df.empty)
#print(df.shape)
#print(df.head())
#print(df.tail(3))

#print(df.info())
#print(df.describe())
print(df.describe(include=object))

#print(df[['mag', 'title']][100:105])





