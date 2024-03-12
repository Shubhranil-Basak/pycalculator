"""
# Module: graph


## Description: It can be used to plot multiple graphs at the same time.

## Supported functions:
    1. Sin
    2. Cos
    3. Tan
    4. Cot
    5. Sec
    6. Cosec
    7. Cot
    8. Log
    9. Exp/e^
    10. abs/| |

## Constants:
    1. pi
    2. e

## Input Format:
    1. Arguments of a function must be inside paranthesis, example: 'sin x' should be written as 'sin(x)'.
    2. Just the expression in x or constants, no need to write 'y = '.
"""

import numpy as np
import matplotlib.pyplot as plt
import re


def main():
    while(True):
        b = input("Enter the equation you want to plot: ")
        if b.lower() == 'end':
            c = input("Do you want to add any y = <constant> or x = <constant> lines?(Y/N): ").upper()
            if c == 'Y':
                y_line = list(map(float, input("Enter the values for y = <constant> line, 0 if none: ").split()))
                x_line = list(map(float, input("Enter the values for x = <constant> line, 0 if none: ").split()))
                for i in y_line:
                    plt.axhline(i, color='red',linewidth=0.5)
                for i in x_line:
                    plt.axvline(i, color='red',linewidth=0.5)
                break
            else:
                break
        else:
            a = b
            a = a.replace('sin', 'np.sin')
            a = a.replace('cos', 'np.cos')
            a = a.replace('tan', 'np.tan')
            a = a.replace('sec', '1/(np.cos)')
            a = a.replace('cosec', '1/(np.sin)')
            a = a.replace('cot', '1/(np.tan)')
            a = a.replace('pi', 'np.pi')
            a = a.replace('log', 'np.log10')
            a = a.replace('ln', 'np.log')
            a = a.replace('e^', 'np.exp')
            a = a.replace('e', 'np.e')
            a = a.replace('^', '**')
            a = a.replace('abs', 'np.abs')
            a = re.sub(r'(\d)x', r'\1*x', a)
            a = re.sub(r'\|([^|]+)\|', r'np.abs(\1)', a)

            x = np.linspace(-9, 10, 1000)
            y = eval(a)
            plt.plot(x, y, label=b)
            plt.legend()

    plt.xticks(np.arange(-10, 11))
    plt.yticks(np.arange(-10, 11))
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.ylim(-10, 10)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Plot of the Equation')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.show()

if __name__ == '__main__':
    main()
