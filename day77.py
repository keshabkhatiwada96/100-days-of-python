import torch

# 1D tensor
numbers = torch.tensor([10, 20, 30, 40, 50])
print("1D Tensor:")
print(numbers)


# 2D tensor
numbers = torch.tensor([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Tensor:")
print(numbers)


# tensor Shape
print("\nShape:")
print(numbers.shape)


# tensor Indexing
print("\nFirst row:")
print(numbers[0])

print("\nFirst value:")
print(numbers[0][0])

print("\nSpecific value:")
print(numbers[1][2])


# tensor Creation
a = torch.zeros(2, 3)
b = torch.ones(2, 3)
c = torch.rand(2, 3)

print("\nZeros:")
print(a)

print("\nOnes:")
print(b)

print("\nRandom:")
print(c)


# basic tensor operations
a = torch.tensor([10, 20, 30])
b = torch.tensor([1, 2, 3])

print("\nAddition:")
print(a + b)

print("\nSubtraction:")
print(a - b)

print("\nMultiplication:")
print(a * b)


# tensor reshaping
numbers = torch.tensor([1, 2, 3, 4, 5, 6])
new_numbers = numbers.reshape(2, 3)
print("\nReshaped Tensor:")
print(new_numbers)


# rensor with requires_grad
x = torch.tensor(5.0, requires_grad=True)
print("Tensor with requires_grad:")
print(x)