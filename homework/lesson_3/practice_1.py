def divide():
    """
    asks for two numbers to divide them, if division is by 0 then ask again.
    :return: division result
    """
    try:
        a = float(input("Первое число: "))
        b = float(input("Делить на : "))
    except ValueError:
        return
    while b == 0:
        b = float(input("Деление на 0 невозможно! введите другое число: "))
    else:
        return a / b


print(divide())
