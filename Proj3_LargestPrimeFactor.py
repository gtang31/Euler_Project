"""
Euler Project 3
=================================================================The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

The idea to breaking this down:
Consider number 24, we can have
1 x 24
2 x 12
3 x 8
4 x 6
6 x 4
8 x 3
12 x 2
24 x 1
We can, at most, only check if N is divisble by values that go up to half our number...
(or sqrt(number) to be exact.) 
"""
from math import sqrt
from time import time

# find largest prime factor of number N
N = 600851475143
def largest_prime_factor(N):
    # start at sqrt(600851475143) and decrement
    for i in range(int(sqrt(N)),1,-1):
        condition = True
        # check if i is a factor
        if (N%i == 0):
            # check if i is a prime number
            for j in range(2,i):
                if (i%j == 0):
                    # if number is even divisible, then its not a prime
                    condition = False
                    # no need to check any further
                    break
        else:
            condition = False
        if (condition):
            prime_factor = i
            break
    return prime_factor
start = time()
print largest_prime_factor(N)
end = time()
print "Elapsed: ",end-start
