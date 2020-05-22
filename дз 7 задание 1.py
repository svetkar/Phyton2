class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return f'{self.my_list[0][0]}  {self.my_list[0][1]}\n{self.my_list[1][0]}  {self.my_list[1][1]}\n{self.my_list[2][0]}  {self.my_list[2][1]}'

    def __add__(self, other):
        return Matrix([[self.my_list[0][0] + other.my_list[0][0],
                        self.my_list[0][1] + other.my_list[0][1]],
                       [self.my_list[1][0] + other.my_list[1][0],
                        self.my_list[1][1] + other.my_list[1][1]],
                       [self.my_list[2][0] + other.my_list[2][0],
                        self.my_list[2][1] + other.my_list[2][1]]])


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 + matrix_2)
