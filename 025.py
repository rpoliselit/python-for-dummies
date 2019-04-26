"""
Make a programa that read a number between 0 and 9999,
and returns units, tens, hundreds and thousands.
"""


#using only strings
#number = '000'+str(input('Enter a number between 0 and 9999:\n')).strip()
number = str(input('Enter a number between 0 and 9999:\n').zfill(4))
u = number[-1]
t = number[-2]
h = number[-3]
m = number[-4]

#using math
#number = int(input('Enter a number between 0 and 9999:\n'))
#u = number % 10
#t = number // 10 % 10
#h = number // 100 % 10
#m = number // 1000 % 10

#prints
print('Units: {}'.format(u))
print('Tens: {}'.format(t))
print('Hundreds: {}'.format(h))
print('Thousands: {}'.format(m))
