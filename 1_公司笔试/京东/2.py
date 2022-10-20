from collections import defaultdict
n = int(input())
nums = list(map(int, input().split(' ')))
# 奇数的dict
odd_dict = defaultdict(int)
# 偶数的dict
even_dict = defaultdict(int)
for i, c in enumerate(nums):
    if i%2 == 0:
        even_dict[c] += 1
    else:
        odd_dict[c] += 1
odd_sort = sorted(odd_dict.items(), key=lambda x:x[1], reverse=True)
even_sort = sorted(even_dict.items(), key=lambda x:x[1], reverse=True)
step = 0
l1, l2 = odd_sort[0], even_sort[0]
print(odd_sort, even_sort)
if l1[0] == l2[0]:
    if l1[0] >= l2[0]:
        l2 = even_sort[1]
    else:
        l1 = odd_sort[1]
print(l1, l2)
print(n-l1[1]-l2[1])