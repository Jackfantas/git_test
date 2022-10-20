def continue_combination(num):
    total_num = 0
    for i in range(3, num+1):
        total_num += (num - i) + 1
    return total_num

res = continue_combination(4)
print(res)