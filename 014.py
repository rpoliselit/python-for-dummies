"""
Make a script that reads a value in meters,
and return it into km, hm, dam, dm, cm, mm,
µm, nm, inchs, feet, miles...
"""

meters = float(input('Enter a value in meters \n'))

print('-'*40)
print('{}m = {:20}km'.format(meters, meters / 10**3))
print('{}m = {:20}hm'.format(meters, meters / 10**2))
print('{}m = {:20}dam'.format(meters, meters / 10))
print('{}m = {:20}dm'.format(meters, meters * 10))
print('{}m = {:20}cm'.format(meters, meters * 10**2))
print('{}m = {:20}mm'.format(meters, meters * 10**3))
print('{}m = {:20}µm'.format(meters, meters * 10**6))
print('{}m = {:20}nm'.format(meters, meters * 10**9))
print('-'*40)
print('{}m = {:.4f}in'.format(meters, meters * 39.3701))
print('{}m = {:.4f}ft'.format(meters, meters * 39.3701 / 12))
print('{}m = {:.4f}mi'.format(meters, meters * 39.3701 / 12 / 5280))
