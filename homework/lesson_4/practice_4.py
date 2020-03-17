a_list = [1, 2, 3, 1, 5, 6, 7, 6, 8, 9, 5, 1]

my_list = [el for el in a_list if not a_list.count(el) > 1]

print(my_list)