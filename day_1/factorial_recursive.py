"""
N! = N * (N - 1) * (N - 2) * (N - 3) * .... 3 * 2  * 1
    = N * (N - 1)!
"""
def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)


print(factorial(5))
