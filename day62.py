# ML learning with diffn data and multiple study hours
from sklearn.linear_model import LinearRegression
# training data 
study_hours = [[1],[2],[3],[4],[5]]
marks = [40,48,60,67,73]
print('study marks : ', study_hours)
print('marks : ', marks)

# creating ml model

model = LinearRegression()
print('ml model created')

# fiiting data 
model.fit (study_hours,marks)
print('data fitted sucessfully')

# making prediction
prediction = model.predict([[6],[7],[8]])

print("predicted marks 6 hours: ",prediction[0])
print("predicted marks 7 hours: ",prediction[1])
print("predicted marks 8 hours: ",prediction[2])

print('coefficeint: ',model.coef_)
print('intercept: ',model.intercept_)