import pandas as pd

data = {
    'Names':['Alpha','Bravo','Charlie'],
    'IDs':[5,6,7]
}
df = pd.DataFrame(data)

df.to_excel('testdataframe.xlsx') #Need openpyxl library installed
