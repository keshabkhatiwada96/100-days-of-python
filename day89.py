#  relu activation practice

import torch

# input values
x = torch.tensor([-5.0, -2.0, 0.0, 3.0, 7.0])

# relu activation
relu = torch.nn.ReLU()

# apply relu
output = relu(x)

print("input:")
print(x)

print("relu output:")
print(output)