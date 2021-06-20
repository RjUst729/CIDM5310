import pandas as pd

faang = faang.assign(
    date=lambda x: pd.to_datetime(x.date),
    volume=lambda x: x.volume.astype(int)
).sort_values(
    ['date', 'ticker']
)

faang.head()

faang_form = pd.read_csv("faang.csv")
print (faang_form)