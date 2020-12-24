# 1 1 2 3 5 8 13 21 ....
# f(n) = f(n - 1) + f(n - 2)
# f(0) = f(1) = 1
def fibonacci(n: int):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
