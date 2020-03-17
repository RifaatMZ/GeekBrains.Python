from sys import argv

script_name, hourly_wage, hours, bonus = argv
salary = (int(hourly_wage) * int(hours)) + int(bonus)

print(salary)



