f_file = open("text1.txt", "a+", encoding="utf8")
m = str(input('Введите строку. Чтобы выйти, нажмите Enter: '))
while True:
    if m != "":
        f_file.write(f"{m}\n")
        m = input('Введите строку для записи в файл. Чтобы выйти, нажмите Enter: ')
    if m == "":
        f_file.close()
        break
