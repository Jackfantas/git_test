# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python (Python 3.6)
    if len(A) < 3: return -1
    res = []
    d = A[1] - A[0]
    left, right = 0, 1
    # pre, cur = A[0], A[1]
    while right < len(A):

        while right < len(A) and A[right] - A[right-1] == d:
            right += 1
        if right - left >= 3:
            res.append(right - left)
        if not right < len(A):
            break
        left = right
        right += 1
        # print(right, left)
        d = A[right] - A[left]

    def continue_combination(num):
        total_num = 0
        for i in range(3, num+1):
            total_num += (num - i) + 1
        return total_num

    count = 0
    for num in res:
        count += continue_combination(num)

    return count


A = [1,3,5,7,1,1,1,2,1]
res = solution(A)
print(res)