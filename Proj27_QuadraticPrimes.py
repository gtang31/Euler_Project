"""
Euler discovered the remarkable quadratic formula:
n² + n + 41
It turns out that the formula will produce 40 primes for the
consecutive values n = 0 to 39. However, when
n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41² + 41 + 41 is clearly divisible
by 41.
The incredible formula  n² − 79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for
consecutive values of n, starting with n = 0.
"""

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

from math import sqrt
from time import time
listPrime = []
size = 0
start = time()
for a in range(-1000,1001):    
    for b in range(1,1001):
        if(isPrime(b)):
            for n in range(1001):
                if(n**2+a*n+b < 0):
                    # do not care about negatives
                    break
                elif(isPrime(n**2+a*n+b)):
                    listPrime.append(n**2+a*n+b)
                else:
                    # n needs to be consecutive
                    break
        if(len(listPrime) > size):
            size = len(listPrime)
            # reset list and save a b
            best_a = a
            best_b = b
        listPrime = []
end = time()
print best_a,best_b
print end-start
