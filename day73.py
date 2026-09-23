# Feature Selection and Basic Feature Engineering
import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "study-hours": [2, 4, 6, 8, 3],
    "attendance": [60, 75, 90, 95, 70],
    "previous-marks": [45, 55, 70, 85, 50],
    "student-id": [101, 102, 103, 104, 105],
    "final-marks": [50, 60, 78, 90, 55]
}
df = pd.DataFrame(data)

selected_features = df[["study-hours", "attendance", "previous-marks"]]
print(selected_features)
print("**************************************************************************")

df["study-attendance-score"] = df["study-hours"] * df["attendance"]
print("study attendance score =", df)
print("****************************************")

X = df[["study-hours", "attendance", "previous-marks", "study-attendance-score"]]
y = df["final-marks"]
print(X)
print(y)

model = LinearRegression()
model.fit(X, y)
print("model created")

prediction = model.predict([[5, 80, 65, 400]])
print("predicted final marks =", prediction)