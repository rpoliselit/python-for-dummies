"""
Make a program that plots multiple numbers,
one at a time, for each value entered by
the user. The value is interrupted when the
requested value is negative or rational.
"""

while True:
    num = float(input('Enter a integer number: '))
    if num.is_integer() == False or num < 0:
        print(f'{num} is a negative and/or rational number.')
        break
    for k in range(1,10):
        p = num * k
        print(f'{num:.0f} x {k} = {p:.0f}')
