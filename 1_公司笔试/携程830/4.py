import math
import heapq

n = int(input())
nums = [int(i) for i in input().split(' ')]

sub_li = [(-abs(nums[i] - nums[i - 1]), i) for i in range(1, n-1)]
heapq.heapify(sub_li)
value, index = heapq.heappop(sub_li)
if value==0:
    print(0)
elif nums[index - 1] == nums[index + 1]:
    heapq.heappop(sub_li)
else:
    res, _ = heapq.heappop(sub_li)
    print(-res)

# import math
# import heapq
# n = int(input())
# nums = [int(i) for i in input().split(' ')]
#
# sub_li = [(-abs(nums[i]-nums[i-1]),i) for i in range(1,n)]
# heapq.heapify(sub_li)
# value, index = heapq.heappop(sub_li)
# if nums[index-1] == nums[index+1]:
#     heapq.heappop(sub_li)
# value,_ = heapq.heappop(sub_li)
# print(-value)