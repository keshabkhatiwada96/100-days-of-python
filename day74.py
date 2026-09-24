# Simple Neuron Calculation

studyhrs = 5
attendance = 80
 
weight1 = 0.6
weight2=0.4
bias=2

output = (studyhrs*weight1)+(attendance*weight2)+bias
print("neuron output = ",output)

# ReLU activatio
if output>0:
    activated_output = output
else:
    activated_output = 0

print("Activated output = ",activated_output)