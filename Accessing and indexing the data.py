import pandas as pd
d = [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
df = pd.DataFrame(d)
df.columns = ['Data1'] #adds the existing coloumn name as data1
df['NewCol'] = 6

df['Data1'] = df['Data1'] - 2
df['NewCol'] = df['NewCol'] + 2
df['NewCol'] = 3 * df['NewCol']
del df['NewCol']  #deletes the coloumn NewCol
# Edit the index name
df.index=['a','b','c','d','e','f','g','h','i','j']
# Reading specific column values
df['Data1']
# Find based on index value
df.at['c','Data1']
print(df)