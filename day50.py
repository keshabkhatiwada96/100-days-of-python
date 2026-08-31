# Pandas Reading CSV and JSON   

import pandas as pd

print("-------Data from csv------")

df = pd.read_csv("students.csv")
print(df)


print("---------------Data From Json---------")

df = pd.read_json("students.json")
print(df)