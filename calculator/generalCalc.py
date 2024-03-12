import numpy as np

def main():
    """
    It can do basic arithmetic and can find values of different functions.
    """
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
            a = a.replace('mod', 'np.abs')
            a = a.replace('e^', 'np.exp')
            a = a.replace('e', 'np.e')

            try:
                print(eval(a))
            except ZeroDivisionError as e:
                print('ERROR, division by zero not allowed')

if __name__ == '__main__':
    main()