f_file = open("text1.txt", "r", encoding="utf8")
content = f_file.readlines()
n = 0
o = 0
for i in content:
    n = n + 1
    o = i.split()
    print(f'Количество слов в строке {n}: {len(o)}')
    p = 0

print(f'Количество строк {n}')
f_file.close()
