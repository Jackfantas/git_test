from collections import defaultdict
n = int(input())
nums = list(map(int, input().split()))
flags = input()
adj = defaultdict(list)
for i in range(n-1):
    father, child = flags[nums[i]-1], flags[i+1]
    adj[(nums[i]-1,father)].append((i+1,child))


res = []
for i in range(len(flags)):
    if adj[(i,flags[i])]==0:
        res.append(1)
        continue
    q = [(i,flags[i])]
    node_set = set()
    node_set.add(flags[i])
    while q:
        node = q.pop(0)
        for c in adj[node]:
            q.append(c)
            node_set.add(c[1])
    res.append(len(node_set))
# print(res)
res = [str(i) for i in res]
print(' '.join(res))
