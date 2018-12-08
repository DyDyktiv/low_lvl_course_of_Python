from sys import stdin


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:
    def __init__(self, arr):
        self.matrix = list(map(list, arr))

    def __str__(self):
        return '\n'.join(map(lambda el: '\t'.join(map(str, el)), self.matrix))

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            for arrs in zip(self.matrix, other.matrix):
                if len(arrs[0]) != len(arrs[1]):
                    raise MatrixError(self, other)
        else:
            raise MatrixError(self, other)
        return Matrix(list(map(lambda lines: list(map(lambda i: i[0] + i[1],
                                                      zip(*lines))),
                               zip(self.matrix, other.matrix))))

    def __mul__(self, n):
        return Matrix(list(map(lambda line: list(map(lambda x: x * n, line)),
                               self.matrix)))

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    @staticmethod
    def transposed(inmatrix):
        return Matrix(list(map(list, zip(*inmatrix.matrix))))

    def transpose(self):
        self.matrix = Matrix.transposed(self).matrix
        return self

    __rmul__ = __mul__


exec(stdin.read())
