# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python (Python 3.6)
    nums = list(str(abs(N)))
    index = [i for i in range(len(nums)) if nums[i]=='5']
    print(index)
    if N >= 0:
        max_n = -10000000
        for i in index:
            res = []
            for j in range(len(nums)):
                if j!=i:res.append(nums[j])
            max_n = max(max_n, int(''.join(res)))
        return max_n
    else:
        min_n = 10000000
        for i in index:
            res = []
            for j in range(len(nums)):
                if j!=i:res.append(nums[j])
            min_n = min(min_n, int(''.join(res)))
        return -min_n

res = solution(-154584)
print(res)