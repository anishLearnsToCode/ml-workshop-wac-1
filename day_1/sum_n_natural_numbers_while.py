"""
0: 0
1: 1
2: 1 + 2

N: 1 + 2 + 3 + ... + N
"""

N = int(input())
result = 0
i = 0

while i <= N:
    result += i
    i += 1

print(result)
