import heapq
n,m,k = map(int, input().split(' '))
grid = []
while n:
    grid.append(list(input().strip()))
    n -= 1
print(grid)
def dfs(grid, i, j, c):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j]=='x' or grid[i][j]!=c:
        return 0
    grid[i][j] = 'x'
    return 1 + dfs(grid, i, j - 1, c) + dfs(grid, i, j + 1, c) + dfs(grid, i - 1, j,c) + dfs(grid, i + 1, j,c)

m, n = len(grid), len(grid[0])
max_count = 0
value_dict ={'r':1,'b':2,'g':3,'p':5}
q = []
for i in range(m):
    for j in range(n):
        if grid[i][j] != 'x':
            c = grid[i][j]
            count = dfs(grid, i, j, grid[i][j])
            value = count * value_dict[c]
            heapq.heappush(q, -value)
print(q)
res = 0
for i in range(k):
    v = heapq.heappop(q)
    res += abs(v)
print(res)