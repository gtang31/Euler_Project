"""
Euler Project 26
======================================================================
A unit fraction contains 1 in the numerator. The decimal
representation of the unit fractions with denominators 2 to 10
are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring
cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""

from time import time
from math import sqrt
from decimal import *

# set decimal precision up to 5000 digits
getcontext().prec = 5000

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

# find all primes up to N
def PrimeNumbers(N):
    sum_of_prime = []
    for i in range(2,N):
        if(isPrime(i)):
            # contains all the prime numbers up to N
            sum_of_prime.append(i)
    return sum_of_prime
  
start = time()
recurring_cycle = ''
biggest_number = 0
for i in PrimeNumbers(1000):
    sequence = ''
    # leave out "0."
    decimal_value = str(Decimal(1)/Decimal(i))[2:]
    # begin finding recurring decimal cycles for each number
    for j in range(len(decimal_value)):
        if decimal_value[j] not in sequence:
            # add to our sequence if new value detected
            sequence += decimal_value[j]
        # if we have 2 consecutive 0's we add it anyway
        elif decimal_value[j] == '0' and decimal_value[j] == decimal_value[j-1]:
            sequence += decimal_value[j]
        else: 
            cache = ''
            for k in range(len(sequence)):
                # check if sequence has been repeated
                cache += decimal_value[j:j+len(sequence)][k]
            # if sequence is repeated, check its length
            if sequence in cache:
                if len(sequence) > len(recurring_cycle):
                    recurring_cycle = sequence
                    biggest_number = i
                    #print i
                break
            # sequence was not repeated, append current value
            sequence += decimal_value[j]            
end = time()


print biggest_number
print 'Elapse',end-start
