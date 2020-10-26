n = int(input())


def even():
    i = 0
    while True:
        if i % 2 == 0:
            yield i
        i += 1


x = even()
for _ in range(n):
    print(next(x))
