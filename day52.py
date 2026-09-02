# Pandas: Cleaning Missing and Duplicate Data

import pandas as pd

data = {
    "Name": ["Keshab", "Ram", "Sita", "Hari"],
    "Age": [20, None, 19, 22],
    "Marks": [80, 65, None, 72]
}

df = pd.DataFrame(data)
print(df)
print('**************')
print(df.isnull())  # isnull() checks whether each value is missing or not
print('***********')
print(df.isnull().sum())    # counts the number of missing values in each column
print('------------')
df["Age"] = df["Age"].fillna(20)  #this fill the missing age with 20
print(df)
print('++++++++++++++')
df = df.dropna()  #removes rows containing any missing value
print(df)
print('--------********+++++++++++/////////')
# creating duplicate data to ensure panda can find duplicate data too
data = {
    "Name": ["Keshab", "Ram", "Sita", "Keshab"],
    "Age": [20, 21, 19, 20],
    "Marks": [80, 65, 90, 80]
}

df = pd.DataFrame(data)
print(df)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print(df.duplicated())   #this checks which rows have been duplicated
print("\\\\\\\\\\\\\\")
df = df.drop_duplicates()    #this remove duplicates row
print(df)