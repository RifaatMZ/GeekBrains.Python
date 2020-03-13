def my_fun(x, y):
    result = 1 / x
    n = -1
    while n > y:
        result /= x
        n -= 1
    return result


def control(x, y):
    result = x ** y
    return result


print(my_fun(2, -3))
print(control(2, -3))
