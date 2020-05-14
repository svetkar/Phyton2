with open("text_6.txt", "r", encoding="utf8") as f_file:
    content = f_file.readlines()
    my_dict = {}
    my_list = []
    my_list2 = []
    k = 0
    for i in content:
        i1 = i.split()
        i2 = i1[:1:]
        for el in i2:
            my_dict.setdefault(el)
        for r in i1:
            for u in r:
                if ord(u) > 47 and ord(u) < 58:
                    my_list.append(u)
            b = ''.join(my_list)
            my_list = []
            try:
                k = k + int(b)
            except ValueError:
                k = k
        my_list2.append(k)
        k = 0
for e, w in enumerate(my_dict, 0):
    my_dict.update({w: my_list2[e]})
print(my_dict)
