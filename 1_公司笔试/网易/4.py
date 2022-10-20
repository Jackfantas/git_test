a, b, n = [int(i) for i in input().split(' ')]
div = 10 ** 9 + 7
a %= div
b %= div
# dp = [a]
for i in range(2, n):
    temp = (((a * b) % div) ** 2) % div
    a, b = b % div, temp % div
res = b % div
print(res)
