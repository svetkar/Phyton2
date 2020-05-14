my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4.txt", "r", encoding="utf8") as f_file:
    content = f_file.readlines()
    with open("text_4_1.txt", "a+", encoding="utf8") as n_file:
        n = 0
        new_list = []
        for i in content:
            z = i.split()
            p = z[1::]
            n = z[0: 1:]
            for el in n:
                m = my_dict.get(el)
                m = str(m)
                p = str(' '.join(p))
                new_list.append(m)
                new_list.append(p)
                b = ' '.join(new_list)
                n_file.write(f'{b}\n')
                new_list = []
