"""
Make a algoritm that reads the height and width of a wall,
and returns its surface area as well as the amount of ink
needed to paint it, knowing that each liter of ink covers
an area of 2 square meters.
"""


print('What is the height and width of the wall in meter units?')

height , width = float(input('Height: ')) , float(input('Width: '))

area = height * width

amount_of_ink = area / 2

print('The wall dimension is {:.2f}x{:.2f} and its area is {:.2f}m²'.format(height,\
                                                                width, area))
print('You need {:.2f}L of ink!'.format(amount_of_ink))
