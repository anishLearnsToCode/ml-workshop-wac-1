"""
N : int
0 : 0 ^ 2
1 : 1 ^2
2 : 1^ 2 + 2 ^ 2

N : 1 ^ 2 + 2 ^ 2 + ... + N ^ 2
"""

N = int(input())
result = 0
for i in range(1, N + 1):
    result += i ** 2

print(result)
