import pandas as pd

data = {
    'Names':['Alpha','Bravo','Charlie'],
    'IDs':[5,6,7]
}
df = pd.DataFrame(data)

print(df[df['IDs']>4])