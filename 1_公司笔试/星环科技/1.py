from collections import defaultdict
m,n = map(int, input().split(' '))
dependency = defaultdict(list) # 任务依赖关系
in_li = defaultdict(int) # 节点入度
task = set()
for i in range(m):
    a, b = input().split('->')
    task.add(a)
    task.add(b)
    dependency[b].append(a)
    in_li[a] += 1
for i in task:
    if i not in in_li:
        in_li[i] = 0
print(in_li, dependency)
# 找到入度为0的节点
q = [t for t in task if in_li[t]==0]
count=0
while q:
    count += 1
    node = q.pop(0)
    for item in dependency[node]:
        in_li[item] -= 1
        if in_li[item]==0:
            q.append(item)
res = 'YES' if count==n else 'NO'
print(res)