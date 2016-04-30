"""
Euler Project 42
=================================================================
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to
its alphabetical position and adding these values we form a word
value. For example, the word value for SKY is 19 + 11 + 25 = 55
= t10. If the word value is a triangle number then we shall call
the word a triangle word.

Using words.txt, a
16K text file containing nearly two-thousand common English words,
how many are triangle words?
"""
f = open('proj42_words.txt','r')
words_list = f.read()
f.close()
words_list = sorted(words_list.translate(None,'"').split(','))

def triangle_numbers(n):
    #define triangle numbers up to the n-th term
    return [(i*(i+1))*0.5 for i in xrange(1,n)]

triangle_list = triangle_numbers(10*3)

# create word value dictionary
from string import ascii_lowercase
word_dict = {}
score = 1
for letters in ascii_lowercase:
    word_dict[letters.upper()] = score
    score += 1

counter = []
# calculate each words' value and compare it against our triangle list
for word in words_list:
    word_value = 0
    for letter in word:
        word_value += word_dict[letter]
    if word_value in triangle_list:
        counter.append(word)
        
print len(counter)
