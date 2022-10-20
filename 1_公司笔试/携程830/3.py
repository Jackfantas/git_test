from collections import defaultdict
n = int(input())
color_str = list(input())
indegree = [0] * n
graph = defaultdict(list)
for i in range(n-1):
    u, v = map(int, input().split(' '))
    indegree[u-1] += 1
    indegree[v-1] += 1
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

q = [i for i in range(n) if indegree[i]==1]
count = 0
node_dict = {'r':0,'g':1,'b':2}
track = [0,0,0]
while q:
    node = q.pop(0)
    track[node_dict[node]]+=1
    for i in graph[node]:
        track[node_dict[i]] += 1
        if track[0] and track[1] and track[2]:
            count += 1
            track[0],track[1],track[2] = 0, 0, 0
        indegree[i] -= 1
        if indegree[i]==0:
            q.append(i)
print(count)