from itertools import count
from itertools import cycle
from itertools import islice

с = 0
for el in islice((cycle(islice(count(2), 6))), 10):
    print(el)
