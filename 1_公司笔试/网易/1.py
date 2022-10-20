n = int(input())
*nums, = map(int, input().split())

hm = dict()
for i in range(n):
    hm[nums[i]] = i
res = []
acc = 0
for i in range(n):
    # 每次遍历将对应位置变为对应的数字
    while nums[i] != i + 1:
        acc += 1
        idx2 = hm[nums[i] - 1]
        nums[i], nums[idx2] = nums[idx2], nums[i]
        # 更新每个数字所在的位置
        hm[nums[idx2]] = idx2
        hm[nums[i]] = i
        res.append([idx2, i])
print(acc)
for i in range(len(res)):
    print(res[i][0], res[i][1])