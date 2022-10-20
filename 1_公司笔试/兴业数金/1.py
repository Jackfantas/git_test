nums = input().split(',')
nums = [int(i) for i in nums]
add = 0
if nums[-1] != 9:
    nums[-1] += 1
    res = [str(i) for i in nums]
    print(','.join(res) + ',')
else:
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
            if nums[i] + 1 >= 10:
                add = 1
                nums[i] = nums[i] + 1 - 10
            else:
                add = 0
                nums[i] = nums[i] + 1
                res = [str(i) for i in nums]
                print(','.join(res) + ',')
                break
        else:
            if add > 0:
                if nums[i] + add >= 10:
                    add = 1
                    nums[i] = nums[i] + add - 10
                else:
                    nums[i] = nums[i] + add
                    add = 0
                    res = [str(i) for i in nums]
                    print(','.join(res) + ',')
                    break
            else:
                break
    if add > 0:
        res = [str(i) for i in nums]
        # print(','.join(res))
        res = str(add) + ',' + ','.join(res) + ','
        print(res)