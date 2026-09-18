# Classification Basics and Logistic Regression

from sklearn.linear_model import LogisticRegression

study_hours= [[1], [6], [5], [4], [2], [3]]
pass_or_fail= ["fail","pass","pass","pass","fail","fail"]

# creating model
model = LogisticRegression()
print("model sucesfully created")

# traing model
model.fit(study_hours,pass_or_fail)
print("model trained ")

# making predction
predictions = model.predict([[2], [1], [7],[9]])
print("pass or fail = ",predictions)
