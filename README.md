# ugly_comprehensions
Some comprehensions that I met in my practice with their translations

The idea came when I tried to create matrix with given count of rows. Each row was receiving values/numbers, separated with a comma and a space ", ", in string, 
so after I read the input I had the idea to make the solution smaller as possible.
I am putting the final "solution" only, because the code isn't look good in the readme file.
All the explanations will be in every file.


print([item for sublist in [[int(x) for x in input().split(", ")] for _ in range(int(input()))] for item in sublist])

Have fun!
