'''
Euler Project 5
================================================================
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder. What is the smallest
positive number that is evenly divisible by all of the numbers
from 1 to 20?
'''
# this is an interesting problem and takes some time to think about,
# we know that any number that can be divided by 11-20 can also be
# divided by 1-10. So we should only check those values. We increment by
# 20 because thats the biggest number, also the smallest possible value
# divisible by all numbers from 1-20 should also be a multiple of 20

import time

start_time = time.time()
number = 20
while True:
    if number%20 == 0 and number%19 == 0 and number%18 == 0 and number%17 == 0 and number%16 == 0 and number%15 == 0 and number%14 == 0 and number%13 == 0 and number%12 == 0 and number%11 == 0:
        break;
    else:
        number += 20
end_time = time.time()
print 'Elapsed time',end_time-start_time
#print number
