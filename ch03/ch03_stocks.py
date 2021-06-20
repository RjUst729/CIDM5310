import pandas as pd

sp=pd.read_csv(
    'data/sp500.csv', index_col='date', parse_dates=True
) .drop(columns=['adj_close'])



sp.head(10)\
    .assign(day_of_week=lambda x: x.index.day_name())


#print(sp)

bitcoin = pd.read_csv(
    'data/bitcoin.csv', index_col='date', parse_dates=True
) .drop (columns=['market_cap']
)
#print(bitcoin)

portfolio = pd.concat ([sp, bitcoin], sort=False)\
    .groupby(level='date') .sum()
    

portfolio.head(10) .assign(
    day_of_week=lambda x: x.index.day_name()
)
df.dtypes
