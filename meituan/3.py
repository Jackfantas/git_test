import heapq
# print(98/100)
n, m = input().split(' ')
n, m = int(n), int(m)
p_list = input().strip().split(' ')
# print(p_list)
p_list = [int(i) for i in p_list]
score_list = input().strip().split(' ')
score_list = [int(i) for i in score_list]

total_score = 0
q = []
for score, p in zip(score_list, p_list):
    heapq.heappush(q, (-score, p))
for i in range(n):
    item = heapq.heappop(q)
    score, p = -item[0], item[1]
    if i < m:
        total_score += score
    else:
        total_score += score * p / 100
print('%.2f'%total_score)