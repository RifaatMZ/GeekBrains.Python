time_input_sec = int(input("Вводит время в секундах: "))

hours = time_input_sec // 3600
minutes = time_input_sec % 3600 // 60
seconds = time_input_sec % 3600 % 60

print(f"Время: {hours:>02}:{minutes:>02}:{seconds:>02}")
