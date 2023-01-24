print("\n".join(set(input() for name in range(int(input())))))

# No black magic here. Just too many parenthesis
# the original task is to get a number of names which we will take in the next few lines
# and to get only the unique one, obviuosly by using a set

number_of_names = int(input())
unique_names_set = set()

for name in range(number_of_names):
  current_name = input()
  unique_names_set.add(current_name)
  
print(*unique_names_set, sep="\n")
# or
print("\n".join(unique_names_set))

# the one row solution came after I saw that the variables are one time used, so we can skip them.
# also the for loop is pretty standard one. It can be done in one row with something like this:
unique_names_set = set(input() for name in range(number_of_names))
# after that we just add the print statement, instead of the set variable,
# the separator of the printed items, and we are getting rid of the first variable

print("\n".join(set(input() for name in range(int(input())))))

# Have fun!
