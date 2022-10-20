n = int(input())
nums = [i for i in range(n*n)]
left = 0
for i in range(n):
    layer = [str(i) for i in nums[left:left+n]]
    # print(layer)
    left += n
    if i % 2 != 0:
        layer.reverse()
    print(' '.join(layer))