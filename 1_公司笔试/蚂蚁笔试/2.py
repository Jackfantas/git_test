from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

res = []
def back_track(start,track):
    if len(track) >= 1:
        res.append(len(track))

    for i in range(start, n):
        if not track or (i > 0 and nums[i]>nums[i-1] and nums[i-1] in track):
            track.append(nums[i])
            back_track(i+1, track)
            track.pop(-1)


back_track(0, [])
ans = ['0'] * n
for k, v in Counter(res).items():
    ans[k-1] = str(v)
print(' '.join(ans))

