"""
Euler Project 7
======================================================================
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13. What is the 10,001st prime number?
"""
import math
from check_prime import is_prime

"""
Use Sieve of Eratosthenes
n = 29
print n
print isPrime(n)
"""
def nth_prime(n):
	nth_prime = 0
	num = 1
	while nth_prime != n:
		if is_prime(num):
			print num
			nth_prime += 1
		num += 1
	else:
		return num - 1
print nth_prime(10001)
