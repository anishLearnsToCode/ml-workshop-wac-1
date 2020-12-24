"""
N!
0! = 1
1! = 1
3! = 1 * 2 * 3

N! = 1 * 2 * 3 * ... * N
"""

N = int(input())
result = 1

for i in range(1, N + 1):
    result *= i

print(result)
