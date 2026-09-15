# Training and Testing ML practice3 
from sklearn.model_selection import train_test_split

excercise_hours = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
calories_burnt = [100, 180, 250, 320, 400, 470, 540, 620, 700, 780]
X_train, X_test, y_train,y_test = train_test_split(
    excercise_hours,
    calories_burnt,
    test_size=0.3,
    random_state=42
)
print("training data",X_train)
print("testing data",X_test)
print("training data",y_train)
print("testing data",y_test)

