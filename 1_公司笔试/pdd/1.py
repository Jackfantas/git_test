from collections import defaultdict, Counter

res = []
apple_count = int(input())
apple_li = list(map(int, input().split()))
k = int(input())
index_li = list(map(int, input().split()))
value_2_index = {j:i for i,j in enumerate(apple_li)}
apple_count_dict = dict(Counter(apple_li))


# def cal_count(apple_count_dict):
#     total = 0
#     for k, v in apple_count_dict.items():
#         if v>=2:
#             total += v*(v-1)//2
#     return total

total = 0
for k, v in apple_count_dict.items():
    if v>=2:
        total += v*(v-1)//2



for i in index_li:

    apple_count_dict[apple_li[i-1]] -= 1

    cur = apple_count_dict[apple_li[i-1]]
    if cur >= 1:
        pre = cur + 1
        sub = pre*(pre-1)//2 - cur*(cur-1)//2
        total -= sub
    print(total)



