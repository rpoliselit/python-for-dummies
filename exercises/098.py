"""
Make a program that has a funciton
called greather(), which gets several
parameters with integer values.

Its function has to analyse all values
and returns the geather one.
"""

from random import randint

def greather(* numbers):
    max = 0
    print('-'*40)
    print('Analysing values...')
    if len(numbers) == 0:
        print('There are not values to analyse!')
    elif len(numbers) == 1:
        print(f'Only one listed value, which is {numbers[0]}.')
    else:
        print(f'The {len(numbers)} values listed are: ', end = '')
        for n in numbers:
            print(f'{n}', end = ' ')
            if max == 0 or max < n:
                max = n
        print(f'\nThe greather one among them is {max}.')


a = 100
greather(randint(-a,a),randint(-a,a),randint(-a,a),randint(-a,a),randint(-a,a),randint(-a,a))
greather(randint(-a,a),randint(-a,a),randint(-a,a))
greather(randint(-a,a),randint(-a,a))
greather(randint(-a,a))
greather()
