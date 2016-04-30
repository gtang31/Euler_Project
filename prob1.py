'''
Euler Project 1
=================================================================================================================================
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
total = 0 #initialize total = 0
for value in xrange(1000):
    if (value%3 == 0) or (value%5 == 0):
        total += value
print total
