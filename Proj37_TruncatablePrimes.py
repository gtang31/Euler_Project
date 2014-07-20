"""
Euler Project 37
================================================================
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from time import time
from math import sqrt

def is_prime(n):
    # function to check if a number is a prime
    if (n == 1): return False
    elif(n != 2 and n%2 == 0): 
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

def primes_up_to(N):
    # find all primes up to N
    sum_of_prime = set()
    for i in xrange(2,N):
        if(is_prime(i)):
            # contains all the prime numbers up to N
            sum_of_prime.add(i)
    return sum_of_prime

def is_truncatable(n):
    # function to truncate digits off a number
    for i in xrange(1,len(str(n))):
        # truncate number from right and left sides
        if (not is_prime(int(str(n)[i:])) or \
            not is_prime(int(str(n)[:-i]))):
            return False
    return True

start = time()
truncatable_primes = []

for prime in primes_up_to(10**6):
    # check if the first or last digit is a prime
    if str(prime)[0] not in ['2','3','5','7'] or\
       str(prime)[-1] not in ['2','3','5','7']:
        continue
    if is_truncatable(prime):
        truncatable_primes.append(prime)
        
print sum(truncatable_primes)-2-3-5-7
end = time()
print 'Elapsed', end - start
