# 爱吃香蕉的珂珂

def minEatingSpeed(piles, h):
    # 由题目可知，吃完所有香蕉的最少小时数为堆数,堆数最大值为10**9
    left = 0
    right = 1000000000

    def f(piles, x):
        # 计算当吃香蕉速度为x时，吃完所有香蕉所花的时间
        hour = 0
        for i in piles:
            hour += i // x
            if i % x > 0:
                hour += 1
        return hour
    while left <= right:
        mid = left + (right - left) // 2
        pos = f(piles, mid)
        print(mid)
        if pos == h:
            right = mid - 1
        elif pos > h:
            left = mid + 1
        elif pos < h:
            right = mid - 1
    return left

piles = [3,6,7,11]
k = 8
res = minEatingSpeed(piles,k)
print(res)
