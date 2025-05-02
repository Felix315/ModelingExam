import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(4, 4), index=[1, 2, 3, 4], columns=['a', 'b', 'c', 'd'])
print(df)

print(df.loc[2, 'c'])  # label-based

print(df.iloc[1, 2])  # position-based

print(df["c"][2])  # column "c", then row label 2
