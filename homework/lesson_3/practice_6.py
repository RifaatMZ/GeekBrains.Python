def int_func (word):
    x = word.capitalize()
    return x


user_input = [int_func(n) for n in input("Введите слова: ").split()]
result = ' '.join(user_input)

print(result)
