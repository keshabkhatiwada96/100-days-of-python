# machine leanring and scikit learn

from sklearn.linear_model import LinearRegression
# training data
study_hours = [[1],[2],[3],[4],[5]]
marks = [40,50,60,70,80]

print("study hours: ", study_hours)
print("marks: ",marks)

# creating machine learning model
model = LinearRegression()
print("ml model created")

# fitting actual data in and training the model
model.fit(study_hours,marks)
print("model trained")

# making our prediction
prediction = model.predict([[6]])
print("predicted marks: ",prediction[0])

# actual concept behind the prediction
print("coefficient:", model.coef_)
print("intercept:", model.intercept_)