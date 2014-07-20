"""
EUler Project 99
======================================================================
Comparing two numbers written in index form like 211 and 37 is not
difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382**518061 > 519432**525806 would
be much more difficult, as both numbers contain over three
million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K
text file containing one thousand lines with a base/exponent pair on
each line, determine which line number has the greatest numerical
value.

NOTE: The first two lines in the file represent the numbers in the
example given above.
"""
from math import log
from time import time
start = time()
with open('proj99_baseexp.txt','r') as base_exp:
    number = 0
    counter = 1
    for line in base_exp:
        temp = line.split(',')
        if int(temp[1])*log(int(temp[0]),10) >= number:
            number = int(temp[1])*log(int(temp[0]),10)
            line_number = counter
        counter += 1
end = time()

print line_number
print 'Elapsed',end - start
