"""
Make a program that has a tuple
fully populated by a count, from
0 to 20. Your program should read
a number from the keyboard, and
display it written.
"""

tuple = ('zero', 'one', 'two', 'three', 'four', 'five',  \
        'six', 'seven', 'eight', 'nine', 'ten', 'eleven', \
        'twelve', 'thirteen', 'fourteen', 'fifteen',     \
        'sixteen', 'seventeen', 'eighteen', 'nineteen',  \
        'twenty')
num = -1
while num not in range(0,21):
    num = int(input('Enter a number between 0 and 20: '))

print(f'The chosen number is {tuple[num]}.')
