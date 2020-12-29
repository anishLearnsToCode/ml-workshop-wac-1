def var(x):
    return x ** 2

var = lambda x: x ** 2

print(type(var))

print(var(10))

print(list(map(lambda x, y: x + y, [1, 2, 3, 4])))

# func = lambda x: x + 10
# print(func(1))


# for x, y in [(1, 2), (3, 4)]:
#     print(func(x, y))

# for item in map(func, [(1, 2), (3, 4)]):
#     print(item)
