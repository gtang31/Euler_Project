"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds
to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from time import time
from math import sqrt

def is_prime(n):
    # function to check if a number is a prime
    if (n == 1): return False
    else:
        for i in xrange(3,int(sqrt(n))+1,2):
            # check if n is divisible
            if (n%i == 0):
                return False
    return True

def primes_up_to(N):
    # find all primes up to N
    sum_of_prime = [2]
    for i in xrange(3,N,2): # even numbers are not prime
        if is_prime(i):
            # contains all the prime numbers up to N
            sum_of_prime.append(i)
    return sum_of_prime

start = time()
primes_list = primes_up_to(10**6)
longest_list = []
for start_here in xrange(len(primes_list)/1000+1):
    # start our consecutive list with different prime numbers
    index = start_here
    consec_primes = []
    while sum(consec_primes) < 10**6:
        consec_primes.append(primes_list[index])
        index += 1
    consec_primes.pop(-1)    
    if len(consec_primes) > len(longest_list) and is_prime(sum(consec_primes)):
        longest_list = consec_primes
end = time()

print sum(longest_list)
print 'Elapse', end - start
