"""
Make a program that reads to values,
and show this menu:
[1] Add
[2] Multiply
[3] Which is the greather value
[4] New values
[5] Quit

Your program must realise the chosen
operation.
"""


n1 = n2 = choice = ''
menu = True

while menu:
    if choice == 'N' or n1 == n2 == '':
        print('Enter two numbers:')
        n1 = float(input())
        n2 = float(input())

    print('\nSelect:\n[A]ddition\n[Mu]ltiplication\n[Ma]x\n[N]ewValues\n[Q]uit\n')
    choice = str(input()).upper()
    if choice == 'A':
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    if choice == 'MU':
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    if choice == 'MA':
        if n1 == n2:
            print('Same number!')
        else:
            print('{} > {}'.format(max(n1,n2),min(n1,n2)))
    if choice == 'Q':
        menu = False

print('See you later!')
