import numpy as np
import pandas as pd

data = np.genfromtxt(
    'data/example_data.csv', delimiter=';',
    names=True, dtype=None, encoding='UTF',
)

array_dict = {
    col: np.array([row[i] for row in data])
    for i, col in enumerate(data.dtype.names)

}

place = pd.Series(array_dict['place'], name='place')

place_index = place.index

df = pd.DataFrame(array_dict)

print(df)


#print (array_dict)