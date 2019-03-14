import numpy as np
import matplotlib.pyplot as plt

def sigmoid(parameters, features):
    output = 0
    for i in range(0, parameters.size):
        output += parameters[i]*features[i] #inner product of parameters and features
    output = 1/(1 + np.exp(-output)) #sigmoid function
    return output;

def gradientDescent(parameters, features, targets, index):
    alpha = 0.0001 #learning rate
    change = 0
    for i in range(0, parameters.size):
        #stochastic method
        change = alpha*(sigmoid(parameters, features[index]) - targets[index])*features[index][i]
        parameters[i] -= change

x = np.loadtxt('x.csv', delimiter = ',')
x = x.reshape(x.shape[0], x.shape[1])
y = np.loadtxt('y.csv', delimiter = ',')
y = y.reshape(y.size, 1)
#print(x)
#print(y)

#initialize parameter vector
theta = np.zeros((x.shape[1],1))
for i in range(0, 10000): # number of time to iterate through the training set
    for j in range(0, x.shape[0]): 
        gradientDescent(theta, x, y, j)
        
print(theta)
plotDescisionBounary(x, y, theta)