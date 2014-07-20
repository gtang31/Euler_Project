"""
Euler Project 16
================================================================
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

a = str(2**1000)
a = list(a)
num = 0
for i in range(len(a)):
    num += int(a[i])
print num

