"""
Make a script that converts dollars into bitcoin.
"""

dollars = float(input('How much cash do you have in wallet? \nUS$'))
btc = dollars / 5288.44

print('-' * 20)
print('US${:.2f} = {:.8f} BTC'.format(dollars , btc))
