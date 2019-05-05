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
        self.value = value
        self.rows = size[0]
        self.columns = size[1]
        for i in range(self.rows):
            for j in range(self.columns):
                self.value[i][j] = int(self.value[i][j])


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


    #no problem with using for i and not using i itself
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
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(int(0))
            res.append(row)
        for i in range(self.rows):
            for j in range(self.columns):
                res[i][j] = self.value[j][i]
        result = Matrix((self.rows, self.columns), res)
        return result


#problem with using for i and not using i itself
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
        #i = 0
        #while i < size_a[0]:
        for i in range(size_a[0]):
            data_a.append(file.readline().split())
            #i += 1
        #reading size of second matrix
        line = file.readline()
        spl = line.split()
        size_b = (int(spl[0]), int(spl[1]))
        #reading values of second matrix
        #i = 0
        #while i < size_b[0]:
        for i in range(size_b[0]):
            data_b.append(file.readline().split())
            #i += 1
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
            data_b.append(int(spl[1]))
    return ((len(data_b), 3), data_a, (len(data_b), 1), data_b)



if __name__ == '__main__':
    if sys.argv[2] == 'A':
        DATA = get_b_v(sys.argv[1])
        print(DATA[1])
        print(DATA[3])
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
                print('It is impossible to multiply first matrix by the second.')
