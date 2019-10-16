"""
Make a program that reads the amount of km that a rented car ran,
and the amount of days this one was rented. Calculate the price of
rental, since the car rental costs US$60 per day amd US$0.15 per km.
"""

km = float(input('How many km? \n'))
days = float(input('How many days? \n'))

rent = 60 * days + 0.15 * km

print('The total cost: US${:.2f}.'.format(rent))
