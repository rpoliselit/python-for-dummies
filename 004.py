"""
Extracting some information about variable 'object'.
"""

object = input('Type anything: ')
print('Its primitive type is {}'.format(type(object)))
print('Is this a number? {}'.format(object.isnumeric()))
print('Is this a letter? {}'.format(object.isalpha()))
print('Is this alphanumeric? {}'.format(object.isalnum()))
print('Is this in captal letter? {}'.format(object.isupper()))
print('Is this in small letters? {}'.format(object.islower()))
