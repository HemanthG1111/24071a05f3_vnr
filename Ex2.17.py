import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\heman\Downloads\country_wise_latest_modified.csv")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Country/Region', y='Confirmed last week', label='Confirmed last week')
sns.lineplot(data=df, x='Country/Region', y='1 week change', label='1 Week Change')
plt.xlabel("Countries/Regions")
plt.ylabel("Confirmed Cases")
plt.title("Comparison of Confirmed Cases")
plt.legend()
plt.show()