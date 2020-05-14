with open("text_5.txt", "w", encoding="utf8") as f_file:
    n = input("Пожалуйста, введите числа, разделенные пробелами: ")
    f_file.write(f"{n}")
with open("text_5.txt", "r", encoding="utf8") as f_file:
    content = f_file.readline()
    c = content.split()
    m = 0
    for i in c:
        i = float(i)
        m = m + i
    print(m)
