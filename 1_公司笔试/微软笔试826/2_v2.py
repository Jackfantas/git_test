def solution(A):
    # write your code in Python (Python 3.6)
    # A.sort()
    res = []
    pre_sum = [0]
    total_sum = 0
    num_dict = {0: 1}
    for i in A:
        total_sum += i
        num_dict[total_sum] = num_dict.get(total_sum, 0) + 1
        if num_dict[total_sum] >= 10 ** 5:
            return -1
        pre_sum.append(total_sum)

    count = 0
    for i in range(len(pre_sum)):
        for j in range(i + 1, len(pre_sum)):
            if pre_sum[j] - pre_sum[i] == 0:
                count += 1
                if count > 10 ** 9:
                    return -1
    return count


A = [2, -2, 0,3,4,-7]
res = solution(A)
print(res)
