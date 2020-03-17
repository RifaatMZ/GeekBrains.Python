from sys import argv
from itertools import count
from itertools import cycle


a_list = [1, 2, 3, 4, 5]
name, number = argv

for el in count(int(number)):
    if el > 20:     # this line is only for testing
        break
    else:
        print(el)

c = 0
for el in cycle(a_list):
    if c > 20:       # this line is only for testing
        break
    else:
        print(el)
        c += 1
