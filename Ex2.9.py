import pandas as pd

data1 = {
    'Names' : ['Aplha','Bravo','Charlie'],
    'IDs' : [5,6,7]
}
data2 = {
    'Names' : ['Delta','Echo','Foxtrot'],
    'IDs' : [8,9,10]
}

print(pd.concat([pd.DataFrame(data1),pd.DataFrame(data2)],axis=1))