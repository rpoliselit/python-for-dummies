"""
Make an algoritm that reads the price of a product,
and returns this one with 5% off.
"""

price = float(input('What is the price? US$'))
off = price * (100/100 - 5/100)

print('Its price with 5% off is US${:.2f}.'.format(off))
