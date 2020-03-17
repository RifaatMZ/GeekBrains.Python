from functools import reduce

my_list = [n for n in range(100, 1001) if not n % 2]


def my_func(a, b):
    return a + b


print(my_list)
print(reduce(my_func, my_list))
