"""
Euler Project 36
================================================================
The decimal number, 585 = 10010010012 (binary), is palindromic in
both bases.

Find the sum of all numbers, less than one million, which are
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may
not include leading zeros.)
"""
from time import time

def decimal_palindromes(n):
    # this function finds all the palindromes up to n-1
    palindromes = []
    for number in xrange(10**6):
        if str(number) == str(number)[::-1]:
            palindromes.append(number)
    return palindromes

def binary_palindromes(lis):
    # checks for all the binary palindromes in lis
    binary_palindromes = []
    for number in lis:
        if bin(number)[2:] == bin(number)[::-1][:-2]:
            # save the number whose binary value is palindromic
            binary_palindromes.append(number)
    return binary_palindromes

start = time()
print sum(binary_palindromes(decimal_palindromes(10**6)))
end = time()
print 'Elapsed', end - start
