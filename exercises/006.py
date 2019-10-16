"""
Make an algoritm that reads a number and prints
its double, triple and square root.
"""

number = float(input('Type a number: '))
double = number*2
triple = number*3
square_root = number**(1/2)

print('Number: {} \n Double: {} \n Triple: {}'.format(number, double, triple))
print('Square root: {:.2f}'.format(square_root))
