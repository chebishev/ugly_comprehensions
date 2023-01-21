# Flattening Matrix
# Write a program that receives a matrix and prints the flattened version of it (a list with all the values). 
# For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the number of a matrix's rows. 
# On the next rows, you will get the elements for each column separated with a comma and a space ", ".

rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([])
    for number in input().split(", "):
        matrix[row].append(int(number))

output_matrix = []
for row in matrix:
    for number in row:
        output_matrix.append(number)

print(output_matrix)

# So you can read the matrix in one row without declaring the rows variable:
matrix = [int(x) for x in input().split(", ")] for _ in range(int(input()))]
# Adding the row above in the print statement gave me the idea for this repo
# without this row the final solution would be more readable:
print([item for sublist in matrix for _ in range(int(input()))] for item in sublist])

# the flattening works on this principle:
print([item for sublist in matrix for item in sublist])
# and it isn't quite readable in this varian too
# so this is the solution that makes sense:
flatten_list = []
for sublist in matrix:
    for item in sublist:
        flatten_list.append(item)

# another solution with more readable comprehensions:
rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

print([item for sublist in matrix for item in sublist])

# One row solution:
print([item for sublist in [[int(x) for x in input().split(", ")] for _ in range(int(input()))] for item in sublist])



# test inputs:

# 2
# 1, 2, 3
# 4, 5, 6

# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
