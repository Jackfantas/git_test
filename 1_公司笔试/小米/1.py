nums = [2, 6, 7, 8, 1]
n = 5
x = 3

left, right = 0, n - 1
count = 0
while x > 0:
    if x < nums[left] and x < nums[right]:
        x = -1
        break
    if nums[left] < nums[right]:
        if x >= nums[right]:
            x -= nums[right]
            right -= 1
        elif x >= nums[left]:
            x -= nums[left]
            left += 1
    else:
        if x >= nums[left]:
            x -= nums[left]
            left += 1
        elif x >= nums[right]:
            x -= nums[right]
            right -= 1
    count += 1

if x < 0:
    print(-1)
else:
    print(count)
