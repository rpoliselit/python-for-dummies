"""
Varible gets an input refered on console by the
phrase enclosed in quotation marks '' or "".
Inputs are alwaeys str type.
Print function prints on console.
"""
name = input('What is your name? ')

#print('Hello ', name ,'! Welcome to python world!')
#print('Hello '+ name +'! Welcome to python world!')
print('Hello {}! Welcome to python world!'.format(name))
