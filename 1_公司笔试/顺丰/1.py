from collections import defaultdict
n = int(input())
nums_li = list(str(n))
num_count = defaultdict(int)
if n < 55555:
    print(55555)
else:
    for i in range(len(nums_li)):
        num_count[nums_li[i]] += 1
    # 如果 5的个数大于5
    if num_count['5'] > 5:
        print(n+1)
    elif num_count['5'] == 5:
        if num_count['5']==len(nums_li):
            print(155555)
        else:
            flag = False
            for i in range(len(nums_li)-1, -1, -1):
                for j in range(i-1,-1,-1):
                    if nums_li[i]>nums_li[j]:
                        nums_li[i],nums_li[j] = nums_li[j], nums_li[i]
                        nums_li[i] = '0'
                        flag = True
                        break
                if flag:
                    break
            if flag:
                print(''.join(nums_li))
            else:
                nums_li[j] += str(int(nums_li[j])+1)
                print(''.join(nums_li))

    else:
        for i in range(len(nums_li) - 1, -1, -1):
            if int(nums_li[i]) < 5:
                nums_li[i] = '5'
                num_count['5'] += 1
                if num_count['5'] == 5:
                    print(''.join(nums_li))
                    break
        if i==0:
            nums_li = ['1']+nums_li
            for i in range(len(nums_li) - 1, -1, -1):
                if int(nums_li[i]) != 5:
                    nums_li[i] = '5'
                    num_count['5'] += 1
                    if num_count['5'] == 5:
                        print(''.join(nums_li))
                        break

