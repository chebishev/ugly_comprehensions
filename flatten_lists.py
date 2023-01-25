print(*[' '.join(element) for element in [string.split() for string in input().split("|")][::-1] if element])

# This problem was to get a string with numbers separated with one or many spaces and pipes.
# first we separate the string into list, splitting by pipes.
# after that we reverse the list and print all elements on one row
# We are getting the input as a string and we are reversing it by slicing
lists_of_numbers = input.split("|")[::-1]

for element in list_of_numbers.split():
  if element:
    print(" ".join(element), end="")
    
# it can be more detailed but i just wanted to show you how these 4 rows can be written on one
# do not forget that the repo is "ugly comprehensions" :)
# so, the more readable solution must be something like this:
numbers = [string.split() for string in input().split("|")]
print(*[' '.join(string) for string in numbers[::-1] if string])

# and the first row can be skipped with replacing "numbers[::-1" with [string.split() for string in input().split("|")]
# ofcourse we must change the variables in one of the comprehensions and the one row solution will look like this (again):
print(*[' '.join(element) for element in [string.split() for string in input().split("|")][::-1] if element])

# test inputs:

# 1 2 3 |4 5 6 |  7  88

# 7 | 4  5|1 0| 2 5 |3

# 1| 4 5 6 7  |  8 9
