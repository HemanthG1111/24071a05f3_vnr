import pandas as pd

df=pd.read_csv(r"C:\Users\heman\Downloads\country_wise_latest_modified.csv")
print("List With Missing values:\n",df.head())
df['New deaths']=df['New deaths'].fillna(5)
df['New recovered']=df['New recovered'].fillna(250)

print("List With Updated values:\n",df.head())