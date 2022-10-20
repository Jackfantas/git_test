str1 = input()
m = int(input())
n = int(input())
grid = []
for i in range(0,len(str1), n):
    grid.append(list(str1[i:i + n]))
flows = input().split()
print(flows)
# visited = [[0] * n for _ in range(m)]
# print(visited)
# print(grid)
directions = [[0,1],[0,-1],[1,0],[-1,0]]
def dfs(flow, flow_next_index, x, y):
    if flow_next_index==len(flow):
        return True
    for add_x,add_y in directions:
        next_x, next_y = x+add_x, y+add_y
        if 0<=next_x<m and 0<=next_y<n:
            if grid[next_x][next_y] == flow[flow_next_index] and visited[next_x][next_y]==0:
                visited[next_x][next_y] = 1
                flag = dfs(flow,flow_next_index+1, next_x, next_y)
                if flag:
                    return True
                else:
                    visited[next_x][next_y] = 0
    return False

def is_flow_valid(flow):
    global visited
    for i in range(m):
        for j in range(n):
            if grid[i][j]==flow[0]:
                visited[i][j] = 1
                flag = dfs(flow, 1, i, j)
                if flag:
                    return True
                visited[i][j] = 0
    return False

ans = []
for flow in flows:
    visited = [[0]*n for _ in range(m)]
    flag = is_flow_valid(flow)
    if flag:
        ans.append(flow)
print(' '.join(sorted(ans)))



