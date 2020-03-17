import math


def fibo_gen(n):
    if n > 16:
        for el in range(16):
            yield el
    else:
        for el in range(n):
            yield el
    print('... =', math.factorial(n))


for el in fibo_gen(19):
    print(el)
