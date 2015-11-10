"""
Euler Project 10
======================================================================
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from math import sqrt
from check_prime import is_prime

# Use Seive of Eratosthenes to find all primes below 2M
def sum_of_prime(n):
	not_primes = set()
	for i in xrange(2, int(sqrt(n)) - 1):
		if i in not_primes: continue
		p = 2
		while p*i < n:
			not_primes.add(p*i)
			p += 1
	primes = list()
	for i in xrange(2, n):
		if i in not_primes: continue
		primes.append(i)
	return sum(primes)

print sum_of_prime(2000000)
