"""
1
2 3
K00
00T
"""
N = int(input())
row, col = map(int, input().split())
def bfs(grid, i,j,step):
    # global step
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
        return
    if grid[i][j] == 'T':
        return step
    step += 1
    for x, y in [(i-2,j-1),(i-1,j-2),(i+1,j-2),(i+2,j-1),(i-2,j+1),(i-1,j+2),(i+1,j+2),(i+2,j+1)]:
        # step += 1
        res = dfs(grid,x,y,step)
        if res:
            return res


    return -1

for _ in range(N):
    grid = []
    for i in range(row):
        grid.append(list(input()))
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='K':
                # print(i, j)
                step = 0
                print(dfs(grid,i,j,0))
