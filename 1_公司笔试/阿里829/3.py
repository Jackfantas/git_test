from collections import defaultdict
n, m = map(int,input().split(' '))
num_1 = map(int, input().split())
num_2 = map(int, input().split())
num_dict = defaultdict(int)
for i in num_1:
    if i%337==0:
        div = i // 337
        if div<6:
            num_dict[div] += 1
        else:
            num_dict[6] += 1
print(num_dict)
total_count = m*num_dict[6]
for n in num_2:
    for k in range(1,6):
        if k * n % 6==0:
            total_count += num_dict[k]
print(total_count)