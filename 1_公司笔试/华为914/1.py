"""
5 5
0 1
3 3
1
2 2
"""

from collections import Counter

m, n = map(int, input().split(' '))
grid = [[0] * n for _ in range(m)]
start_x, start_y = map(int, input().split())
grid[start_x][start_y] = 's'
end_x, end_y = map(int, input().split())
grid[end_x][end_y] = 'e'
num_lake = int(input())
for _ in range(num_lake):
    lake_x, lake_y = map(int, input().split())
    grid[lake_x][lake_y] = 'x'


# print(grid)

def dfs(grid, i, j):
    if grid[i][j] == 'e':
        if not res:
            res.append(len(road))
        else:
            if len(road) > res[-1]: return
            while res and len(road) < res[-1]:
                res.pop(-1)
            res.append(len(road))
        return
    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 'x' or visited[x][y]: continue
        road.append((x, y))
        visited[x][y] = 1
        dfs(grid, x, y)
        visited[x][y] = 0
        road.pop(-1)

res = []
road = []
visited = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if grid[i][j] == 's':
            visited[i][j] = 1
            dfs(grid, i, j)

res = Counter(res)
print(res)
