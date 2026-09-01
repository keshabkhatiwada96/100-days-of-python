import pandas as pd

data = {
    "Name": ["Keshab", "Ram", "Sita", "Hari"],
    "Age": [20, 21, 19, 22],
    "Marks": [80, 65, 90, 72]
}

df = pd.DataFrame(data)

print(df)         #this prints whole data frame
print('----------------------')
print(df[['Name','Marks']])   #this prints only the name and marks section
print('------------------')
print(df.iloc[1])   # this prints 2nd row
print(df.iloc[1,2])  #this prints row 1 and column 2
print('--------------')
print(df[df["Marks"]>70])  #only the student marks higher than 70 will be printed
print('---------')
print(df.sort_values('Marks'))  #this will sort marks from lowest to highest 