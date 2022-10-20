def square():
    for i in range(10):
        yield i ** 2
res = square()
print(type(square()))