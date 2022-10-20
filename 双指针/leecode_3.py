'''
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
'''


def lengthOfLongestSubstring(s):
    res = 0
    left, right = 0, 0
    window = {}
    n = len(s)
    while right < n:
        r_char = s[right]
        right += 1
        # 更新window
        window[r_char] = window.get(r_char, 0) + 1

        # 判断什么时候收缩左侧，此处为窗口中包含重复元素
        while window[r_char] > 1:
            l_char = s[left]
            left += 1
            # 更新window
            window[l_char] -= 1
        res = max(res, right - left)#之所以不用+1是因为right+=1这步操作。

    return res

s = "abcabcbb"
print(lengthOfLongestSubstring(s))