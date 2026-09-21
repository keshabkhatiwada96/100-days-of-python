# Confusion Matrix 
from sklearn.metrics import confusion_matrix

actual = ("fail","pass","pass","pass","fail","fail")
predicted = ("pass","pass","fail","pass","fail","fail")

matrix = confusion_matrix(actual,predicted)
print(matrix)