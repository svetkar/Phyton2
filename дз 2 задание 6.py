q = input('Хотите ввести товар? (да/нет): ')
i = 0
my_list = []
my_dict2 = {"название": [], "цена": [], "количество": [], "ед.": []}
while True:
    if q == 'да':
        my_dict = {"название": None, "цена": None, "количество": None, "ед.": None}
        i += 1
        q1 = str(input('Введите название: '))
        q11 = {'название': q1}
        my_dict.update(q11)
        my_dict2['название'].append(q1)
        q2 = int(input('Введите цену: '))
        q22 = {'цена': q2}
        my_dict.update(q22)
        my_dict2['цена'].append(q2)
        q3 = int(input('Введите количество: '))
        q33 = {'количество': q3}
        my_dict.update(q33)
        my_dict2['количество'].append(q3)
        q4 = str(input('Введите единицы измерения: '))
        q44 = {'ед.': q4}
        my_dict.update(q44)
        my_dict2['ед.'].append(q4)
        my_list.append((i, my_dict))
        print(my_list)
        q = input('Хотите ввести товар? (да/нет): ')
        continue
    else:
        print(my_list)
        break
print(my_dict2)
