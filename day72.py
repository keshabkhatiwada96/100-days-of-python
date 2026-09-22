#  Overfitting and Underfitting 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
study_hours=[[1],[2],[3],[4],[5],[6],[7],[8]]
marks = [40,45,52,59,68,78,88,98]

X_train,X_test,y_train,y_test = train_test_split(
    study_hours,
    marks,
    test_size = 0.25,
    random_state=42
)

overfit_model = DecisionTreeRegressor(max_depth=None, random_state=42)
overfit_model.fit(X_train,y_train)

print("+++++++++ovefit model++++++++++")
train_score = overfit_model.score(X_train, y_train)
test_score = overfit_model.score(X_test, y_test)
print("training score =", train_score)
print("testing score =", test_score)

print("+++++++++underfit model++++++++++")
underfit_model=DecisionTreeRegressor(max_depth=1)
underfit_model.fit(X_train,y_train)
train_score = underfit_model.score(X_train,y_train)
test_score = underfit_model.score(X_test,y_test)
print("training score =", train_score)
print("testing score =", test_score)