import numpy as np
import sympy
import re

def derivative(f, x: sympy.Symbol, val: dict = None):
    if val != None:
        return sympy.diff(f, x).subs(val)
    return sympy.diff(f, x)

def integration(f, x: sympy.Symbol, ul: float=None, ll: float=0):
    if ul != None:
        return sympy.integrate(f, x).subs(x, ul) - sympy.integrate(f, x).subs(x, ll)
    return sympy.integrate(f, x)

def limit(f, x: sympy.Symbol, val: float)->int:
    return sympy.limit(f, x, val)

def series_exp(f, x: sympy.Symbol, term: int):
    return sympy.series(f, x, n=term)

def equation_solve(f, x: sympy.Symbol, val:float = 0):
    equation = sympy.Eq(f, val)
    return sympy.solve(equation, x)

def main():
    while(True):
        b = input("Enter the function: ")
        if b.lower() == 'end':
            break
        else:
            a = b
            a = a.replace('sqrt', 'sympy.sqrt')
            a = a.replace('sin', 'sympy.sin')
            a = a.replace('cos', 'sympy.cos')
            a = a.replace('tan', 'sympy.tan')
            a = a.replace('sec', '1/(sympy.cos)')
            a = a.replace('cosec', '1/(sympy.sin)')
            a = a.replace('cot', '1/(sympy.tan)')
            a = a.replace('pi', 'sympy.pi')
            a = a.replace('log', 'sympy.log')
            a = a.replace('e^', 'sympy.exp')
            a = a.replace('^', '**')
            a = a.replace('mod', 'np.abs')
            a = re.sub(r'(\d)x', r'\1*x', a)
            a = re.sub(r'\|([^|]+)\|', r'sympy.abs(\1)', a)

            x = sympy.symbols('x')
            try:
                f = eval(a)
            except:
                print("Invalid function")
                continue

            print(f'''
                    1. Find Derivative
                    2. Find Integral
                    3. Find Limit
                    4. Series Expansion
                    5. Equation Solver
                    6. Exit
    ''')
            choice = int(input("Enter your option: "))
            if choice == 1:
                com = input('Do you want to find derivativ at a point?(Y/N): ')
                if(com == 'Y' or com == 'y'):
                    x_val = float(input("Enter values of x: "))
                    print(derivative(f, x, {x: x_val}))
                else:
                    print(derivative(f, x))
            elif choice == 2:
                com = input('Do you want to find the definite integral?(Y/N): ')
                if(com == 'Y' or com == 'y'):
                    ul, ll = map(float, input("Enter values of upper limit and lower limit: ").split())
                    print(integration(f, x, ul, ll))
                else:
                    print(integration(f, x))
            elif choice == 3:
                val = float(input("Enter the point where you want to find the limit: "))
                print(limit(f, x, val=val))
            elif choice == 4:
                term = int(input("Enter the degree of the series: "))
                print(series_exp(f, x, term=term))
            elif choice == 5:
                rhs = float(input("Enter the value of the equation: "))
                print(equation_solve(f, x, rhs))
            elif choice == 6:
                break
            else:
                print("Invalid Option")

if __name__ == '__main__':
    main()