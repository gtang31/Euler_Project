 #-*- coding: utf-8 -*-
"""
Euler Project 11
=====================================================================
What is the greatest product of four adjacent numbers in the same
direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""
import numpy
import time
from operator import mul

# load the .txt file containing the grid
grid = numpy.loadtxt("proj11_grid.txt")
print grid
product = 0

def check_col(grid,product):
    for col in range(20):
        for row in range(17):
            if(reduce(mul,grid[row:row+4,col]) >= product):
                product = reduce(mul,grid[row:row+4,col])
    return product

def check_row(grid,product):
    for row in range(20):
        for col in range(17):
            if(reduce(mul,grid[row,col:col+4]) >= product):
                product = reduce(mul,grid[row,col:col+4])
    return product

def check_diag_forward(grid,product):
    for row in range(17):
        for col in range(17):
            # create a diagonal vector like a forward-slash
            diag = [grid[row,col]]
            for i in range(1,4):
                diag.append(grid[row+i,col+i])
            if(reduce(mul,diag) >= product):
                product = reduce(mul,diag)
    return product

def check_diag_backward(grid,product):
    for row in range(17):
        for col in range(19,2,-1):
            # create a diagonal vector like a backward-slash
            diag = [grid[row,col]]
            for i in range(1,4):
                diag.append(grid[row+i,col-i])
            if(reduce(mul,diag) >= product):
                product = reduce(mul,diag)
    return product

start = time.time()
product = check_diag_backward(grid,product)
product = check_col(grid,product)
product = check_row(grid,product)
product = check_diag_forward(grid,product)
end = time.time()
print product
print end-start
