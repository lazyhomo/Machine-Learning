import pandas as pd

names = ['Nadeem', 'Kabir', 'Chinnu']
birthdate = [19, 15, 15]

# Create DataFrame
babydf = list(zip(names, birthdate))
df = pd.DataFrame(data=babydf, columns=['Names', 'Births'])

# Save CSV (fixing path and escaping backslashes)
df.to_csv(r"C:\Users\nadaf\Videos\birth.csv", index=False, header=False)

