from collections import defaultdict


def count_re(points):
    res = 0
    # num_dict = defaultdict(set)
    num_dict = {}
    for point in points:
        x, y = point
        num_dict[x] = set()

    for point in points:
        x, y = point
        num_dict[x].add(y)
    keys = list(num_dict.keys())
    print(keys)
    for i in range(1, len(keys)):
        if len(num_dict[keys[i]]) < 2: continue
        for j in range(i):
            if len(num_dict[keys[j]]) < 2: continue
            intersect = num_dict[keys[i]] & num_dict[keys[j]]
            if len(intersect) < 2:
                continue
            else:
                res += 2 * len(intersect) - 2
    return res


# points = '[(1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 4)]'
# points = eval(points)
# num = count_re(points)
# print(num)
from collections import defaultdict

dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict1[2] ='two'

print(dict1[1])
print(dict2[1])
print(dict3[1])
print(dict4[1])
