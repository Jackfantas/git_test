s = input()
left, right = 0, 0
target = {'r':1, 'e':1, 'd':1}
window = {}
count = 0
res = []
while right < len(s):
    c = s[right]
    right += 1
    if c in target:
        window[c] = window.get(c, 0) + 1
    while right-left >= 3:
        if window['r']==window['e']==window['d']:
            res.append(left)
        d = s[left]
        left += 1
        window[d] -= 1
# print(res)
count = 0
help = {}
for i in range(len(res)-1):
    for j in range(i+1, len(res)):
        if (j-i)%3==0:
            count += 1
print(len(res) + count)