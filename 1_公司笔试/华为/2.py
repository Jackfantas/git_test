m, n = map(int, input().split(' '))
grid = []
for i in range(m):
    grid.append(input().split(' '))
print(grid)
count = 0
q = []
for i in range(m):
    for j in range(n):
        if grid[i][j] == '2':
            q.append([i,j])
visited = set()
while q:
    node = q.pop()
    row,col = node[0],node[1]
    visited.add((row,col))
    if grid[row][col] == '1': continue
    if grid[row][col]=='0':count +=1
    if grid[row][col] == '4':
        grid[row][col] = '0'
        count += 3
    if grid[row][col] == '6':
        count += 1
        grid[i][j] = '0'
        for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= i < m and 0 <= j < n:
                grid[i][j]='0'

    for i,j in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
        if 0<=i<m and 0<=j<n and (i,j) not in visited:
            if grid[i][j] != '1':
                q.append([i,j])
            if grid[i][j] == '3':
                print(count+1)
                exit()

print(count)
