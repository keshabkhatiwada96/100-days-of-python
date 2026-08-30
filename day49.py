# Pandas: Series and DataFrames
# Pandas is a Python library used for working with structured and tabular data.
import pandas as pd

# Series
marks = pd.Series(
    [80, 75, 90],
    index=["Keshab", "Ram", "Sita"]
)

print("Marks:")
print(marks)

print("-----------------")

print("Keshab's marks:", marks["Keshab"])

print("--------------------")

# DataFrame
data = {
    "Name": ["Keshab", "Ram", "Sita"],
    "Age": [20, 21, 20],
    "Marks": [80, 75, 90]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("-----------")

# Select column
print(df["Name"])

print("-------------")

# Select row
print(df.iloc[0])

print("------------------")

# DataFrame information
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Data Types:")
print(df.dtypes)

print("----------------------")

# First rows
print(df.head(2))

print("-----------")

# Filtering
print("students scoring above 75:")
print(df[df["Marks"] > 75])