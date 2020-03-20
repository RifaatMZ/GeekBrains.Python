numbers = [1, 5, 3, 6, 3, 34]

with open("text_5.txt", "w") as out_f:
    for line in numbers:
        out_f.write(f"{str(line)} ")

with open("text_5.txt", "r") as f_obj:
    for line in f_obj:
        n = map(int, line.split())
        print(sum(n))
