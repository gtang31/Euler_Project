"""
Euler Project 14
================================================================
The following iterative sequence is defined for the set of
positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the
following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing
at 1) contains 10 terms. Although it has not been proved yet
(Collatz Problem), it is thought that all starting numbers
finish at 1.

Which starting number, under one million, produces the longest
chain?

NOTE: Once the chain starts the terms are allowed to go above
one million.
"""
# this project makes use of Dynamic Programming

# calculate the Collatz Chain starting at given integer
def LongestCollatzChain(n,known_chains):
    chain = 0
    while n!= 1:
        chain += 1
        if n%2 == 0:
            n = n/2
            if n in known_chains:
                chain += known_chains[n]
                break
        else:
            n = 3*n + 1
            if n in known_chains:
                chain += known_chains[n]
                break
    return chain

from time import time
i = 1
chain = 0
start = time()
# use dictionary to track previous values and their chain length
known_chains = {}
while i < 10**6:
    if chain < LongestCollatzChain(i,known_chains):
        chain = LongestCollatzChain(i,known_chains)
        print i
    known_chains[i] = LongestCollatzChain(i,known_chains)
    i += 1    
end = time()
print end-start
