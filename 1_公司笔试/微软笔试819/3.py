from collections import defaultdict
def solution(A, B):
    # write your code in Python (Python 3.6)
    graph = defaultdict(list)
    for i, j in zip(A, B):
        graph[j].append(i)
        graph[i].append(j)
    print(graph)
    track = [0]
    visited = [0] * len(graph)
    fuel_count = []

    def dfs(index):
        if index not in graph:
            fuel_count.append(1)
            return

        for i in graph[index]:
            if visited: continue
            visited[i] = 1
            track.append(i)
            dfs(i)
            track.pop(-1)
            visited[i] = 0

    dfs(0)
    return fuel_count

A, B = [0,1,1], [1,2,3]
s = solution(A, B)
print(s)