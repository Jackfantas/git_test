from collections import defaultdict
s = input()
min_len = len(s)
c_dict = defaultdict(int)
for c in s:
    c_dict[c] += 1
need = {}
for k in c_dict:
    if c_dict[k] > len(s)//4:
        need[k] = c_dict[k]-len(s)//4
print(need)
valid = 0
if not need:
    print(0)
else:
    window = {}
    left, right = 0, 0
    while right<len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c]==need[c]:
                valid += 1
        while valid==len(need):
            min_len = min(min_len, right-left)
            d = s[left]
            left += 1
            if d in window:
                if window[d]==need[d]:
                    valid -= 1
                window[d] -= 1
    print(min_len)