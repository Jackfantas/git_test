t = int(input())


def is_sushu(x):
    for i in range(2, int(x**0.5)):
        if x % i == 0:
            return False
    return True

for _ in range(t):
    number = int(input())
    if number < 2:
        print("yukari")
        continue
    if is_sushu(number):
        print("kou")
        continue

    step = 0
    while number > 1:
        for i in range(2, number + 1):
            while is_sushu(i) and number%i==0:
                number = number // i
                step += 1


    if step % 2 == 1:
        print("kou")
    else:
        print("yukari")