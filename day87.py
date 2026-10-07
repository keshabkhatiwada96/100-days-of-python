# day 87 - classification vs regression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

# regression data
X_reg = [[1], [2], [3], [4], [5]]
y_reg = [10, 20, 30, 40, 50]

# classification data
X_class = [[1], [2], [3], [4], [5]]
y_class = [0, 0, 0, 1, 1]

# regression model
regression_model = LinearRegression()

# classification model
classification_model = LogisticRegression()

# train regression model
regression_model.fit(X_reg, y_reg)

# train classification model
classification_model.fit(X_class, y_class)

# regression prediction
regression_prediction = regression_model.predict([[6]])

# classification prediction
classification_prediction = classification_model.predict([[3]])

print("regression prediction:")
print(regression_prediction)

print("classification prediction:")
print(classification_prediction)