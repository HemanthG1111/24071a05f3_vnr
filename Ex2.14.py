import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\heman\Downloads\country_wise_latest_modified.csv")
plt.scatter(df["Confirmed"], df["Deaths"], color="green")
plt.xlabel("Confirmed cases")
plt.ylabel("Deaths")
plt.title("Scatter Plot")
plt.show()