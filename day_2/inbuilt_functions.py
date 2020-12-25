def abs(x: int) -> int:
    return x if x > 0 else -x

print(abs(-10))


ascii = [ord(character) for character in 'hello']
print(ascii)

print(min(ascii))
print(max(ascii))
print(sum(ascii))

n = int(input())
print(sum(x for x in range(1, n + 1)))
