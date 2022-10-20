def removeElement(nums,val):
    slow,fast = 0,0
    while fast<len(nums):
        if nums[fast]!=val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow