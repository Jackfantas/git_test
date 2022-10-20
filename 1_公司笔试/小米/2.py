data_1 = [1, 2, 3]
data_2 = [4, 5, 6, 7]
n_1, n_2 = 3, 4

d1 = dict(enumerate(data_1))
d2 = dict(enumerate(data_2))
length = n_1 + n_2 - 1

lc = [0] * length
for i in range(length):
    temp = 0
    for j in range(n_1):
        temp += d1[j] * d2.get(i - j, 0)
    lc[i] = temp

mu = [0] * (length + 1)
for i in range(length):
    temp = 0
    for j in range(n_1):
        temp += d1[j] * d2.get((i + j) % length, 0)
    mu[i] = temp
lc = [str(i) for i in lc]
mu = [str(i) for i in mu]
res1, res2 = ' '.join(lc), ' '.join(mu)
print(f'{len(lc)}, {res1}')
print(f'{len(mu)}, {res2}')
