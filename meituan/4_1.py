m, n = [int(i) for i in input().split(' ')]
A = input().strip().split(' ')
A = [int(i) for i in A]
B = input().strip().split(' ')
B = [int(i) for i in B]
total_step = 0
dp = [[0]*(n+1) for _ in range(m + 1)]
for i in range(1, m+1):
    dp[i][0] = abs(A[i-1])
for i in range(1, n+1):
    dp[0][i] = abs(B[i-1])
for i in range(1, m+1):
    for j in range(1, n+1):
        if A[i-1]==B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1]+dp[i-1][j], abs(A[i-1]-B[j-1]))
print(dp[-1][-1])