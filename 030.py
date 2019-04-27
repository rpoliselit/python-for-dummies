"""
Make a program that reads a integer number,
and returns its parity.
------------------------
Terminal customization (best choices):
\33[style;text;backm
style: 0,1,4,7.
text color: 30~37
background color: 40~47
"""

number = int(input('{}Enter a integer number: {}'.format('\33[1;37m','\33[m')))
print('\33[1;35m-=-\33[m'*10)

if (number % 2) == 0:
    print('{} is {}even!{}'.format(number,'\33[1;30;41m','\33[m'))
else:
    print('{} is {}odd!{}'.format(number,'\33[1;30;41m','\33[m'))
