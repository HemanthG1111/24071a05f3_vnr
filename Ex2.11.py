import pandas as pd

df=pd.read_csv(r"C:\Users\heman\Downloads\country_wise_latest_modified.csv")
print("Complete List:\n",df.head())
df=df.head().dropna()

print("List With Dropped Column:\n",df.head())