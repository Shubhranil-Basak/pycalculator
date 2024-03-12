import calculus
import generalCalc
import graph
import Matrices

while(True):
    print("Which calculator you want to use:")
    print(f'''
            1. General calculator
            2. Graphing calculator
            3. Calculus calculator
            4. Matrix calculator
            5. Close the program 
        ''')
    c = input("Enter your choice: ")
    if c == '1':
        generalCalc.main()
    elif c == '2':
        graph.main()
    elif c == '3':
        calculus.main()
    elif c == '4':
        Matrices.main()
    elif c == '5':
        exit()
    else:
        print("Wrong input")
