from collections import defaultdict

count, h_diff = map(int, input().split())
height_list = list(map(int, input().split()))
# print(h_diff, height_list)
left = 0
max_h_stack, min_h_stack = [], []
max_h_map_index, min_h_map_index = defaultdict(int), defaultdict(int)
ans_book_num = 0
ans_book_index = []
for i, height in enumerate(height_list):
    while max_h_stack:
        if max_h_stack[-1] <= height:
            max_h_stack.pop()
        else:
            break
    max_h_stack.append(height)
    max_h_map_index[height] = i

    while min_h_stack:
        if min_h_stack[-1] >= height:
            min_h_stack.pop()
        else:
            break
    min_h_stack.append(height)
    min_h_map_index[height] = i
    while max_h_stack[0] - min_h_stack[0] > h_diff:
        if max_h_map_index[max_h_stack[0]] < min_h_map_index[min_h_stack[0]]:
            left = max_h_map_index[max_h_stack[0]] + 1
            max_h_stack.remove(max_h_stack[0])
        else:
            min_h_stack.remove(min_h_stack[0])
            left = min_h_map_index[min_h_stack[0]]
    if max_h_stack[0] - min_h_stack[0] <= h_diff:
        cur_book_num = i - left + 1
        if cur_book_num < ans_book_num:
            continue
        if cur_book_num == ans_book_num:
            ans_book_index.append([left, i])
        if cur_book_num > ans_book_num:
            ans_book_num = cur_book_num
            ans_book_index = [[left, i]]
print(f'{ans_book_num} {len(ans_book_index)}')
for left, right in ans_book_index:
    print(f'{left + 1} {right + 1}')
