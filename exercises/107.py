"""
Make a function readInt() that reads only
integer numbers, and another function called
readReal() that reads only float values.
Make the errors treatment.
"""

def readInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('This is not a integer number!')
        except KeyboardInterrupt:
            print('\nUser killed the process.')
            break
        else:
            return n

def readReal(txt):
    while True:
        try:
            n = float(input(txt).strip().replace(',','.'))
        except (ValueError, TypeError):
            print('This is not a float number!')
        except KeyboardInterrupt:
            print('\nUser killed the process.')
            break
        else:
            return n

x = readInt('Enter an integer number: ')
print(x)
y = readReal('Enter a real number: ')
print(y)
