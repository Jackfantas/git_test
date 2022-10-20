q = int(input())
while q:
    nums_li = list(input())
    left, right = 0, len(nums_li)
    print(nums_li)
    flag = False
    if int(nums_li[-1])%2==0:
        print(''.join(nums_li))
        flag = True
    else:
        for i in range(len(nums_li)-1):
            if int(nums_li[i])%2==0:
                nums_li[i], nums_li[-1] = nums_li[-1], nums_li[i]
                print(''.join(nums_li))
                flag = True
                break
    if not flag:
        print(-1)
    q -= 1