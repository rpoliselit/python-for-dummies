"""
Make a program that reads the value of an angles,
and returns the sin, cos, amd tan.
"""

from math import cos, sin, tan, radians

angle = float(input('Enter any angle: '))
sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))
print('sin {:.1f}º = {:.2f}'.format(angle,sin))
print('cos {:.1f}º = {:.2f}'.format(angle,cos))
print('tan {:.1f}º = {:.2f}'.format(angle,tan))
