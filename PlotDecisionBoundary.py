import numpy as np
import matplotlib.pyplot as plt

def plotDescisionBounary(x, y, theta):
    x1 = x[:,1]
    x1 = x1.reshape(x1.size, 1)
    x10 = np.ndarray((50, 1)) #feature 1 values corresponding to y = 0
    for i in range(0, 50):
        x10[i] = x1[i]

    x11 = np.ndarray((49, 1)) #feature 1 values corresponding to y = 1
    for i in range(50, 99):
        x11[i-50] = x1[i]

    x2 = x[:,2]
    x2 = x2.reshape(x1.size, 1)
    x20 = np.ndarray((50, 1)) #feature 2 values corresponding to y = 0
    for i in range(0, 50):
        x20[i] = x2[i]

    x21 = np.ndarray((49, 1)) #feature 2 values corresponding to y = 1
    for i in range(50, 99):
        x21[i-50] = x2[i]

    plt.scatter(x10, x20)
    plt.scatter(x11, x21)

    decisionBoundary = np.ndarray((99,1))
    for i in range(0, 99):
        #decision boundary values are found by solving sigmoid(theta*x) = 0.5
        decisionBoundary[i] = (-1*theta[0]-(theta[1]*x1[i]))/theta[2]
    
    plt.plot(x1, decisionBoundary, color = 'k', lw = 0.5)
    plt.savefig('ScatterPlot')