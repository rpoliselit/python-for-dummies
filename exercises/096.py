"""
Make a program that has a function
called fancytxt, which gets any text
as parameter, and print a message
with adaptative length
"""

def fancytxt(msg):
    msg = '* '+msg+' *'
    length = len(msg)
    print('~'*length)
    print(f'{msg}')
    print('~'*length)


fancytxt('Hello world!')
fancytxt('Python')
fancytxt('Zen of Python')
