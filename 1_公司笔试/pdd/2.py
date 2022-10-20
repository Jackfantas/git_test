from collections import deque
T = int(input())
res = []
count = 0
q_li = deque(['Alfred', 'Brian', 'Ken', 'Dennis'])
n = 10**9
while n>0:
    last = q_li.popleft()
    count += 1
    if count%3 != 0:
        q_li.append(last)
    q_li.append(last)
    n -= 1 # cola minus 1
    res.append(last)

for _ in range(T):
    n = int(input())
    print(res[n])