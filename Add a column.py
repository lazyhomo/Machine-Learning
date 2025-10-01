import pandas as pd
d = [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
df = pd.DataFrame(d)
df.columns = ['Data1'] #adds the existing coloumn name as data1
df['NewCol'] = 6  #creates a new coloumn of NewCol with 6 as its value all the time
print(df)