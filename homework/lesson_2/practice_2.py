# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
n = int(input("Вводите количество элементов: "))

for i in range(0, n):
    ele = input()
    my_list.append(ele)
print(my_list)

n -= 1 if n % 2 != 0 else n
x = 0  # list's index steps updater

while x != n:
    my_list[x], my_list[x + 1] = my_list[x + 1], my_list[x]
    x += 2
print(my_list)
