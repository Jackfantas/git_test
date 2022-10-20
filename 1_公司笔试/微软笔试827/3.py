import heapq
def solution(A, B):
    q = []
    for n1, n2 in zip(A,B):
        heapq.heappush(q, max(n1,n2))
    pre = -1
    for i in range(len(q)):
        num = heapq.heappop(q)
        if num == pre:continue
        pre = num
        if num != i+1:
            return i+1
    return pre + 1

A = [1,2,3]
B = [1,3,3]
# A = [3,2,1,6,5]
# B = [4,2,1,3,3]
res = solution(A,B)
print(res)