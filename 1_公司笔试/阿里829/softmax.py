import numpy as np
logits = [2,3,8]
logits = [i/max(logits) for i in logits]
mask = [0, 1, 1]
fenmu = 0
for i in logits:
    fenmu += np.exp2(i)
print(fenmu)
softax = []
for i in range(len(logits)):
    softax.append(np.exp2(logits[i])/fenmu)
print(softax)