import re


def find_sum(a_line):
    return sum(map(int, re.findall('\d+', line)))


subjects_dict = {}

with open("text_6.txt") as f_obj:
    for line in f_obj:
        my_list = line.split(":")
        subjects_dict[my_list[0]] = find_sum(line)

    print(subjects_dict)
