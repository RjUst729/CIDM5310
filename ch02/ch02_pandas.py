import pandas as pd
import numpy as np
import datetime as dt


my_dataframe = pd.DataFrame(
    [

    {'mag': 5.2, 'place': 'California'},
    {'mag': 1.2, 'place': 'Alaska'},
    {'mag': .5,  'place': 'California'},
    ]
)





quakes_df= pd.read_csv('data/earthquakes.csv')



print(quakes_df)

my_dataframe.to_csv('output.csv', index=False)
#my_dataframe.to_excel('output.xls', index=False)
my_dataframe.to_json('output.json')

print (quakes_df)


