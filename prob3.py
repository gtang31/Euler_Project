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
from check_prime import is_prime
from math import sqrt
# find largest prime factor of number N

def largest_prime_factor(n):
	c = int(sqrt(n))
	if (c%2 == 0):
		c += 1
	for i in range(c, 1, -2):
		if (n%i == 0) and is_prime(i): return i

n = 600851475143
print largest_prime_factor(n)
