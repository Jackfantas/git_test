"""
3
10 20 30
1 2 1
2 1 3
4
2 3 1 3
"""
from collections import defaultdict
import heapq

cake_count = int(input())
prices = list(map(int, input().strip().split()))
up_list = list(map(int, input().strip().split()))
down_list = list(map(int, input().strip().split()))
customer_count = int(input())
tastes = list(map(int, input().strip().split()))

hashmap = defaultdict(list)
index = 0
for t1,t2,p in zip(up_list, down_list, prices):
    temp1 = hashmap[t1]
    heapq.heappush(temp1, (p,index))
    hashmap[t1] = temp1

    temp2 = hashmap[t2]
    heapq.heappush(temp2, (p,index))
    hashmap[t2] = temp2
    index += 1

print(hashmap)
res = []
sold = set()
for t in tastes:
    if hashmap[t]:
        flag = 1
        while flag:
            li = hashmap[t]
            if not li:
                res.append("-1")
                flag = 0
                break
            val, ind = heapq.heappop(li)
            if ind not in sold:
                res.append(str(val))
                flag = 0
                sold.add(ind)
            hashmap[t] = li
    else:
        res.append("-1")
print(hashmap)
print(' '.join(res))