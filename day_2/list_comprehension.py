"""
{ x | x is a real number}
{x ^2 | x in [0,10]}
{x + 3 | x in negative inntegers }

[generator_function(x, y, z...) for x, y, z in iterator]
"""

numbers = [x / 2 for x in range(1, 11)]
print(numbers)

val = (x for x in range(1, 10))
print(type(val))

