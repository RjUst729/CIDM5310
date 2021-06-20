import pandas as pd

my_response = pd.read_csv('data/covid19_total_cases.csv', index_col='index')\
    .T.nlargest(20, 'cases').sort_values('cases', ascending=False)

print(my_response)
