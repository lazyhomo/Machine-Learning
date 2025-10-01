import pandas as pd
# List of Tuples
empoyees = [(11, 'Jack',    44, 'Sydney',   19) ,
            (12, 'Riti',    41, 'Delhi' ,   17) ,
            (13, 'Aadi',    46, 'New York', 11) ,
            (14, 'Mohit',   45, 'Delhi' ,   15) ,
            (15, 'Veena',   43, 'Delhi' ,   14) ,
            (16, 'Shaunak', 42, 'Mumbai',   10 ),
            (17, 'Shaun',   40, 'Colombo',  12)]
# Create a DataFrame object
df = pd.DataFrame(  empoyees,
                    columns=['ID', 'Name', 'Age', 'City', 'Experience'],
                    index=['b', 'd', 'a', 'c', 'g', 'f', 'e'])
# Sort DataFrame by column 'Experience'
#df = df.sort_values(by=['Name']) #By name sorts the list in the alphabetic order
#df = df.sort_values(by=['Experience'], ascending=True) #By Experience sorts the list in the order of ascedbning or descending
# Sort DataFrame by the Row Index labels in order of a,b,c,d,e,f,g,h
#df = df.sort_index()
# Sort DataFrame by the Column Names
df = df.sort_index(axis=1) #alphabetical ord3er of the coloumns
#Here, axis=1 sorted the columns (a, b, c).
#If it were axis=0, it would sort by the row indices (0,1,…).
# Display the DataFrame
print(df)