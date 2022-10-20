#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bestSumDownwardTreePath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY values
#
from collections import defaultdict


def jp_morgan():
    parent = [-1, 0, 1, 0, 2]
    values = [-5, -10, -10, -10, 10]

    # Write your code here
    tree = defaultdict(list)
    for i, p in enumerate(parent):
        tree[p].append(i)

    print(tree)

    max_sum = -1000

    def dfs(root):
        global max_sum
        print('max_sum: ', max_sum, 'root: ', root)
        if not tree[root]:
            return
        val = values[parent.index(root)]
        print('val: ', val)
        max_sum = max(max_sum, max(max_sum, 0) + val)
        for node in tree[root]:
            dfs(node)

    dfs(-1)

    print('max_sum: ', max_sum)


import random

# 生成[0,20]随机整数
target = random.randint(0, 20)
# 统计猜测次数
guess_count = 0
while True:
    # 输入, str类型
    ss = input('请输入你猜测的数字：')
    # 如果输入q
    if ss == 'q': break
    # 转成整型
    num = int(ss)
    # 如果输入不合要求,重新输入
    if not 0 <= num <= 20:
        print('输入不符合要求，请重新输入[0,20]的整数')
    else:
        # 写在这里代表只有输入合法的情况，才算一次猜测
        guess_count += 1
        # 进入判断逻辑
        if num < target:
            print('太小了')
        elif num > target:
            print('太大了')
        else:
            print(f'猜对了! 猜测次数为{guess_count}')
            while True:
                is_continue = input("输入Y再玩一次, 输入N结束游戏\n")
                # 输入不合法
                if is_continue != 'Y' and is_continue != 'N':
                    print('请输入Y或者N')
                elif is_continue == 'Y':
                    print('继续游戏！')
                    guess_count = 0
                    break
                else:
                    exit('游戏结束！')
# 我在本地修改后提交，验证服务器端是否会同步