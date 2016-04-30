"""
Euler Project 9
======================================================================
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which, a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exist exactly one Pythagorean triplet for which a+b+c=1000.
Find the product abc.
    .
    |\
    | \
    |  \
    |   \
    |    \  c
    |     \
 b  |      \
    |       \
    |        \
    |_        \
    |_|________\
          a          
30-60-90 triangle, because a < b < c
"""

"""
# Fibonacci's Method
import math
counter = 0
oddNum = range(1,1000,2)
for i in oddNum:
    # check if current number is a perfect square
    if ((math.sqrt(i)).is_integer()):
        a = math.sqrt(i)
        b = math.sqrt(sum(oddNum[0:counter]))
        c = math.sqrt(sum(oddNum[0:counter+1]))
    if(a + b + c == 1000):
        print a*b*c
        break
    counter += 1
"""
import time
# Finding all pythagorean triplets using any two positive integers
# where N > M
start = time.time()
for N in range(2,21):
    for M in range(0,N-1):
        a = N**2 - M**2
        b = 2*N*M
        c = N**2 + M**2
        if(a+b+c == 1000):
            #print a,b,c
            print a*b*c
            break
end = time.time()
print end-start
