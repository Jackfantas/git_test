# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(S):
    # write your code in Python (Python 3.6)
    def isPalindrome(x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        ans = 0
        while x > ans:
            ans = ans * 10 + x % 10
            x //= 10
        return x == ans or x == (ans // 10)

    S = [i for i in S]
    S.sort()
    result = []
    track = []
    used = [0] * len(S)

    def back_track(index, res):

        int_track = int(''.join(track.copy())) if track else 0
        if isPalindrome(int_track):
            res = max(res, int_track)
            result.append(res)
        if len(track) == len(S):
            return

        for i in range(len(S)):
            if index == 0 and S[i] == '0': continue
            if used[i]: continue
            if i > 0 and S[i] == S[i - 1] and not used[i - 1]:
                continue
            track.append(S[i])
            used[i] = 1
            back_track(index + 1, res)
            track.pop(-1)
            used[i] = 0

    back_track(0, 0)
    return result

S = '90099'
s = solution(S)
print(s)
# s = [1,2]
