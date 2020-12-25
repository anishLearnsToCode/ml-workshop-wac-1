complex_dict = {
    'hello': 'world',
    100: 'world',
    'pi': 3.14,
    'e': 2.71828,
    range(1, 100, 15): [1, 2, 3, 4, 5, {
        'gold': {
            100: True
        }
    }]
}

print(len(complex_dict))
print(complex_dict[range(1, 100, 15)][-1]['gold'].get(100, [True, False]))
