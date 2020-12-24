N = int(input())
# N = 0 --> 0
# N = 3 --> 1 + 2 + 3 = 6

result = 0
for i in range(1, N + 1):
    result += i

print(result)
