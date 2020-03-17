import math

my_list = [el for el in range(20, 241) if not math.fmod(el, 20) or not math.fmod(el,21)]

print(my_list)