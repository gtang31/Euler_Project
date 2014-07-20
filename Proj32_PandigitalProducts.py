"""
We shall say that an n-digit number is pandigital if it makes use
of all the digits 1 to n exactly once; for example, the 5-digit
number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9
pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be
sure to only include it once in your sum.
"""
from itertools import permutations
from math import sqrt
pandigital_candidates = list(permutations([1,2,3,4,5,6,7,8,9],9))
unusual_numbers = set()
for multiplicand in xrange(1,99):
    for multiplier in xrange(1,999):
        possible_pandigital = int(str(multiplicand) + str(multiplier) +\
                              str(multiplicand * multiplier)) 
        if possible_pandigital in pandigital_candidates:
            unusual_numbers.add(possible_pandigital)
            
print sum(unusual_numbers)   
