"""
Make a module called currency.py,
in which its functions are:
increase, decrease, double, half,
currency, and summary.

Make a module called data.py in
which its funcion is: readCurrency.

Transform both modules into packages.

Make a programa that imports this
module and uses these functions.
"""
# importing from modules
# from ex106 import currency, data

#importing from packages
from ex106.util import currency, data

print('-'*40)
price = data.readCurrency('Enter the price: US$')
currency.summary(price, 15, 10)
# print(f'Increasing 20%: {currency.increase(price,20,True)}')
# print(f'Decreasing 13%: {currency.decrease(price,13,True)}')
# print(f'The double of {currency.currency(price)} is {currency.double(price)}.')
# print(f'The half of {currency.currency(price)} is {currency.half(price)}.')

# help(currency.summary)
