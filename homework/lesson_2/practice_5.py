# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют
# элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 2, 1]
user_input = input("Enter rating: ")

try:
    i = my_list.index(int(user_input))
    my_list.insert(i + 1, int(user_input))

except:
    my_list.append(int(user_input))
    my_list.sort(reverse=True)

print(my_list)
