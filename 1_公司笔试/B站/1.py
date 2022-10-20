t = int(input())
for _ in range(t):
    nums = list(input())
    flag = True
    nums_list = []
    temp = []
    for c in nums:
        if '0'<=c<='9':
            temp.append(c)
        else:
            if temp:
                nums_list.append(temp)
            temp = []
    if(temp):
        nums_list.append(temp)
    print(nums_list)
    
    if not nums_list:
        print('aaano')
    else:
        for num in nums_list:
            sub = 1 if int(num[1])-int(num[0])>0 else -1
            flag=True
            for i in range(1, len(num)):
                if int(num[i])-int(num[i-1])!=sub:
                    flag = False
                    break

            if flag:
                print('yes')
                break
        if not flag: print('no')
