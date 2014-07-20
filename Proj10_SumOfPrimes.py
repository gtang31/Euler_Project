"""
Euler Project 10
======================================================================
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import time
from math import sqrt

# function to check if a number is a prime
def isPrime(n):
    # even numbers are not prime
    if(n != 2 and n%2 == 0):
        return False
    else:
        prime = True
        for i in range(3,int(sqrt(n))+1,2):
            # check if n is divisible
            if (n%i == 0):
                prime = False
                break
    return prime

# find the sum of all primes up to N
def sumOfPrime(N):
    sum_of_prime = []
    for i in range(3,N):
        if(isPrime(i)):
            # contains all the prime numbers up to N
            # .append() faster than using +=
            sum_of_prime.append(i)
    return sum(sum_of_prime)+1

start = time.time()
print sumOfPrime(2000000)
#print isPrime(1)
end = time.time()
print 'Elapse',end-start
