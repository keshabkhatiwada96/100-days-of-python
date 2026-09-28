# Build a Simple Neural Network
import numpy as np

# input data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# expected output
y = np.array([
    [0],
    [1],
    [1],
    [1]
])

# weights and bias
weights = np.zeros((2, 1))
bias = np.zeros(1)

learning_rate = 0.1


# sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# training
for epoch in range(10000):

    # prediction
    z = np.dot(X, weights) + bias
    prediction = sigmoid(z)

    # error
    error = prediction - y

    # gradient
    gradient = error * prediction * (1 - prediction)

    weights_gradient = np.dot(X.T, gradient)
    bias_gradient = np.sum(gradient)

    # update weights and bias
    weights -= learning_rate * weights_gradient
    bias -= learning_rate * bias_gradient


# final prediction
prediction = sigmoid(np.dot(X, weights) + bias)

print("prediction:")
print(prediction)

print("rounded predictions:")
print(prediction.round())