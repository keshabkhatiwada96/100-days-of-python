#  ml mini project

import pandas as pd

# student data
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "attendance": [50, 55, 60, 65, 70, 75, 85, 90],
    "result": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("student data:")
print(df)

# features
X = df[["study_hours", "attendance"]]

# target
y = df["result"]

print("features:")
print(X)

print("target:")
print(y)