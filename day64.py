#Trainig vs Testing data 2nd project

from sklearn.model_selection import train_test_split

study_hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
marks = [35, 45, 52, 60, 67, 73, 79, 84, 91, 96]
print("study hours: ",study_hours)
print('marks',marks)

X_train, X_test, y_train, y_test = train_test_split(
    study_hours,
    marks,
    test_size=0.3,
    random_state=42
)

print("Training data:", X_train)
print("Testing data:", X_test)
print("Training marks:", y_train)
print("Testing marks:", y_test)