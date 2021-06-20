import pandas as pd

covid = pd.read_csv('data/covid19_cases.csv').assign(
    date=lambda x: pd.to_datetime(x.dateRep, format='%d/%m/%Y')
).set_index('date').replace(
    'United_States_of_America', 'USA'
).replace('United_Kingdom', 'UK').sort_index()

covid[
    covid.countriesAndTerritories.isin([
        'Argentina', 'Brazil', 'China', 'Colombia', 'India', 'Italy', 
        'Mexico', 'Peru', 'Russia', 'Spain', 'Turkey', 'UK', 'USA'
    ])
].reset_index().pivot(index='date', columns='countriesAndTerritories', values='cases').fillna(0)

print (covid)