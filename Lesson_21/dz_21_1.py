class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])

    def m_print(self):
        print(self.matrix)

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Matrix sizes do not match")
        add = []
        for i in range(self.n):
            n = []
            for j in range(self.m):
                n.append(self.matrix[i][j] + other.matrix[i][j])
            add.append(n)
        return Matrix(add)

    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Matrix sizes do not match")
        sub = []
        for i in range(self.n):
            n = []
            for j in range(self.m):
                n.append(self.matrix[i][j] - other.matrix[i][j])
            sub.append(n)
        return Matrix(sub)

    def mul_int(self, int):
        mul_int = []
        for n in self.matrix:
            n_new = []
            for value in n:
                n_new.append(value * int)
            mul_int.append(n_new)
        return Matrix(mul_int)

    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("Matrix sizes do not match")
        elif isinstance(self, Matrix):
            mul = []
            for i in range(self.n):
                n = []
                for j in range(other.m):
                    value = 0
                    for k in range(self.m):
                        value += self.matrix[i][k] * other.matrix[k][j]
                    n.append(value)
                mul.append(n)
            return Matrix(mul)

    def transpose(self):
        tps = []
        for i in range(len(self.matrix[0])):
            n = []
            for j in range(len(self.matrix)):
                n.append(self.matrix[j][i])
            tps.append(n)
        return Matrix(tps)


A = Matrix([[8, -2, 1], [5, 0, 3], [9, 7, 1]])
B = Matrix([[0, 7, 4], [-1, 0, 7], [8, 1, 3]])
C = A + B
D = A - B
E = A.mul_int(4)
F = A * B
G = A.transpose()
print("A:")
A.m_print()
print("B:")
B.m_print()
print("A + B:")
C.m_print()
print("A - B:")
D.m_print()
print("A * 4:")
E.m_print()
print("A * B:")
F.m_print()
print("A transpose:")
G.m_print()
