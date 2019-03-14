LogisticRegression.py
---
This file is meant to generalize the implementation of logistic regression of two target values. Parameters are fit through the
stochastic gradient descent method. Data is read in through two .csv files, "x.csv", and "y.csv" respectively. The input variable data are assumed to contain vertical columns of subsequent features, including the first column being 1's to satisfy the bais term.
A default learning rate of 0.0001 is set, with 10000 number of times to iterate through the training set.

PlotDecisionBoundary.py
---
This implementation was done according to the dataset in "Problem Set #1" in Stanford's CS229 course (Autumn 2017), thereby not
generalizing the plotting process. This function plots the feature space and the estimated decision boundary given a parameter vector.

Results and Conclusion
---
After 100,000 iterations through the training set at a learning rate of 0.0001, the resulting parameters found were -2.6242539, 0.76348427, and 1.17312019 repectively. The scatterplot shows that these values do approximately seperate the data. I am not sure how to determine an appropriate learning rate and iteration amount yet. 
