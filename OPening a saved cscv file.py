import pandas as pd
import numpy as np
from pandas import DataFrame


df = pd.read_csv(r"C:\Users\nadaf\Videos\birth.csv", names =['Names','Births'])

print(df.head(2))
print(df.tail(2))
print(df.head(-2))
print(df.columns)