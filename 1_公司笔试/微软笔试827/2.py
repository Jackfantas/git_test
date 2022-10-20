def solution(A, N, M):
    res = [0]
    track = []
    A.sort()
    def back_track(start, M):

        if start <= N:
            res[0] = max(res[0], len(track))
            if start == N: return

        for i in range(start, N):
            if track:
                if (A[i]-track[0])%M==0:
                    track.append(A[i])
                    back_track(i+1, M)
                    track.pop(-1)
                else:
                    continue
            else:
                track.append(A[i])
                back_track(i + 1, M)
                track.pop(-1)
    back_track(0, M)
    return res[0]

A = [7,1,11,8,4,10]
A = [-3,-2,1,0,8,7,1]
A = [1,4,7,10,1,4]
N = len(A)
M = 3
res = solution(A, N, M)
print(res)