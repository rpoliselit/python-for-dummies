"""
Make a program that reads two values,
and compare them. It shows in console
one of these messages:
-first number is bigger than second one
-first number is smaller than second one
-they are the same number
"""

n1,n2=float(input('Enter a number: ')),float(input('Enter another number: '))

if n1 > n2:
    print('{} is BIGGER than {}'.format(n1,n2))
elif n1 < n2:
    print('{} is SMALLER than {}'.format(n1,n2))
else:
    print('Both are the SAME number!')

#try it again using 1 and 0.9999999999999999.
