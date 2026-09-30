# Neural Network Mini Project 

import torch

#input data 
X = torch.tensor([
    [1.0, 50.0],
    [2.0, 60.0],
    [3.0, 70.0],
    [4.0, 80.0],
    [5.0, 90.0]
])

# expected result
y =torch.tensor([
    [0.0],
    [0.0],
    [0.0],
    [1.0],
    [1.0]
])

# neural network
model = torch.nn.Sequential(
    torch.nn.Linear(2, 4),
    torch.nn.ReLU(),
    torch.nn.Linear(4, 1),
    torch.nn.Sigmoid()
)

# loss function
loss_function = torch.nn.BCELoss()

# optimizer
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

# training
for epoch in range (1000):
    # prediction
    predction = model(X)

    # loss calculation
    loss = loss_function(predction,y)

    # gradients calculation
    loss.backward()

    # weights update
    optimizer.step()

    # clearing gradients
    optimizer.zero_grad()

# new studnet
new_student = torch.tensor([[4.5, 85.0]])
predctions = model(new_student)

print("predictiona: ")
print(predctions)

print("round predictiona: ")
print(predctions.round())
