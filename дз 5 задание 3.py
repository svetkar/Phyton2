with open("text_3.txt", "r", encoding="utf8") as f_file:
    print('Сотрудники с з/п меньше 20 000: ')
    n = 0
    m = 0
    for i in f_file:
        p = float(i.split().pop(1))
        n = n + 1
        m = m + p
        if p < 20000:
            p1 = i.split().pop(0)
            print(p1)
    print(f'Средняя з/п на сотрудника: {m / n}')
