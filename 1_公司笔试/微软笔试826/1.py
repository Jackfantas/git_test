# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python (Python 3.6)
    nums = list(str(abs(N)))
    res = []
    # >=0 delete the fisrt 5
    if N > 0:
        flag = 1
        for i in range(len(nums)):
            if nums[i] == '5' and flag == 1:
                flag = 0
            else:
                res.append(nums[i])
        return int(''.join(res))
    else:
        # <= delete the last 5
        flag = 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == '5' and flag == 1:
                flag = 0
            else:
                res.append(nums[i])
        res.reverse()
        return -int(''.join(res))

res = solution(1525345)
print(res)