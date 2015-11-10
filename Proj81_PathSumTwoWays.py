"""
In the 5 by 5 matrix below, the minimal path sum from the top
left to the bottom right, by only moving to the right and down,
is indicated in bold red and is equal to 2427.


131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331

Find the minimal path sum, in matrix.txt (right click and 'Save
Link/Target As...'), a 31K text file containing a 80 by 80
matrix, from the top left to the bottom right by only moving
right and down.
"""
from numpy import loadtxt
from time import time

matrix = loadtxt('Proj81_matrix.txt', delimiter = ',')
#matrix = loadtxt('proj81.txt', comments = '#')
curr_row = 1
def ShortestPathSum(curr_row,matrix):
    for col in range(1,len(matrix)):
        matrix[curr_row,col] += \
         min(matrix[curr_row-1,col],matrix[curr_row,col-1])
        #print matrix[curr_row,col]
        #print matrix
    if curr_row == len(matrix)-1:
        # stop once we rached the NxN'th element
        return matrix[curr_row,col]
    else:
        # call recursion
        return ShortestPathSum(curr_row+1,matrix)

    
start = time()
print ShortestPathSum(curr_row,matrix)
end = time()
print 'Elapsed', end-start
