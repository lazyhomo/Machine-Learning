import pandas as pd
import numpy as np
from pandas import DataFrame
dates = pd.date_range('20130101', periods=10)
df2 = pd.DataFrame(np.random.randn(10,4), index = dates , columns = list('ABCD'))
print(df2)