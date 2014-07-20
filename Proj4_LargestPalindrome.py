'''
Euler Project 4
======================================================================
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit
numbers.
'''
def swap(string):
    temp = ''
    for character in range(len(string)):
        temp += string[len(string)-character-1]
    return temp

palindrome = []
for a in range(999,99,-1):
    for b in range(999,99,-1):
        product = str(a*b)
        if (product == swap(product)):
            palindrome.append(int(product))
            
print max(palindrome)

# altenative method, consider temp == temp[::-1]
