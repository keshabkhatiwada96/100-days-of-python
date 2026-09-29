#day 79 Training, Loss and Optimizers
import torch 

# input data
X = torch.tensor([[1.0],[2.0],[3.0],[4.0]])

# expected output
y = torch.tensor([[2.0],[4.0],[6.0],[8.0]])

# weights & bias
weight = torch.tensor([[0.0]],requires_grad=True)
bias = torch.tensor([[0.0]],requires_grad=True)

# loss function
loss_function = torch.nn.MSELoss()

# optimizer
optimizer = torch.optim.SGD([weight,bias], lr = 0.01)

# training
for epoch in range(1000):
    # prediction
    prediction = X*weight+bias

    # calculate_loss
    loss = loss_function(prediction,y)

    # calculate_gradients
    loss.backward()

    # updated weight and bias
    optimizer.step()

    # removing old gradients
    optimizer.zero_grad()

print("weight =", weight)
print("bias =", bias)

print("prediction:")
print(X * weight + bias)