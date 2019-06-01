"""
Make a program that has a function
called as area, which gets the dimensions
of a retangular ground (length and width),
and show its area.
"""

def ftxt(msg):
    print("-"*30)
    print(f'{msg:*^30}')
    print('-'*30)

def area(l, w):
    a = l * w
    print(f'The area of a ground {l}x{w} is {a}m².')



ftxt(' AREA OF TERRAIN (SI) ')
length = float(input('Lenght (m): '))
width = float(input('Width (m): '))
area(w = width, l = length)
