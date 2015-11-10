'''
Euler Project #4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
palindrome = list()
for a in xrange(999,99,-1):
    for b in xrange(999,99,-1):
        product = str(a*b)
        if (product == product[::-1]):
            palindrome.append(int(product))
            
print max(palindrome)
