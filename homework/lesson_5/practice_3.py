employer_list = []
salary_list = []

with open("text_3.txt", "r") as f_obj:
    for line in f_obj:
        line_list = line.split()
        try:
            salary_list.append(int(line_list[1]))
            if int(line_list[1]) < 20000:
                employer_list.append(line_list[0])
        except IndexError:
            break
print(employer_list)
print(f"Salary average is {sum(salary_list)/len(salary_list)}")
