a_list = [3, 8, 3, 2, 7, 9, 6, 3, 0, 2, 5, 8, 2, 5]

new_list = [a_list[i] for i in range(1, len(a_list)) if a_list[i - 1] < a_list[i]]

print(new_list)
