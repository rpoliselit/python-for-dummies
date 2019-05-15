"""
Make a program that reads the gender of
a person, but it only gets 'M' or 'F'
values. While it is wrong, reads again.
"""


'''
while True:
    gender = str(input('Enter your gender [M/F]: ')).strip().upper()[0]
    if gender in 'MF':
        break
print('Done!')
'''

gender = ' '
while gender not in 'MF':
    gender = str(input('Enter your gender [M/F]: ')).strip().upper()[0]
print('Done!')
