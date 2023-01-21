# Primary Diagonal
# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right). 
# On the first line, you will receive an integer N – the size of a square matrix. 
# The next N lines holds the values for each column - N numbers, separated by a single space. 

matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
print(sum(matrix[row][row] for row in range(len(matrix))))
# or
rows = int(input())
print(sum([[int(x) for x in input().split()] for _ in range(int(input()))][row][row] for row in range(len(rows))))

# The origin:
# this is already used in the previous file, but still this is a way to read a matrix with a number, 
# taken from the input as a range
matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
# of course you can't use this number again, so the number of the rows are the length of the matrix
# and the goal here is to get the primary diagonal sum. So the normal way to do this must be something like that:
diagonal_sum = 0
for row in range(len(matrix)):
	diagonal_sum += matrix[row][row]

print(diagonal_sum)

# the other way to shrink the code above is with this comprehension:
diagonal_sum = sum(matrix[row][row] for row in range(len(matrix)))
print(diagonal_sum)

# after that you can skip the creating of the variable:
print(sum(matrix[row][row] for row in range(len(matrix))))

# and at the final we can substitute "matrix" with this comprehension:
[[int(x) for x in input().split()] for _ in range(int(input()))]
# but it is used twice, so at this point I can't do this to you 
# and I am leaving it as a two rows solution
# We can start with variable for the matrix size:
rows = int(input())
# and the second row must be:
print(sum(matrix[row][row] for row in range(len(matrix))))
# but we are swaping the matrix with the other comprehension:
[[int(x) for x in input().split()] for _ in range(int(input()))]
# and for the range we are putting the "rows" again:
print(sum([[int(x) for x in input().split()] for _ in range(int(input()))][row][row] for row in range(len(rows))))





# test inputs:

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# 3
# 1 2 3
# 4 5 6
# 7 8 9
