import pandas as pd
#read csv file
df = pd.read_csv("bright_stars.csv")
#check number of rows and columns
print(df.shape)

del df["Luminosity"]

print(list(df))

df.to_csv("main.csv")