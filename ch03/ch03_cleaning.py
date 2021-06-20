import pandas as pd
df = pd.read_csv('data/nyc_temperatures.csv')
df.head()

temps_df=pd.read_csv('data/nyc_temperatures.csv')

#Ln 5 must be adjusted to name the dataframe temps_df.  
# This allows for the print function to display in the terminal

print(temps_df)