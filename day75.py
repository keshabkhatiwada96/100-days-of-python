# Neurons, Layers and Activation Functions

studyhrs = 5
attendence = 40


# neuron 1 
weight1 = 0.4
weight2=0.6
bias1 = 2
output1 = (studyhrs*weight1)+(attendence*weight2)+bias1

# neuron2 
weight3=0.3
weight4 =0.7
bias2 = 1
output2=(studyhrs*weight3)+(attendence*weight4)+bias2

print("neuro 1 =",output1)
print("neuro 2 =",output2)

# ReLu activation
if output1>0:
    activated1 = output1
else:
    activated1 = 0

if output2>0:
    activated2 =output2
else:
    activated2=0

print("activated neuron1 = ",activated1)
print("activated neuron2 = ",activated2)