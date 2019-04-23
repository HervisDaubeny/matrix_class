Matrix calculator. (Python)

Contains:
    Addition + size check
    Subtraction + size check
    Multiplication + size check

Plan:
    Approximation of given points in plane by polynom of second
    degree. (Least squares method)
    Input from stdin.
    
Usage:
    The program opens file given as script argument and does 
    operation (+, -, *) given as second argument.

Input file format: 
    #file has to be in folowing format for correct function

    rows columns 			#first matrix
    value value value ... value 		#first row with n values
    ...						#m - 1 rows
    value value value ... value			#m th row with n values
    rows columns			#second matrix
    value value value ... value 		#first row with n values
    ...						#m - 1 rows
    value value value ... value			#m th row with n values

Pylint score:
    Your code has been rated at 9.87/10
