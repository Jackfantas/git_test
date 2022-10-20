from collections import defaultdict
def main():
    inHand = "H9 SA SQ SJ S10 H8 C9 D9"
    color_dict = defaultdict(list)
    num_dict = defaultdict(int)
    help_dict = {'A':14, 'K':13,'Q':12, 'J':11}
    for item in inHand.split(' '):
        c, num = item[:1], item[1:]
        if num in help_dict:
            num = help_dict[num]
        else:
            num = int(num)
        color_dict[c].append(num)
        num_dict[num] += 1

    sorted_color = sorted(color_dict.items(), key=lambda x:len(x[1]), reverse=True)
    sorted_num = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)
    print(sorted_color, sorted_num)

    if len(sorted_color[0][1]) >= 5:

        nums = sorted(sorted_color[0][1])
        if nums[-1] == 14 and nums[-5] == 10:
            return "HuangJiaTongHuaShun"
        else:
            is_continue = False
            for i in range(len(nums)-4):
                if nums[i] + 4 == nums[i+4]:
                    is_continue = True
            if is_continue:
                return "TongHuaShun"
            else:
                # sitiao
                if sorted_num[0][1] == 4:
                    return 'SiTiao'
                # hulu
                if sorted_num[0][1] == 3:
                    if sorted_num[1][1] >= 2:
                        return 'HuLu'
                return 'TongHua'

    else:
        nums = sorted(num_dict.keys())
        print(nums)
        if sorted_num[0][1] == 4:
            return 'SiTiao'
        # hulu
        if sorted_num[0][1] == 3:
            if sorted_num[1][1] >= 2:
                return 'HuLu'
        # shunzi
        is_continue = False
        for i in range(len(nums) - 4):
            if nums[i] + 4 == nums[i + 4]:
                is_continue = True
        if is_continue:
            return 'ShunZi'

        # santiao
        if sorted_num[0][1]==3:
            if sorted_num[1][1]<2:
                return 'SanTiao'
        if sorted_num[0][1]==2:
            if sorted_num[1][1] == 2:
                return 'LiangDui'
            else:
                return 'YiDui'
        return 'GaoPai'

res = main()
print(res)