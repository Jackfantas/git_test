n = int(input())
dp = [0] * max(4,n+1)
dp[1], dp[2], dp[3] = 1, 3, 5
if n < 4:
    print(dp[n])
else:
    for i in range(4,n+1):
        if i%2 == 0:
            dp[i] = i + dp[i//2] + dp[i//2-1]
        else:
            dp[i] = i + dp[(i-1)//2]*2
    print(str(int(dp[n])))