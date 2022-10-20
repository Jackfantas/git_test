n = int(input().strip())
x1, y1 = input().strip().split(' ')
x2, y2 = input().strip().split(' ')
x3, y3 = input().strip().split(' ')
d1, d2, d3 = input().strip().split(' ')

x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)
x3, y3 = int(x3), int(y3)
d1, d2, d3 = int(d1), int(d2), int(d3)

for x in range(1, n+1):
    if abs(x-x1) > d1: continue
    if abs(x-x2) > d2: continue
    if abs(x-x3) > d3: continue
    for y in range(1, n+1):
        if abs(y-y1) > d1:continue
        if abs(y-y2) > d2:continue
        if abs(y-y3) > d3:continue
        if abs(x-x1) + abs(y-y1)==d1 and abs(x-x2) + abs(y-y2)==d2 and abs(x-x3) + abs(y-y3)==d3:
            print(x, y)
            exit()
