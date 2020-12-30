"""
m: int
cost: list[int]

a_1 + a_2 = m

return index[a_1], index[a_2]
"""


# O(n ^2)
def get_flavour_index(m: int, cost: list) -> list:
    flavours = len(cost)
    for i in range(flavours):
        for j in range(i + 1, flavours):
            if cost[i] + cost[j] == m:
                return [i + 1, j + 1]


def get_flavour_index_fast(m: int, cost: list) -> list:
    elements = {}
    for index, number in enumerate(cost):
        required = m - number
        if required in elements:
            return [elements[required] + 1, index + 1]
        elements[number] = index

"""
[4 5 -3 3 2]
m = 1

4 {} -3?? no {4 --> 0}
5 {} -4?? no {4 --> 0, 5 --> 1}
-3 4?? yes 

1 3?? {} {elements --> index} {1 --> 0}
4 0?? {4 --> 1, 1 --> 0}
5 -1?? {5 --> 2, 4 --> 1, 1 --> 0}
3 1?? yes
"""

test_cases = int(input())

while test_cases > 0:
    m = int(input())
    _ = int(input())
    cost = list(map(int, input().split()))
    result = get_flavour_index_fast(m, cost)
    print(result[0], result[1])
    test_cases -= 1
