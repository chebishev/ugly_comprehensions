first_range, second_range = [int(x) for x in input().split()]
print(*(set(int(input()) for x in range(first_range)).intersection(set(int(input()) for x in range(second_range)))), sep="\n")

# this is two row solution with two comprehensions... obviuosly

# the task is to get numbers from two for loops and to merge only the unique ones.
# the solutions is to generate two sets and to intersect them

line_with_ranges = input().split()
first_range = line_with_ranges[0]
second_range = line_with_ranges[1]
first_set = set()
second_set = set()

for number in range(first_range):
	current_number = int(input())
	first_set.add(current_number)
	
for number in range(second_range):
	current_number = int(input())
	second_set.add(current_number)
	
final_set = first_set.intersection(second_set)
# or
print(*first_set.intersection(second_set))

# so the first comprehension is to get the ranges. It is necesary
first_range, second_range = [int(x) for x in input().split()]
# it can be done with list, map:
first_range, second_range = list(map(int, input().split()))
# it's the same funcionality
# after that. we can convert the for loops direct into the declaration of the sets:
first_set = set(int(input() for number in range(first_range)))
# repeating this for the second one:
second_set = set(int(input() for number in range(first_range)))
# and after the interseciton we have to print the result
# and for the second time the result with the comprehensions:

first_range, second_range = [int(x) for x in input().split()]
print(*(set(int(input()) for x in range(first_range)).intersection(set(int(input()) for x in range(second_range)))), sep="\n")

# test inputs:

# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5

# 2 2
# 1
# 3
# 1
# 5

