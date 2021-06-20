from random import randrange


def gen_random_numbers(qty, min, max):
    while qty > 0:
        yield randrange(min, max)
        qty -= 1


first = gen_random_numbers(5, 0, 100)

for i in first:
    print(i, end=' ')
