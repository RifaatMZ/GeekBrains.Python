with open("text.txt", "w") as f_obj:
    while True:
        string = input()
        if string:
            f_obj.write(f"{string}\n")
        else:
            break
