# Sean invented a game involving a matrix where each cell of the matrix contains an integer. He
# can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum
# of the elements in the submatrix located in the upper-left quadrant of the matrix.
# Given the initial configurations for matrices, help Sean reverse the rows and columns of each matrix in the
# best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.
# Example
# 1 2
# 3 4
# It is and we want to maximize the top left quadrant, a matrix. Reverse row :
# 1 2
# 4 3
# And now reverse column :

# 4 2
# 1 3
# The maximal sum is .
# Function Description
# Complete the flippingMatrix function in the editor below.
# flippingMatrix has the following parameters:
# - int matrix[2n][2n]: a 2-dimensional array of integers
# Returns
# - int: the maximum sum possible.
# Input Format
# The first line contains an integer , the number of queries.
# The next sets of lines are in the following format:
# The first line of each query contains an integer, .
# Each of the next lines contains space-separated integers in row of the
# matrix.
# Constraints
# , where .


#  CODE 

def flippingMatrix(matrix):
 sum = 0
 n = len(matrix)
 for i in range(n // 2 ):
 for j in range(n // 2):
 sum += max(matrix[i][j],
 max(matrix[i][n-1-j],
 max(matrix[n-1-i][j], matrix[n-1-i][n-1-j])))
 return sum
