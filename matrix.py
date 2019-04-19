#!/usr/bin/env python3

'''Matrix class.'''

import sys


class Matrix:
    '''Matrix representation class. Supports: addition, subtracrion,
    multiplication'''
    value = []
    rows = 0
    columns = 0

    def __init__(self, value, size):
        self.value = value
        self.rows = size[0]
        self.columns = size[1]
        for i in range(self.rows):
            for j in range(self.columns):
                self.value[i][j] = int(self.value[i][j])


    def __add__(self, another):
        if self.rows == another.rows and self.columns == another.columns:
            res = self.value
            for i in range(self.rows):
                for j in range(self.columns):
                    res[i][j] += another.value[i][j]
            result = Matrix(res, (self.rows, self.columns))
            return result
        else:
            return 1


    def __sub__(self, another):
        if self.rows == another.rows and self.columns == another.columns:
            res = self.value
            for i in range(self.rows):
                for j in range(self.columns):
                    res[i][j] -= another.value[i][j]
            result = Matrix(res, (self.rows, self.columns))
            return result
        else:
            return 1

    
    def __mul__(self, another):
        if self.columns == another.rows:
            res = []
            res_size = (self.rows, another.columns)
            row = []
            for i in range(res_size[0]):
                row = []
                for j in range(res_size[1]):
                    row.append(int(0))
                res.append(row)
            for i in range(res_size[0]):
                for j in range(res_size[1]):
                    for k in range(?): '''Nasobeni.'''

        return 1


def get_data(in_file):
    '''Loads data to Matricies.'''
    matrix_a = []
    matrix_b = []
    with open(in_file, 'r') as file:
        line = file.readline()
        size_a = (int(line.split()[0]), int(line.split()[1]))
        for i in range(size_a[0]):
            matrix_a.append(file.readline().split())
        line = file.readline()
        size_b = (int(line.split()[0]), int(line.split()[1]))
        for i in range(size_b[0]):
            matrix_b.append(file.readline().split())
    return (matrix_a, size_a, matrix_b, size_b)


if __name__ == '__main__':
    MATRICES = get_data(sys.argv[1])
    mat_a = Matrix(MATRICES[0], MATRICES[1])
    mat_b = Matrix(MATRICES[2], MATRICES[3])
    if sys.argv[2] == '+':
        mat_c = mat_a + mat_b
        if type(mat_c) is Matrix:
            print(mat_c.value)
        else:
            print('Matricies are not of the same type. Addition inposible.')
    if sys.argv[2] == '-':
        mat_c = mat_a - mat_b
        if type(mat_c) is Matrix:
            print(mat_c.value)
        else:
            print('Matricies are not of the same type. Subtraction imposible.')
    if sys.argv[2] == '*':
        .
    
