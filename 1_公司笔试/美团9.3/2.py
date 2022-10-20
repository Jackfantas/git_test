import heapq
n = int(input())
nums = list(map(int, input().split()))
# q= heapq.heapify(nums)

def mex(nums):
    for i in range(10**9):
        if i not in nums:
            return i
res = []
for i in range(n):
    res.append(mex(nums[:i]+nums[i+1:]))
print(res)