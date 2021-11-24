import pandas as pd
import numpy as np
from io import StringIO
import os

data = pd.read_csv('CensusDataMini.csv')

print(data)

# df.columns is zero-based pd.Index
# df = df.drop(df.columns[[0, 1, 3]], axis=1)

data.drop(data.columns[[0]], axis=1, inplace=True)

data.to_csv("output_filename.csv", index=False, encoding='utf8')



