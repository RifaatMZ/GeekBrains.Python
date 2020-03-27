class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        matrix = ""
        for i in range(len(self.lists)):
            for j in range(len(self.lists[i])):
                matrix += f"  {str(self.lists[i][j])}"
            matrix += "\n\n"
        return matrix

    def __add__(self, other):
        matrix = []
        for i in range(len(self.lists)):
            in_list = []
            for j in range(len(self.lists[i])):
                in_list.append(self.lists[i][j] + other.lists[i][j])
            matrix.append(in_list)
        return matrix


a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[1, 2, 3], [4, 5, 6]])
new_matrix = Matrix(a + b)

print(new_matrix)
