energy = 10
actions = [[1,1],[2,3],[3,5],[5,10],[7,9],[8,10]]
n = len(actions)

dp = [[0] * (n + 1) for _ in range(energy + 1)]
print(dp)
# 行代表体力值
for i in range(1, energy + 1):
    for j in range(1, n + 1):
        if i - actions[j - 1][0] < 0:
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - actions[j - 1][0]][j - 1] + actions[j - 1][1])

print(dp[-1][-1])