from itertools import count

for el in count(2):
    if el > 16:
        break
    else:
        print(el)

my_list = [1, 2, 3, 4]

from itertools import cycle

с = 0
for el in cycle(my_list):
    if с > 8:
        break
    print(el)
    с += 1
