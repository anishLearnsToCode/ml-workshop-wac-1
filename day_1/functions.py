"""
Functions
def function_name(args... [optional], arg1, arg2, arg3 .... arg4=dv, arg5=dv2 ...):
    code
    code
"""


def hello():
    print('hello world')


def full_name(first_name: str, last_name: str, middle_name=None) -> None:
    if middle_name:
        result = first_name + ' ' + middle_name + ' ' + last_name
    else:
        result = first_name + ' ' + last_name
    print(result)


def extract_character_from_str(string: str, character: str) -> str:
    result = ''
    for c in string:
        if c == character:
            result += c
    return result


# first_name = input()
# last_name = input()
# full_name(extract_character_from_str(first_name, 'l'), last_name[0:5])
# full_name('ll', last_name[0:5])
# full_name('ll', 'world')

full_name('anish', 'sachdeva')
full_name(first_name='wolfgang', middle_name='amadeus', last_name='mozart')

print('hello', end='**')
