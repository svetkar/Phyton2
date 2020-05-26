class Date:
    def __init__(self, d):
        self.d = d

    def my_2(self):
        return self.my_1(self.d), self.my_3(self.d)

    @classmethod
    def my_1(cls, s):
        s1 = int(s[0:2] + s[3:5] + s[6:10])
        print(f'{s1}')

    @staticmethod
    def my_3(t):
        if int(t[0:2]) < 1 or int(t[0:2]) > 31:
            print(f'Incorrect day')
        if int(t[3:5]) < 1 or int(t[3:5]) > 12:
            print(f'Incorrect month')
        if int(t[6:10]) < 0 or int(t[6:10]) > 2020:
            print(f'Incorrect year')


date_1 = Date('11-03-2020')
date_1.my_2()
print()
date_2 = Date('33-03-2020')
date_2.my_2()
print()
date_3 = Date('11-13-2020')
date_3.my_2()
print()
date_4 = Date('11-03-2021')
date_4.my_2()
