import pandas as pd

data = {
  "calories": [420, 380, 390, 750, 530, 600 ],
  "duration": [50, 40, 45, 30, 29, 43]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 

locdf = df.loc[1]
print(locdf)
locdf = df.loc[[1,3]]
print(locdf)
newdf = pd.DataFrame(data, index=['a','b','c','d','e','f'])
print(newdf)
locdf = newdf.loc['d']
print(locdf)
locdf = newdf.iloc[::3] #1 print=>leave=>repeat
print(locdf)