from typing import List


class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        left1 = 0
        right1 = len(nums) - 1
        res = []
        # 寻找左右边界
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        while left1 <=right1:
            mid1 = left1 + (right1 - left1) // 2
            if nums[mid1] == target:
                left1 = mid1 + 1
            elif nums[mid1] > target:
                right1 = mid1 - 1
            elif nums[mid1] < target:
                left1 = mid1 + 1


        if left >= len(nums) or nums[left] != target:
            res.append(-1)
        else:
            res.append(left)
        if right1 < 0 or nums[right1] != target:
            res.append(-1)
        else:
            res.append(right1)
        return res

nums = [1,3]
target = 1
s = Solution()
res = s.searchRange(nums, target)
print(res)