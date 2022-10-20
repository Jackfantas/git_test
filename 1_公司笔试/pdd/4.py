c = int(input())
N = int(input())
p, v, u = [], [], []
for _ in range(N):
    a, b, c = map(int, input().split())
    p.append(a)
    v.append(b)
    u.append(c)
print(p, v, u)