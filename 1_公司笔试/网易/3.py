import sys
import heapq

n, k = [int(i) for i in input().split(' ')]
line = sys.stdin.readline().strip()
# 把每一行的数字分隔后转化成int列表
nums = list(map(int, line.split()))
# nums.sort()
track = []
res = []
used = [0] * len(nums)

# 回溯法选k个数
def back_track():
    if len(track) == k:
        track_sum = 2 ** 10 - 1
        for i in track:
            track_sum &= i
        heapq.heappush(res, -track_sum)
#         res.append([track_sum, list(track)])
        return
    for i in range(len(nums)):
        if used[i]: continue
        track.append(nums[i])
        used[i] = 1
        back_track()
        track.pop(-1)
        used[i] = 0

back_track()
print(-res[0])

