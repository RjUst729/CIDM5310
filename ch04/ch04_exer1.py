import pandas as pd
import numpy as np

samp = faang.groupby('ticker').resample('1M').agg(
    {
        'open': np.mean,
        'high': np.max,
        'low': np.min,
        'close': np.mean,
        'volume': np.sum
    }
)
print(samp)
