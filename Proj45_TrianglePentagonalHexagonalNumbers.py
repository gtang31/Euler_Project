# -*- coding: utf-8 -*-
"""
Euler Project 45
======================================================================
Triangle, pentagonal, and hexagonal numbers are generated by the
following formulae:

Triangle	 Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.
Find the next triangle number that is also pentagonal and hexagonal.
"""
def triangle_numbers(n):
    #define triangle numbers up to the n-th term
    return set([i*(i+1)*0.5 for i in xrange(1,n)])

def pentagonal_numbers(n):
    #define pentagonal numbers up to the n-th term
    return set([(i*(3*i-1))*0.5 for i in xrange(1,n)])

def hexagonal_numbers(n):
    #define hexagonal numbers up to the n-th term
    return set([(i*(2*i-1)) for i in xrange(1,n)])

n = 10**5
triangle_list = triangle_numbers(n)
pentagon_list = pentagonal_numbers(n)
hexagon_list = hexagonal_numbers(n)
# make use of set intersection
print (triangle_list & pentagon_list & hexagon_list)
