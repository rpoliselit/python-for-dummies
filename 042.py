"""
Make a program that reads the length of three lines,
and returns - whether they can form a triangle - its
shape:
-Equilateral
-Isosceles
-Scalene
"""
print('TRIANGLES ANALYSIS')
l1 = float(input('1st length: '))
l2 = float(input('2nd length: '))
l3 = float(input('3rd length: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('This is a', end = '')
    if l1 == l2 and l1 == l3:
        print('n EQUILATERAL TRIANGLE.')
    elif l1 == l2 or l1 == l3:
        print('n ISOSCELES TRIANGLE.')
    else:
        print(' SCALENE TRIANGLE.')
elif l1 + l2 == l3 or l2 + l3 == l1 or l3 + l1 == l2:
    print('This is a DEGENERATE TRIANGLE!')
else:
    print('These lengths do NOT form a triangle!')
