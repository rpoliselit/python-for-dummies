"""
Make a program that has a function
called readint(), which one works
as input, however this one accept
only integer numbers.
"""

def readint(msg):
    print('-'*40)
    while True:
        intNum = input(msg)
        if intNum.isnumeric() == True:
            break
        else:
            print('\033[91mERROR! Try gain.\033[m')
    return int(intNum)


#main program
n = readint('Enter a integer number: ')
print(f'You typed number {n}.')
