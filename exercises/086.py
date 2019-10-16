"""
Make a program that create a
matrix 3x3 with its values
are read from keyboard.
Show:
[1] - Sum of all even values
[2] - Sum of all values of 3rd column
[3] - greater value of 2nd row
"""

matrix = [[],[],[]]
even = greater = sum_column3 = 0

#read values
for row in matrix:
    for k in range(3):
        row.append(int(input(f'Element[{matrix.index(row)} , {k}]: ')))

#print matrix
print(f'{" MATRIX ":-^30}')
for i , row in enumerate(matrix):
    print('|', end = '')
    for j , element in enumerate(row):
        print(f'{element:^6}', end = '')
        #sum of all even numbers
        if element % 2 == 0:
            even += element
        #sum of all values of 3rd column
        if j == 2:
            sum_column3 += element
        #greater value of 2nd row
        if i == 1:
            if greater == 0 or element > greater:
                greater = element
    print('|')
print(f'{"":-^30}')

#greater = max(matrix[1])

print(f'Sum of all even values: {even}')
print(f'Sum of all values of 3rd column: {sum_column3}')
print(f'Greater value of 2nd row: {greater}')
