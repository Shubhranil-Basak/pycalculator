"""
# Module: generalCalc

## Description: It can perform basic aritmetics

## Supported functions:
    1. Sin
    2. Cos
    3. Tan
    4. Cot
    5. Sec
    6. Cosec
    7. Cot
    8. Log
    9. ln
    10. fac -> factorial
    11. Exp/e^
    12. abs
    13. sqrt

## Constants:
    1. pi
    2. e

## Input Format:
    1. Arguments of a function must be inside paranthesis, example: 'sin x' should be written as 'sin(x)'.
    2. Just the expression in x or constants, no need to write 'y = '.
"""


import numpy as np

def main():
    
    while True:
        a = input("Enter your numbers and functions to calculate: ")
        if a.lower() == 'end':
            break
        else:
            a = a.replace('^', '**')
            a = a.replace('sqrt', 'np.sqrt')
            a = a.replace('sin', 'np.sin')
            a = a.replace('cos', 'np.cos')
            a = a.replace('tan', 'np.tan')
            a = a.replace('cot', '1/(np.tan)')
            a = a.replace('sec', '1/(np.cos)')
            a = a.replace('cosec', '1/(np.sin)')
            a = a.replace('pi', 'np.pi')
            a = a.replace('fac','math.factorial')
            a = a.replace('log', 'np.log10')
            a = a.replace('ln', 'np.log')
            a = a.replace('abs', 'np.abs')
            a = a.replace('e^', 'np.exp')
            a = a.replace('e', 'np.e')

            try:
                print(eval(a))
            except ZeroDivisionError as e:
                print('ERROR, division by zero not allowed')

if __name__ == '__main__':
    main()
