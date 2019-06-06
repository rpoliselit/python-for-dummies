"""
Make a mini system that uses the
INTERACTIVE HELP of python. User
enters the command, and doc appears.
When user enters 'END', the program
ends.

NOTE1: use colors.
NOTE2: It works as figured out in pycharm so far.
"""

def fancytxt(txt, fg, bg):
    import sys
    from termcolor import cprint
    cprint('~'*len(txt), fg, bg)
    cprint(f'{txt}' , fg, bg, )
    cprint('~'*len(txt), fg, bg)

def thelp(command):
    msg = f" Accessing the command documentation '{command}' "
    fancytxt(msg, 'white', 'on_magenta')
    print('\033[7;30m', end = '')
    help(command, flush = True)
    print('\033[m')


#main program
while True:
    fancytxt(txt=' PyHELP - HELP SYSTEM ', fg='white', bg='on_red')
    ans = str(input('Function or library> ')).strip().lower()
    if ans == 'end':
        fancytxt(' GOOD BYE! ', 'white', "on_green")
        break
    thelp(ans)
