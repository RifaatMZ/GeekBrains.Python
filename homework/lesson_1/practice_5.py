revenue = int(input("ваша выручка: "))
cost = int(input("ваши издержки: "))

financial_results = revenue - cost

if financial_results > 0:
    print("Прибыль")
    profit_margin = financial_results / revenue
    employees_count = int(input("Вводите численность сотрудников фирмы: "))
    profit_per_employee = round(financial_results / employees_count, 2)
    print(f"Прибыль фирмы на одного сотрудника {profit_per_employee}")

elif financial_results == 0:
    print("Ровно")

else:
    print("Убыток")
