with open("text_2.txt", "r") as f_obj:
    i = 0
    for line in f_obj:
        i += 1
        worlds = len(line.split())
        print(f"In line {i} there are {worlds} word(s).")
    print(f"\nThere are {i} lines")
