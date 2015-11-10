"""
Using names.txt (right click and 'Save Link/Target As...'), a
46K text file containing over five-thousand first names, begin
by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
name in the list. So, COLIN would obtain a score of
938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def NameScore(curr_name,letter_score):
    nameScore = []
    for letter in curr_name.lower():
        nameScore.append(letter_score[letter])
    return sum(nameScore)

from string import ascii_lowercase
from time import time

# create dictionary containing score for each letter
start = time()
letter_score = {}
score = 1
for i in ascii_lowercase:
    letter_score[i] = score
    score += 1

name_list = open('Proj22_names.txt','r')
names = name_list.read()
name_list.close()
names = names.translate(None,'"')
names = sorted(names.split(','))

total_score = []
rank = 0
for i in names:
    rank += 1
    # calculate score for each name
    total_score.append(rank*NameScore(i,letter_score))
end = time()
print 'Elapse', end-start
print sum(total_score)
