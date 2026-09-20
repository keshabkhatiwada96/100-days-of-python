# Accuracy, Precision and Recall
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

#stdent data
study_hours = [[1.5], [2.0], [2.5], [3.0], [4.0], [4.5], [5.0], [6.0]]
pass_or_fail = ["fail", "fail", "fail", "fail", "pass", "pass", "pass", "pass"]
X_train,X_test,y_train,y_test = train_test_split (
    study_hours,
    pass_or_fail,
    test_size=0.25,
    random_state=42
 )
print("Training data:", X_train)
print("Testing data:", X_test)

# creating model
model = LogisticRegression()
print("model created sucesfully")

# training model
model.fit (X_train,y_train)
print("model tarined")

predictions = model.predict(X_test)

print("Actual result:", y_test)
print("Predicted result:", predictions)


# checking accuray
accuracy = accuracy_score(y_test, predictions)
print("Accuracy =", accuracy)

# checking precison
precision = precision_score(y_test, predictions, pos_label="pass")
print("precision =", precision)

# recall 
recall = recall_score(y_test, predictions, pos_label="pass")
print("reecall =", recall)