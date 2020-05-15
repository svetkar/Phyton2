s = input('Пожалуйста, введите элементы списка через пробел: ')
s = s.split()
print(f'Заданный список: {s}')
for i in range(1, len(s)):
    if i % 2 != 0:
        s[i - 1], s[i] = s[i], s[i - 1]
print(f'Новый список: {s}')
