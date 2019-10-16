"""
Make a program that reads tha name of a city from
california, and returns:
1-if its starts or not with 'san'.
2-if its has of not san in any part of name.
"""

city = str(input('Enter a city of California:\n')).strip().title()
city = city.split()

print('Does this city name begin with San?\n','San' in city[0])
print('Does this city name has San?\n', 'San' in city)
