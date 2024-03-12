"""
# Module: matrices


## Description: It can perform:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Finding inverse
    5. Finding transpose
    6. Finding RREF
"""

import tkinter as tk
import numpy as np
import sympy

def add_matrices():
    try:
        matrix1 = [[float(entry.get()) for entry in row] for row in entries1]
    except:
        pass
    try:
        matrix2 = [[float(entry.get()) for entry in row] for row in entries2]
    except:
        pass
    try:
        result = np.add(matrix1, matrix2)
    except:
        result = "There is something wrong with the matrix"

    status_label.config(text=f"Result:\n{result}")

def sub_matrices():
    try:
        matrix1 = [[float(entry.get()) for entry in row] for row in entries1]
    except:
        pass
    try:
        matrix2 = [[float(entry.get()) for entry in row] for row in entries2]
    except:
        pass
    try:
        result = np.subtract(matrix1, matrix2)
    except:
        result = "There is something wrong with the matrix"

    status_label.config(text=f"Result:\n{result}")

def mul_matrices():
    try:
        matrix1 = [[float(entry.get()) for entry in row] for row in entries1]
    except:
        pass
    try:
        matrix2 = [[float(entry.get()) for entry in row] for row in entries2]
    except:
        pass
    try:
        result = np.matmul(matrix1, matrix2)
    except:
        result = "There is something wrong with the matrix"
    status_label.config(text=f"Result:\n{result}")

def inv_matrices():
    matrix1 = [[float(entry.get()) for entry in row] for row in entries1]
    try:
        result = np.linalg.inv(matrix1)
    except:
        result = "Matrix is not invertible"
    status_label.config(text=f"Result:\n{result}")

def trans_matrices():
    matrix1 = [[float(entry.get()) for entry in row] for row in entries1]
    try:
        result = np.array(matrix1).T
    except:
        result = "Matrix is not invertible"
    status_label.config(text=f"Result:\n{result}")

def matrix_to_rref():
    try:
        matrix1 = [[float(entry.get()) for entry in row] for row in entries1]
    except:
        pass
    try:
        matrix1 = sympy.Matrix(matrix1)
        rref_matrix, pivot_columns = matrix1.rref()
        rref_matrix = rref_matrix.applyfunc(sympy.nsimplify)
        matrix1 = np.array(rref_matrix)
    except:
        result = "There is something wrong with the matrix"

    status_label.config(text=f"Result:\n{matrix1}")

def get_second_matrix(com):
    global entries2
    entries2 = [[None for _ in range(row)] for _ in range(row)]

    for i in range(row):
        for j in range(row):
            entries2[i][j] = tk.Entry(root, width=10)
            entries2[i][j].grid(row=i, column=j + row + 1)

            
            entries2[i][j].bind("<Up>", on_arrow_key)
            entries2[i][j].bind("<Down>", on_arrow_key)
            entries2[i][j].bind("<Left>", on_arrow_key)
            entries2[i][j].bind("<Right>", on_arrow_key)

    com_list = [add_matrices, sub_matrices, mul_matrices, inv_matrices, trans_matrices, matrix_to_rref]
    submit_button.config(command=lambda: com_list[com - 1]())
    submit_button.grid(row=row, columnspan=row)

def on_arrow_key(event):
    current_widget = root.focus_get()
    current_row, current_col = None, None

    
    for row in range(row_count):
        for col in range(row_count):
            if entries1[row][col] == current_widget:
                current_row, current_col = row, col
                break

    if current_row is not None and current_col is not None:
        if event.keysym == "Up" and current_row > 0:
            entries1[current_row - 1][current_col].focus()
        elif event.keysym == "Down" and current_row < row_count - 1:
            entries1[current_row + 1][current_col].focus()
        elif event.keysym == "Left" and current_col > 0:
            entries1[current_row][current_col - 1].focus()
        elif event.keysym == "Right" and current_col < row_count - 1:
            entries1[current_row][current_col + 1].focus()

    
    for row in range(row_count):
        for col in range(row_count):
            if entries2[row][col] == current_widget:
                current_row, current_col = row, col
                break

    if current_row is not None and current_col is not None:
        if event.keysym == "Up" and current_row > 0:
            try:
                entries2[current_row - 1][current_col].focus()
            except:
                pass
        elif event.keysym == "Down" and current_row < row_count - 1:
            try:
                entries2[current_row + 1][current_col].focus()
            except:
                pass
        elif event.keysym == "Left" and current_col > 0:
            try:
                entries2[current_row][current_col - 1].focus()
            except:
                pass
        elif event.keysym == "Right" and current_col < row_count - 1:
            try:
                entries2[current_row][current_col + 1].focus()
            except:
                pass
def main():
    global row
    global com
    global submit_button
    row = int(input('Enter the dimension of the matrix: '))
    print('''
            1. ADD
            2. SUBTRACT
            3. MULTIPLY
            4. INVERSE
            5. TRANSPOSE
            6. RREF
''')
    com = int(input('Enter the operation you want to perform: '))

    global entries1
    global entries2
    global status_label
    global root
    global row_count

    row_count = row

    root = tk.Tk()
    root.title('Matrix Calculator')

    entries1 = [[None for _ in range(row)] for _ in range(row)]
    entries2 = [[None for _ in range(row)] for _ in range(row)]

    for i in range(row):
        for j in range(row):
            entries1[i][j] = tk.Entry(root, width=10)
            entries1[i][j].grid(row=i, column=j)

            
            entries1[i][j].bind("<Up>", on_arrow_key)
            entries1[i][j].bind("<Down>", on_arrow_key)
            entries1[i][j].bind("<Left>", on_arrow_key)
            entries1[i][j].bind("<Right>", on_arrow_key)

    if (com == 4 or com == 5 or com == 6):
        com_list = [add_matrices, sub_matrices, mul_matrices, inv_matrices, trans_matrices, matrix_to_rref]
        submit_button = tk.Button(root, text="Submit Matrix", command=lambda: com_list[com - 1]())
        submit_button.grid(row=row, columnspan=row)
    else:
        submit_button = tk.Button(root, text="Submit Matrix", command=lambda: get_second_matrix(com))
        submit_button.grid(row=row, columnspan=row)

    status_label = tk.Label(root, text="")
    status_label.grid(row=row+1, columnspan=row)

    root.mainloop()

if __name__ == "__main__":
    main()
