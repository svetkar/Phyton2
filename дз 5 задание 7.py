with open("text_7.txt", "r", encoding="utf8") as f_file:
    content = f_file.readlines()
    my_dict = {}
    my_list = []
    my_list1 = []
    my_list2 = []
    k = 0
    t = 0
    for i in content:
        for el in i.split():
            my_list.append(el)
            break
    for i in content:
        n = i.split()
        rev = int(n[2])
        c = int(n[3])
        p = rev - c
        my_list1.append(p)
    for i in my_list1:
        if i > 0:
            k = k + i
            t = t + 1

        z = k / t
b = {'средняя прибыль': z}
for i in my_list:
    my_dict.setdefault(i)
for i, el in enumerate(my_dict, 0):
    my_dict.update({el: my_list1[i]})
my_list2 = [my_dict, b]
import json

with open("my_file.json", "w") as write_f:
    json.dump(my_list2, write_f, sort_keys=True, indent=4, ensure_ascii=False)
