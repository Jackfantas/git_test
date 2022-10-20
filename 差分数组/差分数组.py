# 构造差分数组
class Difference:

    def __init__(self):
        self.diff = []

    def difference(self, nums):
        # construct diff[] based on nums[]
        # e.g. nums:[1,2,3]->diff[1,2-1,3-2]
        self.diff = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                self.diff[i] = nums[i]
            else:
                self.diff[i] = nums[i] - nums[i - 1]
        return self.diff

    def increment(self, i: int, j: int, val):
        # use the diff[] to do the complicated increase/decrease operation
        self.diff[i] += val
        if j < len(self.diff) - 1:
            self.diff[j + 1] -= val

    def result(self):
        # transform diff[] to res[]
        n = len(self.diff)
        res = [0] * n
        for i in range(n):
            if i == 0:
                res[i] = self.diff[i]
            else:
                res[i] = res[i - 1] + self.diff[i]

        return res


if __name__ == '__main__':
    # 差分数组测试用例
    diff = Difference()
    orders = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    di = diff.difference([0] * 5)
    for order in orders:
        i, j, val = order
        i -= 1
        j -= 1
        diff.increment(i, j, val)
    res = diff.result()
    print(res)
