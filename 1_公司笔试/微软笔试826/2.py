# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict
def solution(A):
    # write your code in Python (Python 3.6)
    res = 0
    total_sum = 0
    num_dict = defaultdict(int)
    num_dict[0] = 1
    for i in A:
        total_sum += i
        res += num_dict[total_sum]
        num_dict[total_sum] += 1
        if num_dict[total_sum] >= 10 ** 5:
            return -1
    return res


A = [2, -2, 0, 0]
res = solution(A)
print(res)