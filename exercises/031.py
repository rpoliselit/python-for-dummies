"""
Make a program that calculates the price
of travel ticket based on distance.
US$0,50 per km for travels up to 200km of
distance, and US$0,45 per km for longer trips.
"""
color = {'clear' : '\33[m',
        'blue' : '\33[1;35m',
        'white' : '\33[1;37m'}

distance = float(input('{}Enter trip distance in km:{} '.format(color['white'],color['clear'])))
print('-'*20)

price = distance * 0.50 if distance <= 200 else distance * 0.45

#if distance <= 200:
#    price = distance * 0.50
#else:
#    price = distance * 0.45

print('The ticket price is {}US${:.2f}{}.'.format(color['blue'],price,color['clear']))
