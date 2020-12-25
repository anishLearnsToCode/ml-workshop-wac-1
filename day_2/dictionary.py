"""
Dictionary / HashMap
anything --> anything
key value pair
key: unique

lists
integer --> something
"""

words = {
    'batman': 1001,
    'i': 90,
    'am': 45
}
print(type(words))
print(words)

# access elements dictionary
print(words['batman'])

# updating values in my dictionary
words['batman'] = 89
print(words)

# removing key from dictionary
del words['am']
print(words)

# if key is present in my dict
print('i' in words)

#default get method
print(words.get('hello', 'world'))
