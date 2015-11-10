'''
determine whether a number is a prime
implement primality test
'''
from math import sqrt
def is_prime(n):
	if n <= 1: return False		# 1 is not a prime
	elif n <= 3: return True	# 2, 3 are primes 
	elif (n%2 == 0) or (n%3 == 0): return False
	else:
		i = 5
		while i <= sqrt(n):
			if (n%i == 0) or (n%(i + 2) == 0): return False
			i += 6
		return True
print is_prime(25)
