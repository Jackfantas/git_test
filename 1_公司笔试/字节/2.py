s = input()
pre = s[0]
max_len = 1
count = 1
for i in range(1,len(s)):
    if s[i] != pre:
        count += 1
        pre = s[i]
        max_len = max(max_len, count)

    else:
        count = 1
        pre = s[i]
print(max_len)