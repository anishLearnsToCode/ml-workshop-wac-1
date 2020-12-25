passage = input()

words = {}

for word in passage.split():
    words[word] = words.get(word, 0) + 1

print(words)
