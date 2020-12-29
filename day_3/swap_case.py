string = input()

"""
Hello 2
hELLO 2
"""

result = ''.join([character.lower() if character.isupper() else character.upper() for character in string])
print(result)
