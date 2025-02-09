import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\heman\Downloads\country_wise_latest_modified.csv")
sns.boxplot(x='Active',y='Country/Region',data=df.head(10))
plt.xlabel("Active cases")
plt.ylabel("Countries")
plt.title("Active cases varying across different countries")
plt.show()