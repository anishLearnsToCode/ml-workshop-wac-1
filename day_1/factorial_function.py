"""
N : 1 * 2 * 3 * .... * N
"""


def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


"""
nPr = n! / (n - r)!
"""


def permutation(n: int, r: int) -> int:
    return factorial(n) // factorial(n - r)
    # return 24 // factorial(n - r)
    # return 24 // factorial(2)
    # return 24 // 2
    # return 12


# nCr = nPr / r!
def combination(n: int, r: int) -> int:
    return permutation(n, r) // factorial(r)


print(combination(4, 0))
print(combination(4, 1))
print(combination(4, 2))
print(combination(4, 3))
print(combination(4, 4))
