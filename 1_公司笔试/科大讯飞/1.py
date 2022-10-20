str1 = input()
m = int(input())
n = int(input())
grid = []
for i in range(0,len(str1), n):
    grid.append(list(str1[i:i + n]))
flows = input().split()

track = []
res = []
visited = [[0] * n for _ in range(m)]
# print(grid)

def dfs(grid, i, j, track):

    if len(track) < 10:
        res.append(list(track))
    if len(track) == 10:
        res.append(list(track))
        return
    if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] == 1:
        return
    for row, col in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if row < 0 or row >= m or col < 0 or col >= n: continue
        if visited[row][col]==1:continue
        track.append(grid[row][col])
        visited[row][col] = 1
        dfs(grid, row, col)
        track.pop(-1)
        visited[row][col] = 0

for i in range(m):
    for j in range(n):
        dfs(grid, i, j)

print(res)

ans = [flow for flow in flows if flow in res]
print(' '.join(ans))
