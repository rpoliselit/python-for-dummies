"""
Variables x and y gets a number input as string (str),
and int() transform it into integer number.
Order of mathematical operations:
1. ()
2. **
3. *, /, //, %
4. +, -
"""
x = int(input('type a number: '))
y = int(input('type other number: '))
sum = x + y
sub = x - y
mult = x * y
div = x / y
i_d = x // y
rem = x % y
exp1 = x ** y
exp2 = pow(x,y)

print('The sum of {} and {} is {}.'.format(x,y,sum))
print('The subtraction of {} and {} is {}.'.format(x,y,sub))
print('The multiplication between {} and {} is {}.'.format(x,y,mult))
print('The division of {} by {} is {:.3f}.'.format(x,y,div))
print('The integer division of {} by {} is {},'.format(x,y,i_d), end='')
print(' and its remainder is {}.'.format(rem))
print('{} to the power {} is {} \n the same of {}.'.format(x,y,exp1,exp2))
