import json

firm_dict = {}
average_dict = {"average_profit": ""}
i = 0
prof_sum = 0

with open("text_7.txt") as f_obj:
    for line in f_obj:
        my_list = line.split()
        net = int(my_list[2]) - int(my_list[3])
        firm_dict[my_list[0]] = net
        if net > 0:
            i += 1
            prof_sum += net
    average_dict["average_profit"] = prof_sum / i

py_list = [firm_dict, average_dict]

with open("text_7.json", "w") as out_f:
    json_list = json.dumps(py_list)

print(py_list)
print(json_list)