# ReLU Activation with Negative and Positive Outputs

studyhrs = 5
attendance = 40

# neuron 1 - positive output
weight1 = 0.4
weight2 = 0.6
bias1 = 2
output1 = (studyhrs * weight1) + (attendance * weight2) + bias1

# neuron 2 - negative output
weight3 = -0.5
weight4 = 0.2
bias2 = -2
output2 = (studyhrs * weight3) + (attendance * weight4) + bias2

# neuron 3 - negative output
weight5 = -0.3
weight6 = 0.1
bias3 = -1
output3 = (studyhrs * weight5) + (attendance * weight6) + bias3

print("neuron 1 =", output1)
print("neuron 2 =", output2)
print("neuron 3 =", output3)

# ReLU activation

if output1 > 0:
    activated1 = output1
else:
    activated1 = 0

if output2 > 0:
    activated2 = output2
else:
    activated2 = 0

if output3 > 0:
    activated3 = output3
else:
    activated3 = 0

print("activated neuron1 =", activated1)
print("activated neuron2 =", activated2)
print("activated neuron3 =", activated3)