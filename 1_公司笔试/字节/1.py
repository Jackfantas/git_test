n = int(input())
count = 0
layer = []
for i in range(n):
    li = list(map(int, input().split()))
    m, stones = li[0], li[1:]
    if i == 0:
        count += m
        last = -100
        for s in stones:
            if s-last<100 and s>last:
                layer.append([last, s])
            layer.append([s, s + 100])
            last = s + 100
        # print(layer)
    else:
        temp = []
        for i in stones:
            for left, right in layer:
                if right-left==100 and left<i + 50<right:
                    count += 1
                    temp.append(i)
                    break
                elif right-left<100 and i < left and i+100 > right:
                        count += 1
                        temp.append(i)
                        break
        layer_1 = []
        last = -100
        for s in temp:
            if s-last<100 and s>last:
                layer_1.append([last, s])
            layer_1.append([s, s + 100])
            last = s + 100
        layer = layer_1
        # print(layer)

print(count)

"""
3
2 100 280
2 90 360
2 150 360

"""

