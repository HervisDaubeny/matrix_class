Matrix calculator. (Python)

Contains:

    Addition + size check (operation +)
    Subtraction + size check (operation -)
    Multiplication + size check (operation *)
    Polynom of second rank approximation (operation A)

Plan:

    Input from stdin.
    
Usage: (in shell)

    matrix.py input_file operation

Matrix calc input file format: 

    #file has to be in folowing format for correct function
    #look to the file input.txt to see more

    rows columns 			#first matrix
    value value value ... value 		#first row with n values
    ...						#m - 1 rows
    value value value ... value			#m th row with n values
    rows columns			#second matrix
    value value value ... value 		#first row with n values
    ...						#m - 1 rows
    value value value ... value			#m th row with n values

Polynom approximation input file format:

    #file needs to be in folowing format for correct function
    #look to the file points.csv to see more

    x_coord, y_coord	#first point
    x_coord, y_coord	#second point
    ...
    x_coord, y_coord	#m-th point

Pylint score:

    #just finished not pylint optimised yet
    Your code has been rated at 9.62/10
