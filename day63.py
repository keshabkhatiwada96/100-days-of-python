# Training data vs Testing data

from sklearn.model_selection import train_test_split

study_hours = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
marks = [40,48,55,62,68,75,80,85,90,95]

print("study hours: ",study_hours)
print('marks',marks)

X_train,X_test,y_train,y_test = train_test_split(
    study_hours,
    marks,
    test_size=0.2,
    random_state=42
)
print("training data :",X_test)
print("testing data :",X_test)
print("training marks :",y_test)
print("testing marks :",y_test)