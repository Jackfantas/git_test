# 移除数组中的重复元素
def removeDuplicates(nums):
    if len(nums)==0:
        return 0
    slow,fast = 0,0
    while fast<len(nums):
        if nums[fast]!=nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1

    return slow+1