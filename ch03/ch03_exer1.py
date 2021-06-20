import pandas as pd

faang = pd.DataFrame()
for ticker in ['fb', 'aapl', 'amzn', 'nflx', 'goog']:
    df = pd.read_csv(f'data/{ticker}.csv')
    # make the ticker the first column
    df.insert(0, 'ticker', ticker.upper())
    faang = faang.append(df)

faang.to_csv('faang.csv', index=False)

faang_form = pd.read_csv("faang.csv")
print (faang_form)
