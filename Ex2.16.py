import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\heman\Downloads\country_wise_latest_modified.csv")
plt.figure(figsize=(12, 8))
sns.barplot(x="WHO Region", y="New cases", data=df)
plt.xlabel("WHO Regions")
plt.ylabel("New Cases")
plt.title("New Cases Compared Across Different WHO Regions")
plt.show()