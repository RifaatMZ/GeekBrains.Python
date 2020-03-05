a = float(input("Водите количество КМ: "))
b = float(input("Цель: "))
coefficient = 1.1     #improvement coefficient
i = 1

while True:
    if a < b:
        i += 1
        a *= coefficient
        print(f'{i}-й день: {round(a, 2)}')
        continue
    elif i < 2:
        print("Бегать не надо!")
    break
