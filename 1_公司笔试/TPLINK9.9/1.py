T = int(input())
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

index = []
for i in range(n):
    for j in range(m):
        if grid[i][j]==-1:
            index.append([i, j])
# print(index)
prefix = [[0]*(m+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] + grid[i-1][j-1] - prefix[i-1][j-1]
# print(prefix)

def sumRegion(row1, col1, row2, col2):
    return prefix[row2 + 1][col2 + 1] - prefix[row2 + 1][col1] - prefix[row1][col2 + 1] + prefix[row1][col1]

def no_minus1(r1, c1, r2, c2):
    flag = True
    for i, j in index:
        if r1 <= i <= r2 and c1 <= j <= c2:
            flag = False
            break
    return flag

res = 0
for i_1 in range(n):
    for j_1 in range(m):
        for i_2 in range(i_1, n):
            for j_2 in range(j_1, m):
                # if i_1 > i_2 or j_1 > j_2:continue
                if i_2-i_1 == j_2-j_1 and no_minus1(i_1, j_1, i_2, j_2):
                    res = max(res, sumRegion(i_1, j_1, i_2, j_2))
                    # print((i_1, j_1, i_2, j_2), sumRegion(i_1, j_1, i_2, j_2))
print(res)

'''
1
4 4
3 0 5 6
0 9 -1 4
-1 8 1 1
4 -1 5 -1
'''