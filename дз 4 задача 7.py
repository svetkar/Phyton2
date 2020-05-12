from math import factorial


def generator():
    for el in [1, 2, 3, 4, 5]:
        yield factorial(el)


g = generator()
print(g)

for el in g:
    print(el)
