import pandas as pd
# List of Tuples
data1= [('Jack', 34, 'Sydney', 5) ,
        ('Riti', 31, 'Delhi' , 7) ,
        ('Aadi', 46, 'New York', 11)]
# List of Tuples
data2= [('Mohit', 34, 'Tokyo', 11) ,
        ('Veena', 31, 'London' , 10) ,
        ('Shaun', 36, 'Las Vegas', 12)]
# List of Tuples
data3= [('Mark', 47, 'Mumbai',   13) ,
        ('Jose', 43, 'Yokohama', 14) ,
        ('Ramu', 49, 'Paris',    15)]
# Create a DataFrame object from list of tuples
firstDf = pd.DataFrame( data1,
                        columns=['Name', 'Age', 'City', 'Experience'],
                        index = ['a', 'b', 'c'])

# Display the First DataFrame
#print(firstDf)
# Create a DataFrame object from list of tuples
secondDF = pd.DataFrame(data2,
                        columns=['Name', 'Age', 'City', 'Experience'],
                        index = ['d', 'e', 'f'])

# Display the second DataFrame
#print(secondDF)
# Create a DataFrame object from list of tuples
thirdDF = pd.DataFrame( data3,
                        columns=['Name', 'Age', 'City', 'Experience'],
                        index = ['g', 'h', 'i'])

# Display the third DataFrame
#print(thirdDF)
# Concatenate three DataFrames along the Rows
df = pd.concat([firstDf, secondDF, thirdDF])
# Display the Concatenated DataFrame
print(df)