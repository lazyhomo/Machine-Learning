import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

df = pd.read_csv(r"C:\Users\nadaf\Videos\birth.csv", names =['Names','Births'])

df_plot= df['Births'].plot()
print(df_plot)
plt.show()