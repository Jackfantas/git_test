def solution(X, Y, W):
    # write your code in Python (Python 3.6)
    if not X: return 0
    X.sort()
    start_index = X[0]
    count = 1
    for i in range(len(X)):
        if X[i] <= start_index + W:
            continue
        else:
            start_index = X[i]
            count += 1
    return count

case = [1,2,3,4,5,6,7]
res = solution(case, case, 2)
print(res)