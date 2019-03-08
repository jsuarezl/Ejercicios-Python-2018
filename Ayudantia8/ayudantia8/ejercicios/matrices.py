class Matriz:
    def __init__(self, filas, columnas, values):
        self.filas = int(filas)
        self.columnas = int(columnas)
        self.values = list(values)
        matriz = []
        if len(values) != 0:
            for i in range(filas):
                rowList = []
                for j in range(columnas):
                    rowList.append(values[filas * i + j])
                matriz.append(rowList)
        self.matriz = matriz

    def __menor__(self, i, j):  # https://www.programiz.com/python-programming/list#slice
        m = Matriz(self.filas, self.columnas, [])
        m.matriz = [fila[:j] + fila[j + 1:] for fila in (self.matriz[:i] + self.matriz[i + 1:])]
        return m

    def determinante(self, p=False):
        if len(self.matriz) == 2:
            return self.matriz[0][0] * self.matriz[1][1] - self.matriz[0][1] * self.matriz[1][0]
        determinant = 0
        for c in range(len(self.matriz)):
            if p:
                print("c:", c)
                print("d:", determinant)
            determinant += ((-1) ** c) * self.matriz[0][c] * self.__menor__(0, c).determinante()
        return determinant

    def plus(self, matriz):
        values = []
        if self.filas == matriz.filas and self.columnas == matriz.columnas:
            for row in range(0, len(self.matriz)):
                for col in range(0, len(self.matriz[row])):
                    values.append(self.matriz[row][col] + matriz.matriz[row][col])
            return Matriz(self.filas, self.columnas, values)
        else:
            print("Las matrices deben ser del mismo tamaño para poder operarlas.")

    def minus(self, matriz):
        values = []
        if self.filas == matriz.filas and self.columnas == matriz.columnas:
            for row in range(0, len(self.matriz)):
                for col in range(0, len(self.matriz[row])):
                    values.append(self.matriz[row][col] - matriz.matriz[row][col])
            return Matriz(self.filas, self.columnas, values)
        else:
            print("Las matrices deben ser del mismo tamaño para poder operarlas.")

    def times(self, matriz):
        values = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*matriz.matriz)] for X_row in self.matriz]
        m = Matriz(len(values), len(values[0]), [])
        m.matriz = values
        return m

    def __traspuesta__(self, data):
        zip(*data)
        return data

    def divides(self, matriz):
        return self.times(matriz.getMatrixInverse())

    def getMatrixInverse(self):
        determinante = self.determinante()
        if len(self.matriz) == 2:
            return [[self.matriz[1][1] / determinante, -1 * self.matriz[0][1] / determinante],
                    [-1 * self.matriz[1][0] / determinante, self.matriz[0][0] / determinante]]
        cofactores = []
        for r in range(len(self.matriz)):
            cofactorRow = []
            for c in range(len(self.matriz)):
                menor = self.__menor__(r, c)
                cofactorRow.append(((-1) ** (r + c)) * menor.determinante())
            cofactores.append(cofactorRow)
        cofactores = self.__traspuesta__(cofactores)
        for r in range(len(cofactores)):
            for c in range(len(cofactores)):
                cofactores[r][c] = cofactores[r][c] / determinante
        m = Matriz(len(cofactores), len(cofactores[0]), [])
        m.matriz = cofactores
        return m

    def __str__(self):
        return "Filas: {}\n" \
               "Columnas: {}\n" \
               "Valores: {}".format(self.filas, self.columnas, self.__prettymatrix__())

    def __prettymatrix__(self):
        s = "\n"
        for x in self.matriz:
            s += "{}\n".format(x)
        return s
