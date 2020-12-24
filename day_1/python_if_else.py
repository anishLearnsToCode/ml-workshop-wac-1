number = int(input())

if number % 2 == 1 or 6 <= number <= 20:
    print('Weird')
elif 2 <= number <= 5 or number > 20:
    print('Not Weird')
