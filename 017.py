"""
Make a program that reads the adjacent and opposite catheta of
a rectangle triangle, and returns the hypotenuse length.
"""

import math

print('-'*20)
ac = float(input('Adjacent cathetus length: '))
oc = float(input('opposite cathetus length: '))
print('-'*20)

#calculating by math.hypot
h1 = math.hypot(ac, oc)
print('The hypotenuse length is {:.2f} by math.hypot.'.format(h1))
print('-'*20)

#calculating by Pythagoras' theorem
h2 = math.sqrt(ac ** 2 + oc ** 2)
print('The hypotenuse length is {:.2f} by Pythagorean theorem.'.format(h2))
print('-'*20)

#calculating by using the amgle
angle = math.atan(oc / ac)
h3 = ac / math.cos(angle)
h4 = oc / math.sin(angle)
angle_degrees = math.degrees(angle)
print('The angle between adjacent and opposite catheta is {:.1f}º.'.format(angle_degrees))
print('The hypotenuse length is {:.2f} by cos {:.1f}º = {:.2f}.'.format(h3, angle_degrees, math.cos(angle)))
print('The hypotenuse length is {:.2f} by sin {:.1f}º = {:.2f}.'.format(h4, angle_degrees, math.sin(angle)))
print('-'*20)
