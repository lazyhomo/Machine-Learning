
import pandas as pd
import numpy as np
from pandas import DataFrame

d = {'Car': pd.Series([3,4,5,6,7], index =['1','2','3','4','5']),'Bike': pd.Series([3,4,5,6,7], index =['1','2','3','4','5'])}
df = pd.DataFrame(d)
print(df)

print(df.shape)
print(df.size)
print(df.dtypes)