"""
Euler Project 35
================================================================
The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13,
17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from time import time
from math import sqrt

def isPrime(n):
    # function to check if a number is a prime
    if(n != 2 and n%2 == 0): 
    # even numbers are not prime
        return False
    else:
        prime = True
        for i in xrange(3,int(sqrt(n))+1,2):
            # check if n is divisible
            if (n%i == 0):
                prime = False
                break
    return prime

def primesUpTo(N):
    # find all primes up to N
    sum_of_prime = set()
    for i in xrange(2,N):
        if(isPrime(i)):
            # contains all the prime numbers up to N
            sum_of_prime.add(i)
    return sum_of_prime

def rotateNumbers(s):
    # rotate a string to the right by n places
    rotated_s = set([s])
    s = str(s)
    # rotate each character to the right
    for i in range(len(s)-1,0,-1):
        rotated_s.add(int(s[i:] + s[:i]))
    return rotated_s

start = time()
primes = primesUpTo(10**6)
circular_primes = set()
# begin finding circular primes
for i in primes:
    # skip over known circular primes
    if i not in circular_primes:
        # check if current prime is a circular prime
        # make use of sets, where order does not matter
        if rotateNumbers(i).issubset(primes):
            # if so, combine it
            circular_primes = circular_primes.union(rotateNumbers(i))
end = time()


print len(circular_primes)
print 'Elapsed', end-start
