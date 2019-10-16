"""
Make a program that simulates the operation
of an ATM. In the beginning, ask the user
what the value to be drawn (integer number),
and the program must inform how many bills of
each value will be delivered.

Note: Consider that the ATM has only 50, 20,
10, and 1 banknotes.
"""

print(f"""{'='*30}\n{'ATM':^30}\n{'='*30}""")

while True:
    withdraw = float(input('Cash withdraw: U$'))
    if withdraw.is_integer() == True:
        break
    else:
        print('Enter an integer value.')

"""
for k in [50,20,10,1]:
    num = withdraw//k
    withdraw -= num * k
    print(f'Total of US${k:>2}: {num:>2.0f}.')
"""

k = 50
while True:
    num = withdraw//k
    withdraw -= num * k
    print(f'Total of US${k:>2}: {num:>2.0f}.')
    if k == 50:
        k = 20
    elif k == 20:
        k = 10
    elif k == 10:
        k = 1
    else:
        break

print(f"""{'='*30}""")
