import pandas as pd
import numpy as np
from io import StringIO
import os

data = pd.read_csv('CensusDataMini.csv')

# print(data)

# df.columns is zero-based pd.Index
# df = df.drop(df.columns[[0, 1, 3]], axis=1)

# Drops the first column
# data.drop(data.columns[[0]], axis=1, inplace=True)

# There are 16 unique values
# Think about doing it in ranges instead of handeling it by each case'
# Doing it in groups of 4, so (4, 8, 12, 16)
# We could k anaomize each of the groups and and will ganrantee the l diversity for each group 


group = data.groupby(['Race'])

print(group.size())

data.to_csv("lCensusData.csv", index=False, encoding='utf8')
