'''
常用的场景：寻找一个数、寻找左侧边界、寻找右侧边界
①寻找一个数的二分搜索框架：
def binarySearch(nums,target):
    left = 0
    right = ...
    while(...):
        mid = left + (right-left)/2 #可以防止left+right溢出的情况
        if nums[mid]==target:
            ...
        elif nums[mid]<target:
            left = ...
        elif nums[mid]>target:
            right = ...
    return ...

②寻找左侧边界
def leftbound(nums,target):
    n = len(nums)
    if n==0:return -1
    left = 0
    right = n-1
    while left<=right: #结束的条件是left=right+1
        mid = left + （right-left）//2
        if nums[mid]==target:
            right = mid-1
        elif nums[mid]<target:
            left = mid + 1
        elif nums[mid]>target:
            right = mid-1 #注意
    # 检查出界情况
    if left>=nums.length or nums[left]!=target:
        return -1
    return left

③ 寻找右侧边界
def rightbound(nums,target):
    n = len(nums)
    if n==0:return -1
    left = 0
    right = n-1
    while left<=right: #结束的条件是left=right+1
        mid = left + （right-left）//2
        if nums[mid]==target:
            left = mid + 1
        elif nums[mid]<target:
            left = mid + 1
        elif nums[mid]>target:
            right = mid - 1 #注意
    # 检查出界情况
    if right<0 or nums[right]!=target:
        return -1
    return left
'''

# 寻找一个数