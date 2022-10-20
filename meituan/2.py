n = int(input())
x1, y1 = input().strip().split(' ')
x2, y2 = input().strip().split(' ')
x3, y3 = input().strip().split(' ')
d1, d2, d3 = input().strip().split(' ')
res = []
def find_tartget(t_x,t_y,t_d):
    res = []
    t_x,t_y,t_d = int(t_x), int(t_y), int(t_d)
    for x in range(1, n+1):
        if abs(x-t_x) > t_d: continue
        for y in range(1, n+1):
            if abs(y-t_y) > t_d:continue
            if abs(x-t_x) + abs(y-t_y)==t_d:
                res.append((x,y))
    return res

res1 = find_tartget(x1,y1,d1)
res2 = find_tartget(x2,y2,d2)
res3 = find_tartget(x3,y3,d3)
for item in res1:
    if item in res2 and item in res3:
        print(item[0], item[1])
        break