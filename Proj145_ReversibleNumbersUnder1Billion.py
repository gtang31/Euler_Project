"""
Euler Project 145
======================================================================
Some positive integers n have the property that the sum [ n + reverse
(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63
= 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36
, 63, 409, and 904 are reversible. Leading zeroes are not allowed in
either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""
from time import time

counter = []
start = time()
for number in xrange(1,10**8,2):
    flag = False
    if str(number)[-1] == '0':
        continue
    result = int(str(number)[::-1]) + number
    while result:
        # check each individual digit if it is even
        # avoid using int to str conversion
        curr_digit = result % 10
        if curr_digit % 2 == 0:
            flag = True
            break
        result /= 10
    if flag:
        continue
    counter.append(number)
    counter.append(int(str(number)[::-1]))
end = time()

print len(counter)
print 'Elapsed', end - start
