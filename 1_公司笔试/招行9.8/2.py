import string

s = input()
stack = []
step = 0
for i in range(len(s)):
    if not stack:
        stack.append(s[i])
    else:
        if s[i]==stack[-1]:
            stack.pop(-1)
            temp = 'r'
            pre = stack[-1] if stack else ''
            next = s[i+1] if i+1 < len(s) else ''
            for c in 'red':
                if c != pre and c != next:
                    temp = c
                    break
            stack.append(temp)
            step += 1
        else:
            stack.append(s[i])
print(stack)
print(step)
