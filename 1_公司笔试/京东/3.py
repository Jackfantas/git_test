n = int(input())
def factotial(number):
    if number==1:
        return 1
    else:
        result = number*factotial(number-1)
        return result

if n < 6:
    print(0)
elif n == 6:
    print(1)
else:
    count = 0
    max_red = n // 3
    other_character = n%3
    for i in range(2, max_red+1):
        other_character = n - i*3
        positon = i + 1
        count += other_character * positon * (26**other_character)

    print(int(count)%(10**9+7))