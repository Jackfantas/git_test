import sys
from copy import copy

input_str = list(input())
decrease = -1
for i in range(8):
    if input_str[i] < input_str[i+1]:
        continue
    else:
        decrease = i
if decrease == -1:
    print('null')
else:
    new_str = copy(input_str)
    swap_index = new_str.index(max(new_str[decrease+1:]))
    new_str[decrease],new_str[swap_index] = new_str[swap_index], new_str[decrease]
    new_str = new_str[:decrease+1] + sorted(new_str[decrease+1:], reverse=True)
    print(''.join(new_str))

increase = -1
for i in range(8):
    if input_str[i] > input_str[i+1]:
        continue
    else:
        increase = i

if increase==-1:
    print('null')
else:
    new_str = copy(input_str)
    swap_index = new_str.index(min(new_str[increase + 1:]))
    new_str[increase], new_str[swap_index] = new_str[swap_index], new_str[increase]
    new_str = new_str[:increase + 1] + sorted(new_str[increase + 1:])
    print(''.join(new_str))