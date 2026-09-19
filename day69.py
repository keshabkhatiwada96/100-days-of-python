# Logistic Regression with float data 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#stdent data
study_hours = [[1.5], [2.0], [2.5], [3.0], [4.0], [4.5], [5.0], [6.0]]
pass_or_fail = ["fail", "fail", "fail", "fail", "pass", "pass", "pass", "pass"]


X_train, X_test, y_train, y_test = train_test_split(
    study_hours,
    pass_or_fail,
    test_size=0.25,
    random_state=42
)
print("Training data:", X_train)
print("Testing data:", X_test)
#creating model
model = LogisticRegression()
print("model successfully created")
#training model
model.fit(X_train, y_train)
print("model trained")
#makng prediction
# making predction
predictions = model.predict([[2.0], [1.0], [7.0],[9.0]])
print("pass or fail = ",predictions)
