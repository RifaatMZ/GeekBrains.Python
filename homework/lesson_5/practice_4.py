new_block = []
my_dict = {"one": "один",
           "two": "два",
           "three": "три",
           "four": "четыре"}

with open("text_4.txt", "r") as f_obj:
    for line in f_obj:
        line_list = line.split(" - ")
        translation = my_dict[line_list[0]]     # можно удалять эту страку, но так понятнее ...
        new_block.append(f"{translation} - {line_list[1]}")

with open("text_4_ru.txt", "w") as out_f:
    for line in new_block:
        out_f.write(line)

