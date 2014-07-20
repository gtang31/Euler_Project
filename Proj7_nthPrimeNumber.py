"""
Euler Project 7
======================================================================
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13. What is the 10 001st prime number?
"""
import math
import time

# function to check if a number is a prime
def isPrime(n):
    # negative numbers are not prime
    if(n <= 1):
        return False
    else:
        prime = True
        for i in range(2,int(round(math.sqrt(n)))+1):
            # check if n is divisible
            if (n%i == 0):
                prime = False
                break
    return prime
"""
n = 29
print n
print isPrime(n)
"""
def nth_prime(nth):
    num = 2
    count = 1
    while count < nth+1:
        if (isPrime(num)):
            # increment counter keeping track # of primes encountered
            count +=1
        # move to next number
        num += 1
    return 'The '+str(nth)+'th prime number is '+str(num)

start = time.time()
print nth_prime(10001)
end = time.time()
print 'Elapsed',end-start
