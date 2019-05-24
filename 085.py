"""
Make a program that create a
matrix 3x3 with its values
are read from keyboard.
Show matrix with correct format.
"""

matrix = [[] , [] , []]

# for k in range(9):
#     if k < 3:
#         matrix[0].append(float(input(f'1st row | {k+1}º number: ')))
#     elif k < 6:
#         matrix[1].append(float(input(f'2nd row | {k-2}º number: ')))
#     else:
#         matrix[2].append(float(input(f'3rd row | {k-5}º number: ')))

for row in matrix:
    for k in range(3):
        row.append(float(input(f'Element[{matrix.index(row)} , {k}]: ')))

for row in matrix:
    print('|', end = '')
    for element in row:
        print(f'{element:^6}', end = '')
    print('|')
