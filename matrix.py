#!/usr/bin/env python3

'''Matrix class.'''

import sys


class Matrix:
    '''Matrix representation class. Supports: addition, subtracrion,
    multiplication'''
    value = []
    rows = 0
    columns = 0

    def __init__(self, size, value):
        '''Constructor.'''
        self.value = []
        self.rows = size[0]
        self.columns = size[1]
        for i in range(self.rows):
            line = []
            for j in range(self.columns):
                line.append(int(value[i][j]))
            self.value.append(line)


    def __add__(self, another):
        '''Addition operator overload.'''
        if self.rows == another.rows and self.columns == another.columns:
            res = self.value
            for i in range(self.rows):
                for j in range(self.columns):
                    res[i][j] += another.value[i][j]
            result = Matrix((self.rows, self.columns), res)
            return result
        return 1


    def __sub__(self, another):
        '''Subtraction operator overload.'''
        if self.rows == another.rows and self.columns == another.columns:
            res = self.value
            for i in range(self.rows):
                for j in range(self.columns):
                    res[i][j] -= another.value[i][j]
            result = Matrix((self.rows, self.columns), res)
            return result
        return 1


    def __mul__(self, another):
        '''Multiplication operator overload.'''
        if self.columns == another.rows:
            res = []
            res_size = (self.rows, another.columns)
            row = []
            for i in range(res_size[0]):
                row = []
                for j in range(res_size[1]):
                    row.append(int(0))
                res.append(row)
            for i in range(self.rows):
                for j in range(another.columns):
                    for k in range(self.columns):
                        res[i][j] += self.value[i][k] * another.value[k][j]
            result = Matrix(res_size, res)
            return result
        return 1


    def transpose(self):
        '''Transposition of given matrix.'''
        res = []
        for i in range(self.columns):
            row = []
            for j in range(self.rows):
                row.append(self.value[j][i])
            res.append(row)
        result = Matrix((self.columns, self.rows), res)
        return result


def get_data(in_file):
    '''Loads data from file and returns them. To be passed as arguments to
    Matrix class constructor.'''
    data_a = []
    data_b = []
    with open(in_file, 'r') as file:
        #reading size of first matrix
        line = file.readline()
        spl = line.split()
        size_a = (int(spl[0]), int(spl[1]))
        #reading values for first matrix
        for _ in range(size_a[0]):
            data_a.append(file.readline().split())
        #reading size of second matrix
        line = file.readline()
        spl = line.split()
        size_b = (int(spl[0]), int(spl[1]))
        #reading values of second matrix
        for _ in range(size_b[0]):
            data_b.append(file.readline().split())
    return (size_a, data_a, size_b, data_b)


def get_b_v(in_file):
    '''Loads data for base A and vector b, that is to be approximated to the
    space created as span(A).'''
    data_a = []
    data_b = []
    with open(in_file, 'r') as file:
        while 1:
            line = file.readline()
            if line == "":
                break
            spl = line.split(',')
            row = [int(spl[0])**i for i in range(2, -1, -1)]
            data_a.append(row)
            row = [int(spl[1])]
            data_b.append(row)
    return ((len(data_b), 3), data_a, (len(data_b), 1), data_b)


def switch_rows(first, second, matrix):
    '''Swithces first riw with the second one.'''
    res = matrix
    res[first], res[second] = res[second], res[first]
    return res


def ref_transform(size, matrix, vector):
    '''Transforms the matrix to row echolon form.'''
    res = matrix
    i = 0
    j = 0
    k = 0
    for k in range(3):
        res[k].append(vector[k][0])
        k += 1
    while i < size[0] and j < size[1]:
        #need to find non zero row below
        found = False
        if res[i][j] == 0:
            for k in range(i + 1, size[0]):
                if res[k][j] != 0:
                    #if found switch rows
                    res = switch_rows(i, k, res)
                    found = True
                    break
        else:
            found = True
        #if none is found start searching next column
        if found == False:
            j += 1
        else:
            #making pivot equal to 1
            const = 1 / res[i][j]
            for k in range(j, size[1] + 1):
                res[i][k] *= const
            #making column below to pivot equal to 0
            for k in range(i + 1, size[0]):
                times = res[k][j] / res[i][j]
                for l in range(j, size[1] + 1):
                    if times < 0:
                        res[k][l] += res[i][l] * times
                    if times > 0:
                        res[k][l] -= res[i][l] * times
            i += 1
            j += 1
    return res


if __name__ == '__main__':
    if sys.argv[2] == 'A':
        DATA = get_b_v(sys.argv[1])
        #matrix A
        MAT_A = Matrix(DATA[0], DATA[1])
        #vector B
        VECT_B = Matrix(DATA[2], DATA[3])
        #A transposition
        MAT_AT = Matrix.transpose(MAT_A)
        #A^T * A
        MAT_AT_A = MAT_AT * MAT_A
        #A^T * b
        VECT_AT_B = MAT_AT * VECT_B
        #transformation of A^T|b to REF
        RES = ref_transform((MAT_AT_A.rows, MAT_AT_A.columns), MAT_AT_A.value, VECT_AT_B.value)
        #solving the equasion
        c = RES[2][3]
        b = RES[1][3] - RES[1][2] * c
        a = RES[0][3] - RES[0][2] * c - RES[0][1] * b
        #printed result
        print(str(a))
        print(str(b))
        print(str(c))
    else:
        DATA = get_data(sys.argv[1])
        MAT_A = Matrix(DATA[0], DATA[1])
        MAT_B = Matrix(DATA[2], DATA[3])
        if sys.argv[2] == '+':
            MAT_C = MAT_A + MAT_B
            if isinstance(MAT_C, Matrix):
                print(MAT_C.value)
            else:
                print('Matricies are not of the same type. Addition impossible.')
        if sys.argv[2] == '-':
            MAT_C = MAT_A - MAT_B
            if isinstance(MAT_C, Matrix):
                print(MAT_C.value)
            else:
                print('Matricies are not of the same type. Subtraction impossible.')
        if sys.argv[2] == '*':
            MAT_C = MAT_A * MAT_B
            if isinstance(MAT_C, Matrix):
                print(MAT_C.value)
            else:
                print('It is impossible to multiply first matrix by the second.\
                        one')
