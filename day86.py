#  neural network random prediction

import torch

# neural network
model = torch.nn.Sequential(
    torch.nn.Linear(2, 4),
    torch.nn.ReLU(),
    torch.nn.Linear(4, 1),
    torch.nn.Sigmoid()
)

# new student data
new_student = torch.tensor([[5.0, 85.0]])

# prediction
prediction = model(new_student)

print("prediction:")
print(prediction)

print("rounded prediction:")
print(prediction.round())