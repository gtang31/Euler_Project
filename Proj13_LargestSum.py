"""
Euler Project 13
================================================================
Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers.
"""
from numpy import loadtxt
numbers = loadtxt("Proj13_LargestSum.txt")
numbers = str(sum(numbers))[0:11]
print numbers.replace('.','')
