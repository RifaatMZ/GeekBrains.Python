n = int(input("Введите целое положительное число: "))
max_n = 0

while n > 1:
    m = n % 10
    n = n // 10

    if m > max_n:
        max_n = m

print(max_n)
