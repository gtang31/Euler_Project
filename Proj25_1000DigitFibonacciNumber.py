"""
Euler Project 25
================================================================
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000
digits?
"""
from math import log10
from time import time

Fib_Sequence = [1,2]
start = time()
# count the number of digits in most recent Fibonacci term
while int(log10(Fib_Sequence[-1]))+1 <= 999:
    # create Fibonacci sequence
    Fib_Sequence.append(Fib_Sequence[-1] + Fib_Sequence[-2])
end = time()
print end-start
# print Fib_Sequence
print len(Fib_Sequence)+1
