# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:04:12 2021

@author: fabic
"""

import numpy as np


sudoku = np.zeros((9,9))
sudoku2 = np.zeros((9,9))

#input start values [rows-1, columns-1]: 
sudoku[0,0] = 7
sudoku[0,2] = 8
sudoku[0,7] = 2
sudoku[2,3] = 2
sudoku[2,4] = 4
sudoku[2,6] = 1
sudoku[3,1] = 9
sudoku[3,6] = 2
sudoku[3,8] = 4
sudoku[4,2] = 6
sudoku[4,3] = 1
sudoku[4,5] = 8
sudoku[5,0] = 5
sudoku[5,4] = 3
sudoku[5,7] = 6
sudoku[6,1] = 2
sudoku[7,4] = 1
sudoku[7,7] = 3
sudoku[8,0] = 1
sudoku[8,5] = 3
sudoku[8,7] = 8
sudoku[8,8] = 6

#input start values [rows-1, columns-1]: 
sudoku2[0,0] = 6
sudoku2[0,2] = 4
sudoku2[0,7] = 8
sudoku2[0,8] = 2
sudoku2[1,4] = 9
sudoku2[1,5] = 7
sudoku2[1,7] = 1
sudoku2[2,2] = 2
sudoku2[2,5] = 4
sudoku2[2,8] = 7
sudoku2[3,1] = 4
sudoku2[3,4] = 6
sudoku2[3,5] = 8
sudoku2[4,0] = 7
sudoku2[4,3] = 1
sudoku2[4,5] = 3
sudoku2[4,8] = 9
sudoku2[5,3] = 7
sudoku2[5,4] = 2
sudoku2[5,7] = 3
sudoku2[6,0] = 4
sudoku2[6,3] = 3
sudoku2[6,6] = 1
sudoku2[7,1] = 9
sudoku2[7,3] = 8
sudoku2[7,4] = 1
sudoku2[8,0] = 2
sudoku2[8,1] = 3
sudoku2[8,6] = 6
sudoku2[8,8] = 8



sudoku2 = sudoku2.astype(int)
sudoku_var = sudoku2

print("The unsolved sudoku:")
print("\n")
print(sudoku2)
print("\n __________________________")
trial_and_error = False

sudoku_solver = np.full((9,9,9),1)

def row_column_update(sudoku_var_work, sudoku_solver_work):
    for row, rows in enumerate(sudoku_var):
        for column, columns in enumerate(rows):
            if sudoku_var_work[row,column] != 0:
                sudoku_solver_work[row, :, sudoku_var[row, column] - 1] = 0
                sudoku_solver_work[:, column, sudoku_var[row, column] - 1] = 0
                sudoku_solver_work[row, column, :] = 0
                sudoku_solver_work[row, column, sudoku_var[row, column] - 1] = 1
    return
            
#actualize sudoku matrix
def update_sudoku(sudoku_var_work, sudoku_solver_work):
    for row, rows in enumerate(sudoku_var):
        for column, columns in enumerate(rows):
            if np.count_nonzero(sudoku_solver[row, column, :] == 1) == 1:
                sudoku_var_work[row, column] = np.where(sudoku_solver[row, column, :] == 1)[0].astype(int) + 1
    return


#Elimanate boxes
def square_update(sudoku_var_work, sudoku_solver_work):
    for row, rows in enumerate(sudoku_var_work):
        for column, columns in enumerate(rows):
            if (row % 3 == 0):
                if (column % 3 == 0):
                    for k in range(3):
                        for l in range(3):
                            if sudoku_var_work[row + k, column + l] != 0:
                                x = sudoku_var_work[row + k, column + l] - 1
                                square_iteration(sudoku_solver_work, x, row, column)
                                sudoku_solver_work[row + k, column + l, x] = 1
                                
    return
                            
                            

def square_iteration(sudoku_solver_work, x, row, column):
    for i in range(3):
        for j in range(3):
            sudoku_solver[row + i, column + j, x] = 0

            

#while(np.count_nonzero(sudoku_var) != 0:

    
for z in range(10):
    row_column_update(sudoku_var, sudoku_solver)
    square_update(sudoku_var, sudoku_solver)
    update_sudoku(sudoku_var, sudoku_solver)
    
 
    
def check_for_empty():
    for row, rows in enumerate(sudoku_var):
        for column, columns in enumerate(rows):
            if np.count_nonzero(sudoku_solver[row, column, :]) == 0:
                valid_solution == False

def check_for_unsolved(sudoku_solver_work):
    for row, rows in enumerate(sudoku_var):
        for column, columns in enumerate(rows):
            if np.count_nonzero(sudoku_solver_work[row, column, :]) > 1:
                return False

def check_for_rows():
    for row, rows in enumerate(sudoku_var):
        for column, columns in enumerate(rows):
            if np.count_nonzero(sudoku_solver[row, column, :]) == 2:
                return [row,column]

sudoku_var_2 = sudoku_var
sudoku_solver_2 = sudoku_solver


"""
if not check_for_unsolved(sudoku_solver):
    trial_and_error = True
    print(np.count_nonzero(sudoku_var))
    A = check_for_rows()
    r = A[0]
    c = A[1]

    for p in range(9):
        if sudoku_solver[r, c, p] != 0:
            sudoku_solver_2[r, c, p] = 0
            for z in range(10):
                row_column_update(sudoku_var_2, sudoku_solver_2)
                square_update(sudoku_var_2, sudoku_solver_2)
                update_sudoku(sudoku_var_2, sudoku_solver_2)
                
            if not check_for_unsolved(sudoku_solver_2):
                sudoku_var = sudoku_var_2
                break
            else:
                print(np.count_nonzero(sudoku_var_2))
                sudoku_solver_2[r, c, p] = 1
                    
        
        
    
    
"""
print("This is the solved sudoku:")
print("\n")
print(sudoku_var)

"""
print("\n")
print("\n")
print("____________________________________")
print(sudoku_solver)
"""

            
#for row, rows in enumerate(sudoku_var):
#    for column, columns in enumerate(rows):
#        if np.count_nonzero(row == 1) == 1:
            
            
