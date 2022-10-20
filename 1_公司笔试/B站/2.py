n = int(input())
char_li = list(input())
stack = []
count = 0
for c in char_li:
    if c=='(':
        stack.append(c)
    else:
        if stack:
            stack.pop(-1)
            count+=2
        else:
            print(count)
            break
if not stack:
    print(0)