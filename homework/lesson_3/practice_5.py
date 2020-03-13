user_input = input("Чтоб найти сумму нажмите Enter, чтоб завершить опирацию введите 'stop'\nВведите числа: ")
user_list = user_input.split()
user_numbers = [int(n) for n in user_list if n.isdigit()]
sum_numbers = sum(user_numbers)

while True:
    if "stop" in user_list:
        break
    else:
        print(sum_numbers)
        user_input = input()
        user_list = user_input.split()
        user_numbers = [int(n) for n in user_list if n.isdigit()]
        sum_numbers += sum(user_numbers)

print(sum_numbers)
