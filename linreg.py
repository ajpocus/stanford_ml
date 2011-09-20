#!/usr/bin/env python

def linreg(training_set):
    """linreg(training_set): takes a list of [x, y] inputs and returns a
	function that predicts y based on input x
    """

    def cost(f, x, y):
	return (f(x) - y)**2

    coefficients = [1, 1]
    learning_rate = 0.5

    def algo(x):
	return coefficients[1] * x + coefficients[0]

    for (x, y) in training_set:
	i = 0
	lim = len(coefficients)
	while i < lim:
	    coefficients[i] += learning_rate * cost(algo, x, y)
	    i += 1

    return algo

