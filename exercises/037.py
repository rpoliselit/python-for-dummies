"""
Make a program that converts an integer
number(decimal) into the following basis:
1 - Binary
2 - Hexadecimal
3 - Octal.

The user have to choose between them beforehand.
"""

print('{}\nNUMERICAL BASIS CONVERTER\n{}'.format('-'*20,'-'*20))

num = int(input('Enter a integer number: '))

print("""
[ 1 ] Binary
[ 2 ] Hexadecimal
[ 3 ] Octagonal
""")
choice = int(input('Which one? '))

if choice == 1:
    print('{} in binary is {}.'.format(num,bin(num)[2:]))
elif choice == 2:
    print('{} in hexadecimal is {}.'.format(num,hex(num)[2:]))
elif choice == 3:
    print('{} in octal is {}.'.format(num,oct(num)[2:]))
else:
    print('This is not a valid value.')
