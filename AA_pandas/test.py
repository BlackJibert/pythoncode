import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20190411'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df)
# DF = df.loc[:, ['A', 'B']]
print(df.A)
