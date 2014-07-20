"""
Euler Project 6
======================================================================
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
import time
def sum_of_squares():
    sumOfSquares = 0
    for value in range(1,101):
        sumOfSquares += value**2
    return sumOfSquares

def squared_sum():
    squaredSum = 0
    for value in range(1,101):
        squaredSum += value
    return squaredSum**2
start = time.time()
print squared_sum() - sum_of_squares()
end = time.time()
print 'Elapsed',end-start

# alterntive solution, this is faster
def solution(n):
    start = time.time()
    # creates a vector
    L1 = sum([i**2 for i in range(1, n + 1)])
    L2 = [i for i in range(1, n + 1)]
    return (sum(L2))**2 - L1
start = time.time()
print solution(100)
end = time.time()
print 'Elapsed',end-start
