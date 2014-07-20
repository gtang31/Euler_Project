# -*- coding: utf-8 -*-
"""
Euler Project 21
================================================================
Let d(n) be defined as the sum of proper divisors of n(numbers
less than n which divide evenly into n). If d(a) = b and
d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11,
20, 22, 44, 55 and 110; therefore d(220) = 284. The proper
divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt
from math import floor
from time import time

def isPrime(n):
    # even numbers cannot be prime
    if(n%2 == 0):
        return False
    else:
        prime = True
        for i in range(3,int(sqrt(n))+1,2):
            # check if n is divisible
            if (n%i == 0):
                prime = False
                break
    return prime

# find proper divisors for given number
def SumProperDivisors(num):
    proper_divisors = [1]
    for i in range(2,int(sqrt(num))+1):
        if(num%i == 0):
            proper_divisors.extend((i,num/i))
    return sum(proper_divisors)

# find amicable numbers
def isAmicable(num_dict):
    amicable_list = []
    for i in num_dict:
        temp = num_dict[i]
        if temp in num_dict and num_dict[temp] == i and temp != i:
            amicable_list.append(i)    
    return amicable_list

start = time()
num_dict = {}
for i in range(1,10**4):
    # can ignore if prime number
    if isPrime(i):
        pass
    else:
        num_dict[i] = SumProperDivisors(i)
        
print sum(isAmicable(num_dict))
end = time()

print 'Elapsed',end-start
