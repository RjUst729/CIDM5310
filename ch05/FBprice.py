import matplotlib.pyplot as pyplot
import pandas as pandas

fb = pd.read_csv(
    'data/fb_stock_prices_2018.csv',
    index_col='date',
    parse_dates=True
)